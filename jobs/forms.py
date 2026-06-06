from django import forms
from .models import ConsultationRequest


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = [
            'full_name',
            'phone',
            'email',
            'interested_country',
            'profession',
            'message',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism familiyangiz'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+998 90 123 45 67'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email manzilingiz'
            }),
            'interested_country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Qaysi davlatga bormoqchisiz?'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kasbingiz'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Qo‘shimcha ma’lumot yozing...',
                'rows': 5
            }),
        }


# Employer job creation form
from .models import Job
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'country', 'city', 'address', 'salary', 'experience', 'description', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: Senior Python Developer'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: USA, Canada, Germany'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: New York, Toronto'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: 123 Main St, Suite 100'
            }),
            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: $5000 - $10000/month'
            }),
            'experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masalan: 3-5 years'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ish tavsifi, talablar, va boshqa malumotlar',
                'rows': 6
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }