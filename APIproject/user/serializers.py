from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from user.models import Role

from .tasks import generate_code, is_admin, send_code

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    roles_id = serializers.ListField(required=False, write_only=True)
    roles = RoleSerializer(many=True, read_only=True)
    
    def create(self, validated_data):

        password = None

        if 'new_password' in validated_data:
            password = validated_data.pop('new_password')

        user = User.objects.create(**validated_data)

        if not (password is None) and (len(password) > 0):
            user.set_password(password)
            user.save()

        user.roles.add(Role.objects.get(name='Usuario'))
        user.save()

        return user

    def update(self, instance, validated_data):

        password = None

        if 'new_password' in validated_data:
            password = validated_data.pop('new_password')

        instance = super(UserSerializer, self).update(
            instance, validated_data)

        if not (password is None) and (len(password) > 0):
            instance.set_password(password)
            instance.save()

        instance.save()
        return instance

    class Meta:
        model = User
        exclude = ['password']


class AdminUserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    roles_id = serializers.ListField(required=False, write_only=True)
    roles = RoleSerializer(many=True, read_only=True)
        
    def create(self, validated_data):

        password = None
        roles_id = None

        if 'new_password' in validated_data:
            password = validated_data.pop('new_password')

        if 'roles_id' in validated_data:
            roles_id = validated_data.pop('roles_id')

        user = User.objects.create(**validated_data)

        if not (password is None) and (len(password) > 0):
            user.set_password(password)
            user.save()

        if roles_id is not None:
            roles = Role.objects.filter(id__in=roles_id)
            for role in roles:
                user.roles.add(role)

        user.save()

        return user

    def update(self, instance, validated_data):

        password = None
        roles_id = None

        if 'new_password' in validated_data:
            password = validated_data.pop('new_password')

        if 'roles_id' in validated_data:
            roles_id = validated_data.pop('roles_id')

        instance = super(AdminUserSerializer, self).update(
            instance, validated_data)

        if not (password is None) and (len(password) > 0):
            instance.set_password(password)
            instance.save()

        if roles_id is not None:
            roles = Role.objects.filter(id__in=roles_id)
            instance.roles.clear()
            for role in roles:
                instance.roles.add(role)

        instance.save()
        return instance

    class Meta:
        model = User
        exclude = ['password']


class UserProfileSerializer(serializers.ModelSerializer):

    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'roles', 'last_name']


class UserNotificationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'last_name']


class UserMinimalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'email']


class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    verification_code = serializers.IntegerField(read_only=True)
    is_active = serializers.CharField(read_only=True)
    user = UserMinimalSerializer(many=False, read_only=True)
    error = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    login_statuses = {'OK': 'OK', 'Not_verified': 'Not Verified',
                      'Not_active': 'Not Active', 'Not_match_found': 'Not Match Found'}

    def save(self):

        query_set = User.objects.filter(email=self.validated_data['username'])

        if query_set.exists() and query_set.first().check_password(self.validated_data['password']):
            user = query_set.first()

            if is_admin(user):
                Token.objects.filter(user=user).delete()
                token = Token.objects.create(user=user)
                user.save()
                return {'token': str(token), 'user': user, 'status': self.login_statuses['OK']}
            else:
                return {'error': 'You are not an administrator user.', 'status': 'Not Allowed'}
        return {'status': self.login_statuses['Not_match_found']}


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    verification_code = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    user = UserMinimalSerializer(many=False, read_only=True)
    error = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    login_statuses = {'OK': 'OK', 'Not_verified': 'Not Verified',
                      'Not_active': 'Not Active', 'Not_match_found': 'Not Match Found'}

    def save(self):

        query_set = User.objects.filter(email=self.validated_data['username'])

        if query_set.exists() and query_set.first().check_password(self.validated_data['password']):
            user = query_set.first()

            if user.verified:
                if user.is_active:
                    Token.objects.filter(user=user).delete()
                    token = Token.objects.create(user=user)
                    user.save()
                    return {'token': str(token), 'user': user, 'status': self.login_statuses['OK']}
                else:
                    return {'status': self.login_statuses['Not_active']}
            else:
                user.verification_code = generate_code()
                user.verification_code_created_date = timezone.now()
                user.save()

                try:
                    send_code(user, 'User not verified. New verification code: ' +
                              str(user.verification_code), email=True)
                except ValueError as e:
                    return {
                        'error': 'Error sending verification code. Check your email address.',
                        'status': 'Message Error'}

                return {'verification_code': user.verification_code, 'user': user,
                        'status': self.login_statuses['Not_verified']}
        return {'status': self.login_statuses['Not_match_found']}


class UserRegisterSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):

        user = super(UserRegisterSerializer, self).save(**kwargs)

        user.verification_code = generate_code()
        user.verification_code_created_date = timezone.now()
        user.registration_date = timezone.now()
        user.roles.add(Role.objects.get(name='Usuario'))

        password = self.validated_data['password']
        if not (password is None) and (len(password) > 0):
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = User
        exclude = ['roles', 'verification_code',
                   'verification_code_created_date']
        extra_kwargs = {
            'new_password': {'write_only': True}
        }


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangeRecoverPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class VerifyCodeSerializer(serializers.Serializer):
    verification_code = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

class RestorePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

class SendCodeSerializer(serializers.Serializer):
    send_choices = ('email')
    username = serializers.CharField(write_only=True)
    send_mode = serializers.ChoiceField(choices=send_choices)

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

class RecoverPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)