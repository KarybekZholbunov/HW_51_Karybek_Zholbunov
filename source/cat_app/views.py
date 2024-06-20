from django.shortcuts import render, redirect
from .models import Cat


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cat = Cat.objects.create(name=name)
        return redirect('cat_info', cat_id=cat.id)
    return render(request, 'home.html')


def cat_info(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()
        cat.save()
    return render(request, 'cat_info.html', {'cat': cat})