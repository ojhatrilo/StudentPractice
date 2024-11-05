# from django.forms import ModelForm
# from .models import Data


# class DataForm(ModelForm):
#     class Meta:
#         model = Data
#         fields = '__all__'
        
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['Dept_Name', 'Dept_Section', 'Student_Reg_No', 'Student_Name', 'Student_Email', 'Cource_Enrolled', 'Course_Durtion', 'Cource_Completion']
        
        widgets = {
            'Dept_Name': forms.Select(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Dept_Section': forms.Select(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Student_Reg_No': forms.NumberInput(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Student_Name': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Student_Email': forms.EmailInput(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Cource_Enrolled': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Course_Durtion': forms.TextInput(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'Cource_Completion': forms.Select(attrs={'class': 'appearance-none border rounded w-full text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
        }
