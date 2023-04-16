from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_plan, name='workout_plan'),
    path('update/<int:workout_id>', views.update_workout_plan, name='update_workout_plan'),
]
