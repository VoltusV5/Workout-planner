from django.db import models
from django.contrib.auth.models import User

# Модель для упражнений
class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='exercises_videos/', null=True, blank=True)
    duration = models.IntegerField(default=30)
    repetitions = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # ← или ['id']

    def __str__(self):
        return self.name

# Модель для тренировки 
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# Модель для порядка упражнений в тренировке
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
