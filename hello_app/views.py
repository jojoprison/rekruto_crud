from django.shortcuts import render


def hello_friend(request):
    if request.method == "GET":
        # stub url parameters, if we dont have them in url or get empty
        name = request.GET.get('name', None)
        message = request.GET.get('message', None)

        content = {
            'name': name,
            'message': message
        }

        return render(request, 'index.html', content)


def error_404(request, exception):
    return render(request, '404.html')
