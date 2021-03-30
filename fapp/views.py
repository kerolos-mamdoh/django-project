import itertools
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import addproject, comment_project, donnate ,featureproject
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .form import myForm, myModelForm, myForm2
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def addproject_form(request):
    return render(request,'addproject.html',{})

def addproject_database(request):
    obj=addproject()
    id=request.user.id
    tittle= request.POST['titles']
    details = request.POST['det']
    cateogry = request.POST['cat']
    target = request.POST['target']
    print('**************************')
    imgs=request.FILES.get('im')
    print(imgs)
    sdate = request.POST['sdate']
    enddate = request.POST['enddate']
    tag=request.POST['tag']
    obj.tittle=tittle
    obj.details=details
    obj.category=cateogry
    obj.total_target=target
    obj.uploadimg=imgs
    obj.startdate=sdate
    obj.edndate=enddate
    obj.id_user=id
    obj.tag=tag
    obj.save()
    return redirect('homepage')

def adminproject(request,id):
    obj=featureproject()
    obj.id_project=id
    obj.save()
    return redirect('homepage')


def addproject_table(request):
    feature=featureproject.objects.all()
    featurefromaprojects={}
    featurearr=[]
    for i in feature:
        featurearr.append(i.id_project)
    #for x in featurearr:
        #featurefromaprojects[x]=addproject.objects.get(id=x)
    #print("mmmmmmmmmmmmmmmmmm")
    #print(featurefromaprojects)
    i=0
    list2=[]
    amount_list=[]
    order_amount=[]
    projectdonnates={}
    obj2 = addproject.objects.all()
    list=addproject.objects.order_by('-startdate')[:5]
    #while(i < 5):
     #   list2.append(list[i])
      #  i=i+1
    donnateobj = donnate.objects.all()
    arr=[]
    for i in donnateobj:
        if i.project_id not in arr:
            arr.append(i.project_id)


    amount=0
    dic={}
    for i in arr:
        x=donnate.objects.all().filter(project_id=i)
        for j in x:
            amount=amount+j.amount
        dic[i]=amount
        amount=0

    sort = sorted(dic.items(), key=lambda kv: kv[1],reverse=True)
    sorteddonnates = dict(sort)
    sdonnate= dict(itertools.islice(sorteddonnates.items(), 5))
    ldonnate={}
    for d in sdonnate:
        b=addproject.objects.filter(id=d)
        for i in b:
            ldonnate[i.tittle]=sdonnate[d]
        #ldonnate[b.tittle]=sdonnate[d]
    print('sdonnate')
    print(sdonnate)


    '''
    maxid=donnate.objects.order_by('-project_id')
    max=maxid[0].project_id
    j=0
    n = 0
    while(n < 10):
        while(j<len(donnateobj)):
            if (5 == donnateobj.get.all().project_id[j]):
                amount=amount+donnateobj.amount
                id=n
            j=j+1
        if (amount and id):
            projectdonnates[id].append(amount)
        n=n+1
        amount=0
    sorted= sorted(projectdonnates.items(), key=lambda kv: kv[1])
    sorteddonnates=dict(sorted)
    sortedprojectsdonnates={}
    while (i<5):
        for x in sorteddonnates:
            sortedprojectsdonnates[x].append(sorteddonnates[x])
    lastdic={}
    for c in sortedprojectsdonnates:
        ob=addproject.objects.filter(id=int(c))
        lastdic[ob.tittle].append(sortedprojectsdonnates[c]) '''
    print('ldonnate')
    print(ldonnate)
    return render(request, 'home.html', {'data': obj2,'list':list,'dic':ldonnate,'featurefromaprojects':featurefromaprojects})


def register_form(request):
    form = myForm()
    return HttpResponse("khkkhk,")

def registerAuth(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            uname = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']
            user = User.objects.create_user(username=uname,last_name=lname,first_name=fname,password=pass1,email='email')
            user.save()
            '''
            send_mail(
                'you are registerd',
                'Here is the message.',
                'keromamdouh98@gmail.com',
                ['keromamdouh98@gmail.com'],
                fail_silently=False,
                
            )'''

            return redirect('homepage')
    else:
       form = myForm()
    return render(request, 'adduser.html', {'form': form})
def home_view(request):
    return render(request, 'home.html')

def loginAuth(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = myModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            uname = form.cleaned_data['username']
            pass1 = form.cleaned_data['password']
            # redirect to a new URL:Authinticate
            user = authenticate(username=uname,password=pass1)
            if user is not None:
                login(request, user)
                return redirect('homepage')
                #logout(request)
                #return HttpResponse('/login found/')
            else:
                return HttpResponse('/not found/')
    else:
        form = myModelForm()
        return render (request, 'login.html', {'form': form})

def profile_user(request):
    projects=addproject.objects.all().filter(id_user=request.user.id)
    id=request.user.id
    return render(request,'profile.html',{'data':projects,'id':id})


def edit_form(request):
    id = request.user.id
    print('xxxxxxxxxxxxx')
    print(id)
    return render(request,'edit_form.html',{'id':id})

def search(request):
    s=request.POST['search']
    ob=addproject.objects.all().filter(tittle__icontains=s)
    return render(request,'search_home.html',{'data':ob})

def searchtags(request):
    s=request.POST['tag']
    ob=addproject.objects.all().filter(tag__icontains=s)
    return render(request,'search_home.html',{'data':ob})

def editprofileuser(request,id):
    obj=User.objects.get(id=id)
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    pass1 = request.POST['psw']
    obj.username=uname
    obj.last_name=lname
    obj.first_name=fname
    obj.password=pass1
    obj.save()
    return redirect('signup')
def comment(request,id):
    obj=comment_project.objects.all().filter(project_id=id)
    return render(request,'comment.html',{'data':obj,'id':id})
def add_comment(request,id):
    obj=comment_project()
    comment =request.POST['com']
    obj.comment=comment
    obj.project_id=id
    obj.save()
    return redirect('homepage')

def donate_form(request,id):
    return render(request,'donnate.html',{'id':id})
def add_donnate(request,id):
    name=request.POST['name']
    amount=request.POST['amount']
    obj=donnate()
    obj.name=name
    obj.amount=amount
    obj.project_id=id
    obj.save()
    return redirect('homepage')

def donateprojects(request,id):
    donntes=donnate.objects.all().filter(project_id=id)
    total=0
    for i in donntes:
        total=total+i.amount
    return render(request,'donnate_projects.html',{'id':id,'data':donntes,'total':total})

def remove_projects(request,id,totaldonnates):
    objproject=addproject.objects.filter(id=id)
    objcomment = comment_project.objects.all().filter(project_id=id)
    objdonnate = donnate.objects.all().filter(project_id=id)
    objproject.delete()
    objcomment.delete()
    objdonnate.delete()
    return redirect('profile')

def deleteprofile(request):
    id = request.user.id
    id_project=[]
    obuser=User.objects.get(id=id)
    obproject=addproject.objects.all().filter(id_user=id)
    for x in obproject:
        id_project.append(x.id)
    for i in id_project:
        ob_comment=comment_project.objects.all().filter(project_id=i)
        ob_comment.delete()
        ob_donnates=donnate.objects.all().filter(project_id=i)
        ob_donnates.delete()
    obuser.delete()
    obproject.delete()
    return HttpResponse("account deleted")
