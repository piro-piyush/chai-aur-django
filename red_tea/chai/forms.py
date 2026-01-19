from django import forms
from .models import Chai

class ChaiStoreSearchForm(forms.Form):
    type = forms.ChoiceField(
        choices=[('', 'All Types')] + list(Chai.ChaiType.choices),
        label="Select Chai Type",
        required=False
    )
    size = forms.ChoiceField(
        choices=[('', 'All Sizes')] + list(Chai.ChaiSize.choices),
        label="Select Chai Size",
        required=False
    )
