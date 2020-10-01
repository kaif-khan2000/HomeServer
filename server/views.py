from django.shortcuts import render,HttpResponse,redirect
from .models import Directory,File
# Create your views here.
def home(request):
    root = Directory.objects.get(name='root',parent=None)
    
    dirs = Directory.objects.filter(parent=root)
    files = File.objects.filter(parent=root)
    return render(request,'server/home.html',{'directories':dirs,'files':files})

def directory(request,slug):
    main = Directory.objects.get(id=int(slug))
    directories = Directory.objects.filter(parent = main)
    files = File.objects.filter(parent=main)
    return render(request,'server/directory.html',{'main':main,'directories':directories,'files':files})

def addFolder(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        parentId = int(request.GET.get('parentId'))
        if request.is_ajax:
            main = Directory.objects.get(id=parentId)
            if main.name == 'root' and main.path == '/':
                Directory.objects.create(name=name,parent=main)
            else:
                path = main.path+main.name+'/'
                Directory.objects.create(name=name,parent=main,path=path)
        return HttpResponse()

def addFile(request):
    if request.method == 'POST':
        file1 = request.FILES['file']
        parentId = request.POST.get('parent')
        name = file1.name
        size = file1.size
        file_type = file1.content_type
        size = str(round(int(size)/1000000,2))+"MB"
        parent = Directory.objects.get(id=parentId)
        File.objects.create(
            name = name,
            typeOfFile = file_type,
            parent = parent,
            size = size,
            actual_file = file1
        )

        return redirect("/directory/"+str(parentId))

def renameFile(request):
    if request.method == 'GET':
        newName = request.GET.get('name')
        extension = fileExtension(newName)
        id = request.GET.get('id')
        if request.is_ajax:
            myfile = File.objects.get(id = id)
            oldExtension = fileExtension(myfile.name)
            if oldExtension != extension:
                newName += '.' + oldExtension
            myfile.name = newName
            myfile.save()
    return HttpResponse()

def fileExtension(name):
    extension = ''
    for i in range(len(name)-1,-1,-1):
        if name[i] == '.': break
        extension += name[i]
    else:
        extension = ''
    
    extension = extension[::-1]

    return extension

def deleteFile(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if request.is_ajax:
            File.objects.get(id=id).delete()
    return HttpResponse()

def deleteFolder(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if request.is_ajax:
            Directory.objects.get(id=id).delete()
    return HttpResponse()

def videos(request):
    videos = File.objects.filter(typeOfFile__icontains = 'video')
    return render(request,'specific/videos.html',{'videos':videos})

def music(request):
    music = File.objects.filter(typeOfFile__icontains = 'audio')
    return render(request,'specific/music.html',{'music':music})

def search(request):
    if request.method == "GET":
        query = request.GET.get('search')

        folders = Directory.objects.filter(name__icontains = query)
        files = File.objects.filter(name__icontains = query)

        return render(request,'server/directory.html',{'directories':folders,'files':files})
