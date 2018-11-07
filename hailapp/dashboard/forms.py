from django import forms
from .models import Adjuster, Claim, ClaimField
from django.contrib.auth.models import User


class NewAdjusterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Adjuster
		fields = ['first_name', 'last_name', 'phone', 'email', 'photo', 'password']

	def save(self, commit=True):
		adjuster = super(NewAdjusterForm, self).save(commit=False)
		u, crt = User.objects.get_or_create(username=self.cleaned_data['email'])
		u.set_password(self.cleaned_data['password'])
		u.is_active = True
		u.save()
		adjuster.user = u
		adjuster.save()
		return adjuster


class ClaimForm(forms.ModelForm):
	price = forms.DecimalField(min_value=0.00, required=False)
	time_limit = forms.DateTimeField(input_formats=['%Y-%m-%d %I:%M %p'])

	class Meta:
		model = Claim
		fields = ['first_name', 'last_name', 'addr_street_1', 'addr_street_1', 'addr_street_2', 
				  'city', 'postal_code', 'phone', 'policy_no', 'loss_no', 'date_of_loss', 
				  'adjusters', 'price', 'time_limit']

	def __init__(self, *args, **kwargs):
		form = super(ClaimForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'


class FieldForm(forms.ModelForm):
	class Meta:
		model = ClaimField
		fields = ['type', 'acres', 'quarter', 'section', 'township', 'range', 'meridian']

	def __init__(self, *args, **kwargs):
		form = super(FieldForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
