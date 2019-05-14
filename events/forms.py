from django import forms
from .models import Person

class events_form(forms.ModelForm):
	name = forms.CharField(widget = forms.TextInput(), required = True , max_length = 100)
	roll_no  = forms.CharField(widget = forms.NumberInput(), required = True )
	email  = forms.EmailField(widget = forms.EmailInput(), required = True , max_length = 100)
	phone  = forms.CharField(widget = forms.NumberInput(), required = True )
    
	class Meta:
		model = Person  
		fields = ['name' ,'roll_no', 'email' , 'phone']

