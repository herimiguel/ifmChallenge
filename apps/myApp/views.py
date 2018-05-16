# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import os

# Create your views here.
def index(request):
    directory = "../ifmChallenge/apps/myApp/test_labels_renamed"
    list = os.listdir(directory)
    pairs = []
    for file in list:
        location = os.path.join(directory, file)
        size = os.path.getsize(location)
        pairs.append((size, file))
    pairs.sort(key=lambda s: s[0])
    context = {
    'pairs' : pairs    
    }
    #     print(pair)
    return render(request, 'myApp/index.html', context)

