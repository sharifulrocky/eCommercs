from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="max 100 text", label="Your name")
    email = forms.CharField(required=True, label="Your email", help_text="Enter Valid email")
    comment = forms.CharField(required=True, widget=forms.Textarea)
