from django.http import JsonResponse

def student(request):
    if request.method == 'GET':
        student = {'id':1, 'name': 'Jose'}
        return JsonResponse(student)