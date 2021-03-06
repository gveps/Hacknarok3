from django.utils import timezone

from api.models import Task, Tag, TagTask, MyUser, Challange, TaskChallange, TaskUser, CategoryTag


# // save task in database return id
def saveTask(name, description, total_times, startDate, endDate, type, status):
    task = Task(name=name, description=description, total_times=total_times, startDate=startDate, endDate=endDate, type=type, status=status)
    task.save()
    return task


# save tag in db return id
def saveTag(name):
    try:
        tag = Tag.objects.get(name=name)
    except Tag.DoesNotExist:
        tag = Tag(name=name)
        tag.save()
    return tag


# save TaskTag in db
def saveTagTask(tag, task):
    tag_task = TagTask(id_tag=tag, id_task=task)
    tag_task.save()


def addTask(name, description, total_times, startDate, endDate, type, status, tags):
    task = saveTask(name=name, description=description, total_times=total_times, startDate=startDate, endDate=endDate, type=type, status=status)
    for tag in tags:
        saveTagTask(tag=saveTag(tag), task=task)
    return task


def addUserToTask(task_id, user_id):
    taskUser = TaskUser(id_user_id=user_id, id_task_id=task_id, counter=0, last_time="2017-11-11")
    taskUser.save()
    return taskUser


def getTagsByTaskName(taskName):
    task = Task.objects.get(name=taskName)
    return TagTask.objects.filter(id_task=task)


def getTagsByTaskId(task_id):
    task = Task.objects.get(id=task_id)
    tags = TagTask.objects.filter(id_task=task)
    tagsstr = []
    for tag in tags:
        tagsstr.append(tag.id_tag.name)
    return tagsstr

def addUser(login, password, name, surname):
    user = MyUser(login=login, name=name, password=password, surname=surname, photo="")
    user.save()
    return user


def createChallange(name, description, bet_value, status):
    challange = Challange(name=name, description=description, bet_value=bet_value, status=status)
    challange.save()
    return challange


def addTaskToChallange(task_id, challange_id):
    taskChallage = TaskChallange(id_challange_id=challange_id, id_task_id=task_id)
    taskChallage.save()
    return taskChallage


def addUserToChallange(user_id, challange_id):
    taskChallanges = TaskChallange.objects.filter(id_challange_id=challange_id)
    for task in taskChallanges:
        taskUser = TaskUser(id_user_id=user_id, id_task=task.id_task, counter=0, last_time="2017-11-26")
        taskUser.save()


def getTaskUsersByUserId(user_id):
    return TaskUser.objects.filter(id_user_id=user_id)


def get_all_tasks_by_id(user_id):
    task_users = getTaskUsersByUserId(user_id)
    tasks = []
    for task_user in task_users:
        tasks.append(Task.objects.get(id=task_user.id_task_id))
    return tasks


def getAllTasksFromChallangeId(challange_id):
    taskChallanges = TaskChallange.objects.filter(id_challange_id=challange_id)
    tasks = []
    for taskchal in taskChallanges:
        tasks.append(taskchal.id_task)
    return tasks


def getChallangeFromUserId(user_id):
    all_tasks = get_all_tasks_by_id(user_id)
    challanges = []
    for task in all_tasks:
        task_challanges = TaskChallange.objects.filter(id_task=task)
        for task_chal in task_challanges:
            challanges.append(task_chal.id_challange)
    challanges = list(dict.fromkeys(challanges))
    return challanges


def addCategoryTag(name, tags):
    for tagStr in tags:
        tag = Tag(name=tagStr)
        tag.save()
        categoryTag = CategoryTag(id_tag=tag, name=name)
        categoryTag.save()

def getTagsFromCategory(category_name):
    tags = CategoryTag.objects.filter(name=category_name)
    tags_str = []
    for tag in tags:
        tags_str.append(tag.id_tag)
    return tags_str


def addTaskWithCategory(name, description, total_times, startDate, endDate, type, status, category_name):
    task = saveTask(name=name, description=description, total_times=total_times, startDate=startDate, endDate=endDate, type=type, status=status)
    for tag in getTagsFromCategory(category_name):
        saveTagTask(tag=tag, task=task)
    return task


def getAllCategories():
    categoryTag = CategoryTag.objects.all()
    categories = []
    for catTag in categoryTag:
        categories.append(catTag.name)
    categories = list(dict.fromkeys(categories))
    return categories


def validateTaskForUser(user_id, task_id):
    userTask = TaskUser.objects.get(id_user_id=user_id, id_task_id=task_id)
    userTask.counter = userTask.counter + 1
    userTask.last_time = timezone.now()
    userTask.save()
