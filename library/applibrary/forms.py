from django import forms

class LoginForm(forms.Form):
    phone = forms.CharField(
        label="נייד",
        required=True,
        widget=forms.TextInput(attrs={'class': 'my-input', 'placeholder': ' הכנס מספר נייד'})
    )
    password = forms.CharField(
        label="סיסמה",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'my-input', 'placeholder': 'הכנס סיסמה'})
    )
class BorrowedForm(forms.Form):
    password = forms.CharField( widget=forms.PasswordInput)