# serializers.py

from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise

class ExerciseSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'video_file', 'duration', 'repetitions']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'exercise_id', 'order']


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, source='workoutexercise_set', required=False)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'exercises', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        # ← УБИРАЕМ user ИЗ validated_data
        exercises_data = validated_data.pop('workoutexercise_set', [])
        # user передаётся через perform_create
        workout = Workout.objects.create(**validated_data)

        for i, ex_data in enumerate(exercises_data):
            WorkoutExercise.objects.create(
                workout=workout,
                exercise_id=ex_data['exercise_id'],
                order=i
            )
        return workout