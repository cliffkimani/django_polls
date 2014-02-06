from django.http import HttpResponseRedirect

def redirect2polls(request):
    return HttpResponseRedirect("/polls/")