import decimal

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from api.dbAccess import addTask, getTaskUsersByUserId, get_all_tasks_by_id, createChallange, addUserToTask


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


@csrf_exempt
def challenge_create(request):
    if request.method == 'POST':
        chanalnge_name = request.POST.get('challenge_name')
        chanalnge_description = request.POST.get('challenge_description')
        price = request.POST.get("task_price")
        status = True
        if price == "":
            price_flo = 0.0
        else:

            price_flo = float(price)
        price_flo = decimal.Decimal(round(price_flo, 2))
        createChallange(chanalnge_name, chanalnge_description, price_flo, status)

    return render(request, 'api/create_chalange/chalnge_create.html')


def home(request):
    return render(request, 'api/task.html')


@csrf_exempt
def new_task(request):
    if request.method == 'POST':
        user_id = 1
        category = 'dupa'

        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_deadline = request.POST.get('task_deadline')
        print(task_name)
        print(task_description)
        print(task_deadline)

        taskk = addTask(task_name, task_description, 1, '2017-11-11', task_deadline, 1, True, category)
        addUserToTask(taskk.id, user_id)
        addTask(user_id, task_name, task_description, 1, '2017-11-11', task_deadline, 1, True, ['Gym', 'Dumbbell'])
        user_id = 1
        list_task = get_all_tasks_by_id(user_id)
        return render(request, 'api/task.html', {'tasks': list_task})
    return render(request, 'api/new_task.html')


@csrf_exempt
def cameramodule(request):
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
