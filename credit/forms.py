from django.forms import ModelForm
from credit.models import Credit  

class CreditForm(ModelForm):  
    class Meta:  
        model=Credit
        fields = "__all__" 