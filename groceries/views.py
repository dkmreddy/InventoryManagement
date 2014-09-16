# Create your views here.
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('groceries/Home.html',{})