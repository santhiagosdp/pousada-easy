from django import forms
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        #user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
