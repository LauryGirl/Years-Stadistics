from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q
from django.utils import timezone
from generics.models import Config

from generics.models import Config
from user import models, serializers
from user.models import User

from .filters import UserFilter

class RoleViewSet(viewsets.ModelViewSet):

    """
    GET: Shows all roles created.\n
    POST: Adds a new role.\n
    GET{id}: Retrieves a specific role determined by id.\n
    PUT{id}: Modifies all fields of a specific role determined by id.\n
    PATCH{id}: Partially modifies the fields of a specific role determined by id.\n
    DELETE{id}: Deletes a specific role determined by id.\n
    """

    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['id', 'name']
    filter_fields = ['admin']


class UserViewSet(viewsets.ModelViewSet):

    """
    Administrative model\n
    GET: Shows all users created.\n
    POST: Adds a new user.\n
    GET{id}: Retrieves a specific user determined by id.\n
    PUT{id}: Modifies all fields of a specific user determined by id.\n
    PATCH{id}: Partially modifies the fields of a specific user determined by id.\n
    DELETE{id}: Deletes a specific user determined by id.\n
    """

    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['id', 'name', 'email', 'last_name']
    filter_class = UserFilter

    def get_queryset(self):
        return models.User.objects.filter(roles__admin=False)


class AdminUserViewSet(viewsets.ModelViewSet):

    """
    Administrative model\n
    GET: Shows all admin users created.\n
    POST: Adds a new admin user.\n
    GET{id}: Retrieves a specific admin user determined by id.\n
    PUT{id}: Modifies all fields of a specific admin user determined by id.\n
    PATCH{id}: Partially modifies the fields of a specific admin user determined by id.\n
    DELETE{id}: Deletes a specific admin user determined by id.\n
    """

    serializer_class = serializers.AdminUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['id', 'name', 'email', 'last_name']
    filter_class = UserFilter

    def get_queryset(self):
        return models.User.objects.filter(roles__admin=True)


class ProfileView(RetrieveUpdateAPIView):

    """
    Administrative model.\n
    GET: Shows the profile of the authenticated user.\n
    PUT{id}: Modifies all fields of the authenticated user.\n
    PATCH{id}: Partially modifies the fields of the authenticated user.\n
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(APIView):

    """
    Logs out a User and deletes the authentication code previously generated. This prevents multiple sessions.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        if not request.user.is_anonymous:
            Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(CreateAPIView):

    """
    Tries to log in a user into the app.\n
    In case the user password combination doesn't match, it returns a 'Not match found' response.\n
    *If the user password combination matches:\n
        *If the user is not verified, returns a 'Not verified' response and sends a new verification code to the user.\n
        *If the user is verified but not active, returns a 'Not active' response.\n
        *If all the previous steps are ok returns an 'OK' response.\n
    """

    serializer_class = serializers.UserLoginSerializer
    permission_classes = [AllowAny]
    queryset = models.User.objects.all()

    def create(self, request):
        serial = self.serializer_class(data=request.data)
        if serial.is_valid():
            data = serial.save()
            data_dict = self.serializer_class(data).data
            return Response(
                data_dict,
                status=status.HTTP_400_BAD_REQUEST if data_dict['status'] != 'OK' else status.HTTP_200_OK)
        return Response(serial.errors, status.HTTP_400_BAD_REQUEST)


class AdminLoginView(CreateAPIView):

    """
    Tries to log in a user into the app.\n
    In case the user password combination doesn't match, it returns a 'Not match found' response.\n
    *If the user password combination matches:\n
        *If the user is not verified, returns a 'Not verified' response and sends a new verification code to the user.\n
        *If the user is verified but not active, returns a 'Not active' response.\n
        *If all the previous steps are ok returns an 'OK' response.\n
    """

    serializer_class = serializers.AdminLoginSerializer
    permission_classes = [AllowAny]
    queryset = models.User.objects.all()

    def create(self, request):
        serial = self.serializer_class(data=request.data)
        if serial.is_valid():
            data = serial.save()
            data_dict = self.serializer_class(data).data
            return Response(
                data_dict,
                status=status.HTTP_400_BAD_REQUEST if data_dict['status'] != 'OK' else status.HTTP_200_OK)
        return Response(serial.errors, status.HTTP_400_BAD_REQUEST)


class RegisterView(CreateAPIView):

    """
    Registers a new User and sends a verification code via email.
    """

    serializer_class = serializers.UserRegisterSerializer
    permission_classes = [AllowAny]
    queryset = models.User.objects.all()

    def create(self, request):
        serial = self.serializer_class(data=request.data)
        if serial.is_valid():

            user = serial.save()
            try:
                send_code(user, 'Para completar tu registro ingresa el siguiente código en tu app: ' +
                          str(user.verification_code), email=True)
            except ValueError as e:
                models.User.objects.filter(id=user.id).delete()
                return Response({'Error': 'Error sending verification code. Check the phone number.'},
                                status.HTTP_400_BAD_REQUEST)

            # google_id = request.data.get('google_id', '')
            # device = request.data.get('device', '')
            # device = FCMDevice.objects.get_or_create(user=models.User.objects.get(
            #     pk=user.pk), registration_id=google_id, type=device)

            return Response({'user': serializers.UserMinimalSerializer(user).data,
                             'verification_code': user.verification_code}, status.HTTP_200_OK)
        return Response(serial.errors, status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):

    """
    Given a verification code and a username (email or phone number)\n
    checks if the combination corresponds to some registered User.\n
    If the combination matches with some User, it returns an authentication token.\n
    """

    serializer_class = serializers.VerifyCodeSerializer

    def post(self, request):
        serial = self.serializer_class(data=request.data)
        if serial.is_valid():
            query_set = models.User.objects.filter(Q(verification_code=serial.validated_data['verification_code']) & (
                Q(email=serial.validated_data['username'])))
            if query_set.exists():
                user = query_set.first()
                elapsed_time = int(
                    (timezone.now() - user.verification_code_created_date).total_seconds() / 60)
                user.verification_code = 0
                user.verification_code_created_date = None

                config_settings = Config.load()

                if elapsed_time <= config_settings.verification_code_validation_time:
                    user.verified = True
                    user.is_active = True
                    token = Token.objects.get_or_create(user=user)
                    user.save()
                    return Response({'token': str(token[0])}, status=status.HTTP_200_OK)
                return Response({'Error': 'Validation time expired.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'Error': 'Incorrect code or username.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):

    """
    Sets a new password for the user given in the request.\n
    """

    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):

        serial = serializers.ChangePasswordSerializer(data=request.data)
        if serial.is_valid():

            user = request.user
            if user.check_password(serial.validated_data['current_password']):
                user.set_password(serial.validated_data['new_password'])
                user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'Error': 'Incorrect current password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class RestorePasswordView(APIView):

    """
    Restores a forgotten password assuming the user has verified his verification code.\n
    """

    serializer_class = serializers.RestorePasswordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serial = self.serializer_class(data=request.data)

        if serial.is_valid():

            user = request.user
            if user.verified:
                user.set_password(serial.validated_data['password'])
                user.verification_code = 0
                user.verification_code_created_date = None
                user.save()
                return Response(status=status.HTTP_200_OK)
            return Response({'Error': 'User not verified.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class RecoverPasswordView(APIView):

    """
    Recover a forgotten password sending an email, assuming the user has verified his verification code.\n
    """
    serializer_class = serializers.RecoverPasswordSerializer

    def post(self, request):

        serial = self.serializer_class(data=request.data)

        if serial.is_valid():
            email = serial.validated_data['email']
            user = User.objects.filter(email = email)
            if user.exists():
                user = user.first()
                if user.verified:
                    config_instance = Config.load()
                    context = {
                        'contactus': config_instance.recover_password_contact_us_url
                    }
                    Token.objects.filter(user=user).delete()
                    token = Token.objects.create(user=user)
                    context['recover'] = config_instance.recover_password_url.format(str(token))
                    message = get_template('mailing/recover.html').render(context)
                    send_mail([email], "Recuperar contraseña", message)
                    return Response({'code': 'email_sent'}, status=status.HTTP_200_OK)
                return Response({'code': 'user_not_verified'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'code': 'not_user'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenValidatorView(APIView):

    """
    Validate existing token.\n
    """
    serializer_class = serializers.TokenSerializer

    def post(self, request):

        serial = self.serializer_class(data=request.data)
        if not serial.is_valid():
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        token = serial.validated_data['token']

        auth_tokens = Token.objects.filter(key = token)
        if auth_tokens.exists():
            user_token = auth_tokens.first()

            now = timezone.localtime(timezone.now()).replace(tzinfo=None)
            time_dif = (now - user_token.created.replace(tzinfo=None))

            if time_dif.days > 1:
                user_token.delete()
                return Response({'code': 'expired_token'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'code': 'ok' }, status=status.HTTP_200_OK)

        return Response({'code': 'no_token'}, status=status.HTTP_400_BAD_REQUEST)

class ChangeRecoverPasswordView(APIView):

    """
    Sets a new password for the recover password process.\n
    """
    serializer_class = serializers.ChangeRecoverPasswordSerializer

    def post(self, request):

        serial = self.serializer_class(data=request.data)
        if serial.is_valid():
            token = serial.validated_data['token']
            auth_tokens = Token.objects.filter(key = token)
            if auth_tokens.exists():
                user_token = auth_tokens.first()
                user = User.objects.filter(id = user_token.user_id).first()
                user.set_password(serial.validated_data['new_password'])
                user.save()
                return Response({ 'code': 'ok' }, status=status.HTTP_200_OK)
            return Response({'code': 'no_token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class SendCodeView(APIView):

    """
    Sends a verification code to a user via the selected send mode (sms, whatsapp, email).\n
    The User is set to inactive (is_active=False) until it verifies the code sent.\n
    """

    serializer_class = serializers.SendCodeSerializer

    def post(self, request):
        serial = self.serializer_class(data=request.data)

        if serial.is_valid():
            query_set = models.User.objects.filter(
                Q(email=serial.validated_data['username']))

            if query_set.exists():

                mode = serial.validated_data['send_mode']

                user = query_set.first()
                verification_code = serializers.generate_code()
                verification_code_created_date = timezone.now()

                try:
                    send_code(
                        user,
                        'Para recuperar contraseña introduce este código: ' +
                        str(verification_code),
                        email=True if mode == 'email' else False)
                except ValueError as e:
                    return Response({'Error': 'Error sending verification code.'}, status.HTTP_400_BAD_REQUEST)

                user.verification_code = verification_code
                user.verification_code_created_date = verification_code_created_date
                user.verified = False
                user.save()

                return Response({'verification_code': user.verification_code}, status=status.HTTP_200_OK)
            return Response({'Error': 'No user matches that username.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    serializer_class = serializers.TokenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = models.User.objects.create(
            name='Test', last_name='User', is_active=True, verified=True, temporary=True)
        token = Token.objects.get_or_create(user=user)
        return Response({'code': 'ok', 'token': token[0].key}, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        if user.is_anonymous:
            return Response({'code': 'no_token'}, status=status.HTTP_200_OK)
        if user.temporary:
            Token.objects.filter(user=user).delete()
            return Response({'code': 'token_erased'}, status=status.HTTP_200_OK)
        return Response({'code': 'not_temporary_user'}, status=status.HTTP_200_OK)
