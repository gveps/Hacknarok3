import decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect
import base64

from django.http import JsonResponse, HttpResponseRedirect
import base64

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from api.dbAccess import addTask, getTaskUsersByUserId, get_all_tasks_by_id, createChallange, addUserToTask, \
    getAllTasksFromChallangeId

from api.dbAccess import addTask, getTaskUsersByUserId, get_all_tasks_by_id, createChallange, addUserToTask
from api.dbAccess import addTask, getTaskUsersByUserId, get_all_tasks_by_id, createChallange, getTagsByTaskId, \
    validateTaskForUser
from api.tagVeryfication import tagVerify
from img_recg.detect import recognize


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
        chanalnge_name = request.POST.get('challenge_name')
        chanalnge_description = request.POST.get('challenge_description')
        price = request.POST.get("task_price")
        status = True
        if price == "" or price is None:
            price_flo = 0.0
        else:
            price_flo = float(price)
        price_flo = decimal.Decimal(round(price_flo, 2))
        challenge = createChallange(chanalnge_name, chanalnge_description, price_flo, status)
        tasks = getAllTasksFromChallangeId(challenge.id)
        return redirect('../challenge_mod', {'challenge': challenge, 'tasks': tasks})
    return render(request, 'api/create_chalange/chalnge_create.html')


def new_task_for_chalange(request):
    if request.method == 'POST':
        challenge = request.GET.get("challenge")

        #  TODO Make adding chalange here

        return redirect('../challenge_mod', {'chalange': challenge})
    return render(request, 'api/new_chalenge_task.html')


def home(request):
    return render(request, 'api/task.html')


@csrf_exempt
def challenge_mod(request):
    if request.method == 'POST':
        challenge = request.POST.get('challenge')
        task=request.POST.get('taks')
        return redirect('../task_for_challenge', {'chalange': challenge})
    return render(request, 'api/challenge_mod.html')


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

        user_id = 1
        list_task = get_all_tasks_by_id(user_id)
        return render(request, 'api/task.html', {'tasks': list_task})
    return render(request, 'api/new_task.html')


@csrf_exempt
def cameramodule(request):
    if request.method == 'POST':
        upload_file=request.body
        image_64_decode = base64.standard_b64decode(upload_file)
        image_result = open('test.png', 'wb')
        image_result.write(image_64_decode)
        image_result.close()

        actual_tags = recognize('test.png')
        # TODO: get user_id and task_id from post
        task_id = 8
        user_id = 1
        expected_tags = getTagsByTaskId(task_id)

        print(actual_tags)

        if tagVerify(expected_tags, actual_tags):
            print("zaliczone")
            validateTaskForUser(user_id, task_id)
        else:
            print("nie zaliczone")

    return render(request, 'api/cameramodule.html')
