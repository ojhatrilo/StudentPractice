# from django.db import models

# # Create your models here.
# class Department(models.Model):
#     Name_Department = models.CharField(max_length=100)
    
#     def __str__(self) -> str:
#         return self.Name_Department
    
    
# class Department_Section(models.Model):
#     Department_Section = models.CharField(max_length=2)
    
#     def __str__(self) -> str:
#         return self.Department_Section

    
# class Data(models.Model):
#     Dept_Name = models.ForeignKey(Department, on_delete=models.CASCADE)
#     Dept_Section = models.ForeignKey(Department_Section, on_delete=models.CASCADE)
#     Student_Reg_No = models.IntegerField()  # Correctly defined IntegerField
#     Student_Name = models.CharField(max_length=100)
#     Student_Email = models.EmailField(max_length=100)
#     Cource_Enrolled = models.CharField(max_length=100)
#     Course_Durtion = models.DurationField()  # Correctly defined DurationField
    
#     class Completion(models.TextChoices):
#         YES = 'Yes'
#         NO = 'No'

#     Cource_Completion = models.CharField(max_length=4, choices=Completion.choices) 

#     def __str__(self) -> str:
#         return self.Student_Name

from django.db import models
from django.core.validators import EmailValidator, RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Department(models.Model):
    Name_Department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.Name_Department
    
    
class Department_Section(models.Model):
    Department_Section = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return self.Department_Section

    
class Data(models.Model):
    Dept_Name = models.ForeignKey(Department, on_delete=models.CASCADE)
    Dept_Section = models.ForeignKey(Department_Section, on_delete=models.CASCADE)
    Student_Reg_No = models.IntegerField(validators=[MinValueValidator(700000000000)])  # Ensuring registration number is positive
    Student_Name = models.CharField(max_length=100)
    Student_Email = models.EmailField(max_length=100, validators=[EmailValidator(message="Enter a valid email address.")])
    Cource_Enrolled = models.CharField(max_length=100)
    Course_Durtion = models.DurationField()  # Correctly defined DurationField
    
    class Completion(models.TextChoices):
        YES = 'Yes'
        NO = 'No'

    Cource_Completion = models.CharField(max_length=4, choices=Completion.choices)

    def clean(self):
        # Custom validation logic
        if not self.Student_Name.isalpha():
            raise ValidationError("Student name should only contain alphabets.")
        if self.Course_Durtion and self.Course_Durtion.total_seconds() <= 0:
            raise ValidationError("Course duration must be positive.")
    
    def __str__(self) -> str:
        return self.Student_Name
