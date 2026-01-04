from django.shortcuts import render

from to_do.models import Task

# views
def home(request):
    work = Task.objects.filter(is_completed = False).order_by('updated_at')
    free = Task.objects.filter(is_completed = True)
    context = {
        'work': work,
        'free' : free,
    }
    return render(request, 'home.html', context)