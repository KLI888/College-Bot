from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'course', 'semester', 'rating', 'feedback', 'improvements']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.RadioSelect(),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please share your experience with our ChatMate assistant...', 'rows': 5}),
            'improvements': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can we make ChatMate better for your learning experience?', 'rows': 5}),
        }
        
        labels = {
            'feedback': 'Your Feedback',
            'improvements': 'Suggestions for Improvement',
        }