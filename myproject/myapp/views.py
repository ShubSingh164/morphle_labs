from django.http import HttpResponse

def htop(request):
    return HttpResponse("This is the htop endpoint!")