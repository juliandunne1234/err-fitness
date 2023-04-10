from django.shortcuts import render


def workout_plan(request):
    return render(request, 'workout_plan/workout_plan.html')
