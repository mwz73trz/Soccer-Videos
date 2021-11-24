from django.shortcuts import render
from django.http import JsonResponse, response
import requests

def get_games(request):
    response = requests.get(f"https://www.scorebat.com/video-api/v3/").json()
    return JsonResponse(response, safe=False)
