from django import forms
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, PasswordInput

from user.models import Role, User


class UserForm(ModelForm):
    new_password = forms.CharField(widget=PasswordInput(), required=False)

    def save(self, commit=True):
        user = super().save(commit=commit)
        if len(self.data['new_password']) > 0:
            user.set_password(self.data['new_password'])
            user.save()
        return user

    class Meta:
        model = User
        exclude = ['password']


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ['name', 'last_name', 'email']
    list_display_links = ('name', 'last_name', 'email')
    form = UserForm


def CustomModelAdmin(model):
    return type('SubClass' + model.__name__,
                (admin.ModelAdmin,
                 ),
                {'list_display': [x.name for x in model._meta.fields],
                    'list_select_related': [x.name for x in model._meta.fields if isinstance(x,
                                                                                             (models.ManyToOneRel,
                                                                                              models.ForeignKey,
                                                                                              models.OneToOneField,
                                                                                              ))],
                 'search_fields': ['id'],
                 'list_display_links': ['id'],
                 })


admin.site.register(User, UserAdmin)
admin.site.register(Role, CustomModelAdmin(Role))