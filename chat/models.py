from django.db import models

# Create your models here.
class History(models.Model):
    user_input = models.CharField(max_length=1000)
    api_output = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_input
    


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Feedback(models.Model):
    COURSE_CHOICES = [
        ('btech', 'B.Tech'),
        ('mtech', 'M.Tech'),
        ('bca', 'BCA'),
        ('mca', 'MCA'),
        ('other', 'Other'),
    ]
    
    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'),
        ('7', '7th Semester'),
        ('8', '8th Semester'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()
    improvements = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.name} - {self.get_course_display()} - {self.rating} stars"