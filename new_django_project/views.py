from django.shortcuts import HttpResponse

def simple(request):
    return HttpResponse("123")