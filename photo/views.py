# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def uploadphotos(request):
    return render_to_response('upload_page.html', {'pagetitle' : 'Upload Photos'})

def filesreceiver(request):
    pass
