from django.http import HttpResponse
def about(request):
    return HttpResponse("This is our about page.")
