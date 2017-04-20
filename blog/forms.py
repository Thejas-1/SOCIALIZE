from django import forms

class UserForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Email_ID =  forms.CharField(max_length=200)
    mobile =  forms.CharField(max_length=20)
    DOB =  forms.CharField(max_length=30)
    Flag =  forms.CharField(max_length=1)
    ORG =  forms.CharField(max_length=200)




    

