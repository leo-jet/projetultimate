from django import forms

from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
                                 )

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Cet utilisateur n existe pas")
        if not user.check_password(password):
            raise forms.ValidationError("Mot de pass incorrect")
        if not user.is_active:
            raise forms.ValidationError("Cet utilisateur n est plus active")
        return super(UserLoginForm, self).clean(*args, **kwargs)