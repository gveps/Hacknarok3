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
        print(task_name)
        print(task_description)
        print(task_deadline)


        addTask(user_id, task_name, task_description, 1, '2017-11-11', task_deadline, 1, True, ['Gym', 'Dumbbell'])
        return render(request, 'api/task.html')
    return render(request, 'api/new_task.html')


@csrf_exempt
def cameramodule(request):
    print('post przed')
    if request.method == 'POST':
        print("post")
        upload_file = request.POST
        cos = request.POST.get('data', 'nie ma')
        print(cos)
        image64 = ""
        print(type(upload_file))
        print(upload_file)
        for elem in upload_file:
            print(elem)
            if "base64" in elem:
                image64 = elem
        # image64 = ''.join(image64.split())
        # image64 = image64[7:]
        image64=str(upload_file)[3:]
        print(len(image64))
        file = open("testfile.txt", "w")
        file.write("data:image/png;" + image64)

        # print(image64)
        # encoded = base64.b64encode(("data:image/png;" + image64).encode('ansi'))
        # image64 = encoded
        # print(encoded)
        # image_64_decode = base64.decodebytes(encoded)
        print(len(image64))
        # image64="data:image/png;" + image64
        for x in range(len(image64)%4-2):
            image64=image64+'='
        print(len(image64))
        image_64_decode = base64.standard_b64decode(image64)
        print(len(image64))
        image_result = open('test.png', 'wb')
        image_result.write(image_64_decode)
        image_result.close()
        # print(upload_file)
        # print(upload_file.size)
        # fs = FileSystemStorage()
        # fs.save(upload_file.name, upload_file.size)
    return render(request, 'api/cameramodule.html')
