from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def error_404(request, exception):
    return render(request, 'home/404.html', status=404)


def error_500(request):
    return render(request, 'home/500.html', status=500)
