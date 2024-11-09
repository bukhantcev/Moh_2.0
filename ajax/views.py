
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def FirstAjax(request):
    text = request.GET['text']
    return HttpResponse('All Done!')

# Create your views here.
