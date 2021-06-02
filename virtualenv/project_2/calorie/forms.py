from django import forms
from .models import Info, Calorie

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        
        fields = [
			'name',
			'gender',
			'age',
            'weight',
		]
        
        labels = {
			'name': 'Name',
			'gender':'Gender',
			'age':'Age',
            'weight':'Weight',
		}

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        
        fields = [
            'food_type',
            'calories',
            'food_type1',
            'calories1',
            'food_type2',
            'calories2',
            'food_type3',
            'calories3',
		]

        labels = {
			'food_type': 'Food Type',
			'calories':'Calories',
            'food_type1': 'Food Type',
			'calories1':'Calories',
            'food_type2': 'Food Type',
			'calories2':'Calories',
            'food_type3': 'Food Type',
			'calories3':'Calories',
		}
        