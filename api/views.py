import json

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.models import Level, SimpleUser

from django.http import HttpResponseRedirect

from .forms import UploadFileForm


def get_level(request, pk):
    level = get_object_or_404(Level, pk=pk)
    context = {'level': level}
    return render(request, 'api/level.html', context)


def get_all(request):
    levels = Level.objects.all()
    context = {'levels': levels}
    return render(request, 'api/levels.html', context)


def get_names(request):
    levels = Level.objects.all()
    context = {'levels': levels}
    return render(request, 'api/names.html', context)


def check_login(login):
    try:
        SimpleUser.objects.get(login=login)
        return True
    except Exception:
        return False


def check_auth(login, password):
    try:
        SimpleUser.objects.get(login=login, password=password)
        return True
    except Exception:
        return False


@csrf_exempt
@require_http_methods(["POST"])
def authentication(request):
    login = request.POST.get('login')
    password = request.POST.get('password')

    if login is None or password is None:
        response = {'data': 'No some fields'}
        return JsonResponse(response)

    if login == "" or password == "":
        response = {'data': 'No some fields'}
        return JsonResponse(response)

    if check_login(login):
        if check_auth(login, password):
            response = {'data': 'Ok'}
        else:
            response = {'data': 'Wrong login/password'}
        return JsonResponse(response)
    else:
        SimpleUser(login=login, password=password).save()
        response = {'data': 'Ok'}
        return JsonResponse(response)


@csrf_exempt
@require_http_methods(["POST"])
def put_score(request):
    login = request.POST.get('login')
    score = request.POST.get('score')

    if login is None or score is None:
        response = {'data': 'fail'}

    try:
        score = int(score)
        user = SimpleUser.objects.get(login=login)
        if user.rating < score:
            user.rating = score
            user.save()

        response = {'data': 'Ok'}
    except Exception:
        response = {'data': 'fail'}

    return JsonResponse(response)


def get_top(request):
    users = SimpleUser.objects.all().order_by('-rating')
    response = {'data': [{'login': u.login, 'rating': u.rating} for u in users]}
    return JsonResponse(response)


def get_random_urls(request):
    levels = Level.objects.all().order_by('?')[:10]
    response = {
        'data': [{
                     'true_name': level.true_name,
                     'fake_name': level.fake_name,
                     'true_photo': level.true_photo.url,
                     'fake_photo': level.fake_photo.url
                 } for level in levels]
    }
    return JsonResponse(response)


# MAXIM FORM
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Files uploaded")
    else:
        form = UploadFileForm()
        return render_to_response('api/upload.html', {'form': form})
