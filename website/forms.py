from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "contact-input",
                    "placeholder": "Votre nom",
                    "autocomplete": "name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "contact-input",
                    "placeholder": "Votre email",
                    "autocomplete": "email",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "contact-input",
                    "placeholder": "Sujet de votre message",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "contact-input contact-textarea",
                    "placeholder": "Votre message",
                    "rows": 7,
                }
            ),
        }

