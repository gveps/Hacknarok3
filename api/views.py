from django.http import JsonResponse
from django.shortcuts import render


def easy(request):
    return JsonResponse({'name': 'Bob',
                         'dupa': 'czarna'})
