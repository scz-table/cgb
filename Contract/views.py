from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render
from .models import *
# from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):

    return render(request, 'Contract/Contract.html')