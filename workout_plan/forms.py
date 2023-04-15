from .models import WorkoutPlan, WorkoutCategory
from django import forms


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = WorkoutPlan
        exclude = ('day_of_week', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
