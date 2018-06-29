from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>i am a noobie programmer<h1>")

