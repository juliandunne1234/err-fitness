from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WorkoutPlan
from .forms import WorkoutForm


def workout_plan(request):

    workout_plan_daily = WorkoutPlan.objects.all()

    context = {
        'workout_plan_daily': workout_plan_daily,
    }

    return render(request, 'workout_plan/workout_plan.html', context)


@login_required
def update_workout_plan(request, workout_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))

    workout = get_object_or_404(WorkoutPlan, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout plan')
            return redirect(reverse('workout_plan'))
        else:
            messages.error(request, 'Failed to updated workout plan. Confirm form is valid.')
    else:
        form = WorkoutForm(instance=workout)
        messages.info(request, f'You are editing {workout.category.name}.')

    template = 'workout_plan/update_workout_plan.html'
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)
