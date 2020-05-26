from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return render(request, 'index.html', context={'title': 'FooBar'})

@csrf_exempt
def get_result(request):
    """View function for get result post call"""
    result = {}
    input_number = None
    if request.method == "POST":
        data = request.POST.copy()
        input_number = data.get('number', None)
    if input_number:
        if int(input_number) % 3 == 0 and int(input_number) % 5 == 0:
            result = {'data': ['foo', 'bar']}
        elif int(input_number) % 3 == 0:
            result = {'data': ['foo']}
        elif int(input_number) % 5 == 0:
            result = {'data': ['bar']}
        else:
            result = {'data': None}

    return JsonResponse(result)

