from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def easy(request):

    return render(request, 'api/base.html', {'cos': 'dupa'})


def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        print(upload_file.name)
        print(upload_file.size)
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file.size)
    return render(request, 'api/upload.html')


def task(request):
    return render(request, 'api/task.html')


def daily(request):
    return render(request, 'api/daily.html')


def account(request):
    return render(request, 'api/account.html')


def competition(request):
    return render(request, 'api/competition.html')


def home(request):
    return render(request, 'api/task.html')


def new_task(request):
    if request.method == 'POST':
        print(request.POST.get('task_name'))
        print(request.POST.get('task_description'))
        print(request.POST.get('task_deadline'))
        return render(request, 'api/task.html')
    return render(request, 'api/new_task.html')


@csrf_exempt
def new(request):
    print('post przed')
    if request.method == 'POST':
        print("post")
        upload_file = request.POST
        for elem in upload_file:
            print(elem)
        # print(upload_file.size)
        # fs = FileSystemStorage()
        # fs.save(upload_file.name, upload_file.size)
    return render(request, 'api/cameramodule.html')



