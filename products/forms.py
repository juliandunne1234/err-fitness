from .models import Product, Category, Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product', 'comment', 'rating', 'review_by')

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', }),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5'}),
            'review_by': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'reviewer_name', 'type': 'hidden'}),
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
