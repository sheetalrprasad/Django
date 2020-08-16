from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name should start with Z")

class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    # botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
    #                             validators = [validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

    def clean(self):
        all_clean_value = super().clean()
        email = all_clean_value['email']
        vemail = all_clean_value['verify_email']

        if email != vemail:
            raise forms.ValidationError("Email Verification Failed.")
