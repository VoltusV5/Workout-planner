from django.db import models
from django.contrib.auth.models import User

# Модель для упражнений
class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='exercises_videos/')
    duration = models.IntegerField()
    repetitions = models.IntegerField()

    def __str__(self):
        return self.name
    

# Модель для тренировки 
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

# Модель для порядка упражнений в тренировке
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.exercise.name} - {self.workout.name}"