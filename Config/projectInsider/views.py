# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
# Create your views here.
 

def inicio(request):

	context = {}

	return render(request, "home.html",context )