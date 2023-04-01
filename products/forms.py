from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product', 'comment', 'rating', 'review_by')

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control',}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5'}),
            'review_by': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'reviewer_name', 'type': 'hidden'}),
        }