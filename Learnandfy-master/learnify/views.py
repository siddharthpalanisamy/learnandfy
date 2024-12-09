from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login,logout
from django.core.files import File

# Create your views here.
def home(request):
    return render(request,"Learnify/Home.html")

def hackathon(request):
    return render(request,"Learnify/Hackathon.html")

def questions(request):
    
    if request.method=="POST":
        title=request.POST['title']
        author=request.user
        description=request.POST['body']
        tag=request.POST['targetUrl']

        instance=Post.objects.create(title=title,author=author,description=description,urldata=tag)
        instance.save()
        return render(request,"Learnify/CreatePost.html")
    
    return render(request,"Learnify/CreatePost.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"Learnify/Log in.html")
        
    return render(request,"Learnify/Log in.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.filter(username=username)

        if len(user):
            return HttpResponse("Username already exist try another username")
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return render(request,"Learnify/Personal-info.html")
    
    return render(request,"Learnify/Signup.html")

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    
    profile_data = Profile.objects.filter(sno=request.user.id).first()
    
    if not profile_data:
        return redirect('profileinfo')
    
    student = Student.objects.filter(user=profile_data).first()
    professional = Professional.objects.filter(user=profile_data).first()
    user=User.objects.get(id=request.user.id)
    email=user.email
    project=Project.objects.filter(leader=request.user)

    context = {
        'profile': profile_data,
        'student': student,
        'professional': professional,
        'email': email,
        'projects':project  
    }
    return render(request, "Learnify/Profile-Show.html", context)


def discussion(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,"Learnify/Discussions.html",context)

def post(request,sno):
    post = Post.objects.filter(sno=sno).first()
    comments = Comment.objects.filter(post_sno=sno)
    count = len(comments)
    profile=Profile.objects.all()
    context = {
        'post': post,
        'profile':profile,
        'comments': comments,
        'count': count
    }

    if request.method=="POST":
        comment=request.POST["body"]
        user=request.user

        instance=Comment.objects.create(comment=comment,post_sno=post,commenter=user)
        instance.save()
        return redirect('discussion')
    return render(request, 'Learnify/Post.html', context)
   
def signout(request):
    logout(request)
    return render(request,"Learnify/Home.html")

def serach(request):
    if request.method == "GET":
        query=request.GET['query']
        allpostAuthor=Post.objects.filter(author__username__icontains=query)
        allpostTitle=Post.objects.filter(title__icontains=query)
        post=allpostTitle.union(allpostAuthor)
        context={
            'posts':post,
        }
    return render(request,'Learnify/Discussions.html',context)

def profileinfo(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        description=request.POST['description']
        isstudent=request.POST['exist']
        phone=request.POST['phone']
        link=request.POST['link']
        sno=request.user

        if isstudent == "student":
            isstudent=1
            instance=Profile(sno=request.user,fname=fname,lname=lname,description=description,phoneno=phone,status=isstudent,link=link)
            instance.save()
            return redirect('student_info')
        
        else:
            isstudent=2
            instance=Profile(sno=request.user,fname=fname,lname=lname,description=description,phoneno=phone,status=isstudent,link=link)
            instance.save()
            return redirect('professional_info')
    return render(request,"Learnify/Personal-Info.html")

def student_info(request):
    if request.method == "POST":
        institution=request.POST['Institution']
        fieldofinterest=request.POST['fieldofinterest']
        degree=request.POST['degree']
        year=request.POST['year']
        profile=Profile.objects.filter(sno=request.user.id).first()

        instance=Student(user=profile,institution=institution,fieldofinterest=fieldofinterest,degree=degree,currentyear=year)
        instance.save()
        return redirect('signin')
    
    return render(request,'Learnify/Student-info.html')

def professional_info(request):
    if request.method == "POST":
        profile=Profile.objects.filter(sno=request.user.id).first()
        organization=request.POST['organization']
        year=request.POST['year']
        designation=request.POST['designation']

        instance=Professional(user=profile,organization=organization,designation=designation,experience_year=year)
        instance.save()
        return redirect('signin')

    return render(request,'Learnify/Professional-info.html')

def project(request):
    return render(request,"Learnify/Post project.html")

def projectview(request,sno):
    project=Project.objects.get(sno=sno)
    folder=Folder.objects.filter(projectno=project)
    foldername=folder.values_list('foldername',flat=True).distinct()

    context={
        'project':project,
        'folder':folder,
        'foldername':foldername
    }
    return render(request,"Learnify/View project.html",context)

def createproject(request):
    if request.method == "POST":
        title=request.POST.get('title')
        body=request.POST.get('body')
        leader=request.user
        project=Project.objects.create(projectname=title,description=body,leader=leader)
        project.save()
        return createfolder(request,project)
    return render(request,"Learnify/Post project.html")

def createfolder(request, project):
    if request.method == "POST":
        foldername = request.POST['foldername']
        files = request.FILES.getlist('fileInput')

        for file in files:
            instance = Folder.objects.create(projectno=project, foldername=foldername, file=file)

        return redirect('project')
    return render(request, "Learnify/Post project.html")


from django.core.files import File

def viewfile(request,sno,foldersno):
    project = Project.objects.get(sno=sno)
    folder = Folder.objects.filter(projectno=project,sno=foldersno).first()
    filedata = ""

    with open(f'static/images/{folder.file}', 'r', encoding="utf-8") as f:
        filedata = f.read()

    mutual = "0"
    if project.leader == request.user:
        mutual = '1'
    else:
        collab = Collaboration.objects.filter(projectno=sno, friend=request.user,status=True)
        if collab.exists():
            mutual = '1'

    context = {
        'filedata': filedata,
        'project': project,
        'mutual': mutual,
        'folder': folder
    }

    if request.method == "POST":
        file_content = request.POST.get('file')
        filepath = f'static/images/{folder.file}'
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(file_content)
        folder.file = folder.file
        folder.save()
        return render(request, "Learnify/Post project.html")

    return render(request, "Learnify/View file.html", context)

def projectlist(request):
    project=Project.objects.all()
    context={
        'projects':project,
    }
    return render(request,"Learnify/Project-list.html",context)

def othersprofile(request, username):
    try:
        user=User.objects.get(username=username)
        profile = Profile.objects.get(sno=user)
        student = Student.objects.filter(user=profile).first()
        professional = Professional.objects.filter(user=profile).first()
        email = user.email
        projects = Project.objects.filter(leader=user)
    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)

    return render(request, 'Learnify/Profile-Show.html', {'profile': profile, 'student': student, 'professional': professional, 'email': email, 'projects': projects,'userid':user.id})

def collab(request,id):
    if request.method=="POST":
        user=User.objects.get(id=id)
        project=request.POST["project"]
        print(project)
        projcollab=Project.objects.get(sno=project)
        coll=Collaboration.objects.create(projectno=projcollab,friend=user,status=False)
        coll.save()
    return redirect('home')