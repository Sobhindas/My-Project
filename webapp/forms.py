from django import forms
from webapp.models import Cart,Contact

class Cartform(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "_all_"
class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "_all_"