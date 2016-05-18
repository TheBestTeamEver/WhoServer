import json

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from api.models import Level, SimpleUser


def get_true(request, pk):
    level = get_object_or_404(Level, pk=pk)
    photo = level.true_photo
    with open(photo.file.file.name, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def get_fake(request, pk):
    level = get_object_or_404(Level, pk=pk)
    photo = level.fake_photo
    with open(photo.file.file.name, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def get_name(request, pk):
    level = get_object_or_404(Level, pk=pk)
    name = level.name
    return HttpResponse(str(name))


def get_level(request, pk):
    level = get_object_or_404(Level, pk=pk)
    context = {'level': level}
    return render(request, 'api/level.html', context)


def get_all(request):
    levels = Level.objects.all()
    context = {'levels': levels}
    return render(request, 'api/levels.html', context)


@require_http_methods(["POST"])
def registration(request):
    return None


@require_http_methods(["POST"])
def authentication(request):
    return None


def get_top(request):
    users = SimpleUser.objects.all().order_by('-rating')
    response = {'data': [{'login': u.login, 'rating': u.rating} for u in users]}
    return JsonResponse(response)


def get_random_urls(request):
    levels = Level.objects.all().order_by('?')[:10]
    response = {
        'data': [{
                     'name': level.name,
                     'true': level.true_photo.url,
                     'fake': level.fake_photo.url
                 } for level in levels]
    }
    return JsonResponse(response)
