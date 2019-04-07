import base64

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect, csrf_exempt


from api.dbAccess import addTask, getTaskUsersByUserId, get_all_tasks_by_id, createChallange


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
    user_id = 1
    list_task = get_all_tasks_by_id(user_id)

    for ele in list_task:

        print(ele.name)
    return render(request, 'api/task.html', {'tasks': list_task})


def daily(request):
    return render(request, 'api/daily.html')


def account(request):
    return render(request, 'api/account.html')


def challenge_create(request):
    if request.method == 'POST':
        # user_id = 1
        # task_name = request.POST.get('task_name')
        # task_description = request.POST.get('task_description')
        # task_deadline = request.POST.get('task_deadline')
        chanalnge_name=request.POST.get('challenge_name')
        chanalnge_description = request.POST.get('challenge_description')

        # createChallange(chanalnge_name,chanalnge_description,)
        print("HIBOB")

    return render(request, 'api/create_chalange/chalnge_create.html')


def home(request):
    return render(request, 'api/task.html')


def new_task(request):
    if request.method == 'POST':
        user_id = 1
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_deadline = request.POST.get('task_deadline')
        addTask(user_id, task_name, task_description, 1, '2017-11-11', task_deadline, 1, True, ['Gym', 'Dumbbell'])
        return render(request, 'api/task.html')
    return render(request, 'api/new_task.html')


@csrf_exempt
def cameramodule(request):
    print('post przed')
    if request.method == 'POST':
        upload_file=request.body
        image_64_decode = base64.standard_b64decode(upload_file)
        image_result = open('test.png', 'wb')
        image_result.write(image_64_decode)
        image_result.close()

    return render(request, 'api/cameramodule.html')
