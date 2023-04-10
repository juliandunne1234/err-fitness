from django.shortcuts import render
from .models import WorkoutPlan


def workout_plan(request):

    workout_plan_daily = WorkoutPlan.objects.all()

    context = {
        'workout_plan_daily': workout_plan_daily,
    }

    return render(request, 'workout_plan/workout_plan.html', context)
