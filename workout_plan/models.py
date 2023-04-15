from django.db import models


class WorkoutCategory(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class DayOfWeek(models.Model):
    day_of_week = models.CharField(max_length=100)

    def __str__(self):
        return self.day_of_week


class WorkoutPlan(models.Model):

    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE)
    workout_time = models.IntegerField(null=False, blank=False, default=45)
    day_of_week = models.OneToOneField(DayOfWeek, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review {self.day_of_week}"
