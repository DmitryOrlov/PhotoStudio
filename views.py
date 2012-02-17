from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home_page.html', {'pagetitle' : 'Welcome to Virtual Photo Studio'})
