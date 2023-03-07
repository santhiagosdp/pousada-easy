from django import forms
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User

'''
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
        
'''
    



from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditarUsuarioForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Endereço de email',
            #'is_active': 'Conta ativa',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha antiga'}),
        label='Senha antiga'
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nova senha'}),
        label='Nova senha'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmação de senha'}),
        label='Confirmação de senha'
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
