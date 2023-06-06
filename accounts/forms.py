# Django
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

# Local Django
from .models import Account,UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name"}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username"}
        )
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter Your Email"}
        ),
    )
    password1 = forms.CharField(
        min_length=4,
        max_length=16,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password"}
        ),
    )
    password2 = forms.CharField(
        min_length=4,
        max_length=16,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Your Password"}
        ),
    )

    class Meta:
        model = Account
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if Account.objects.filter(username=username).exists():
    #         if Account.objects.get(username=username).is_active == False:
    #             return username
    #         raise forms.ValidationError("This username is already taken.")
    #     # elif not re.match('^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',username):
    #     #     raise forms.ValidationError('Username Must Contains Alphabetics and Numerics')
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if Account.objects.filter(email=email).exists():
    #         if Account.objects.get(email=email).is_active == False:
    #             return email
    #         raise forms.ValidationError("This email is already taken.")
    #     return email

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-content"
    
    

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name')
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs["placeholder"] = "First Name"
        self.fields['last_name'].widget.attrs["placeholder"] = "Last Name"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control bg-dark text-white"
            self.fields[field].widget.attrs["style"] = "border-color: #A32CC4"
        
class UserProfileForm(forms.ModelForm):
    
    profile_picture = forms.ImageField(required=False,error_messages={'invalid':('Image Files Only')},widget = forms.FileInput)
    
    class Meta:
        model = UserProfile
        fields = ('address_line_1','address_line_2','phone_number','city','state','country','profile_picture')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['address_line_1'].widget.attrs["placeholder"] = "Address Line 1"
        self.fields['address_line_2'].widget.attrs["placeholder"] = "Address Line 2"
        self.fields['phone_number'].widget.attrs["placeholder"] = "Phone Number"
        self.fields['city'].widget.attrs["placeholder"] = "City"
        self.fields['state'].widget.attrs["placeholder"] = "State"
        self.fields['country'].widget.attrs["placeholder"] = "Country"
        
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control bg-dark text-white"
            self.fields[field].widget.attrs["style"] = "border-color: #A32CC4"