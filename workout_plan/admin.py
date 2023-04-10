from django.contrib import admin
from .models import WorkoutCategory, DayOfWeek, WorkoutPlan


admin.site.register(WorkoutCategory)
admin.site.register(DayOfWeek)
admin.site.register(WorkoutPlan)
