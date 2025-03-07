from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from ots1.models import*
import random 

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res

def candidateRegistration(request):
    if request.method=='POST':
        username=request.POST['username']
        if(len(Candidate.objects.filter(username=username))): 
            userStatus=1
        else:
            candidate=Candidate()
            candidate.username=username
            candidate.password=request.POST['password']
            candidate.name=request.POST['name']
            candidate.save()
            userStatus=2
    else:
        userStatus=3
    context={
            'userStatus':userStatus
        }
    res=render(request,'registration.html',context)
    return res

def loginView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError="invalid username or password"
            res=render(request,'loginview.html',{'loginError':loginError})
             
        else:
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
            res=HttpResponseRedirect("home")
    else:
       res=render(request,'loginview.html')
    return res

def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        res=render(request,'home.html')
    return res

def starttest(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    #fetch question from database table
    n=int(request.GET['n'])
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    questions_list=question_pool[:n]
    context={'questions':questions_list}
    res=render(request,'test_paper.html',context)
    return res 

def calculateTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    total_attmpt=0
    total_right=0
    total_wrong=0
    qid_list=[]
    for k in request.POST:
        if k.startswith('qno'):
            qid_list.append(int(request.POST[k]))
    for n in qid_list:
        question=Question.objects.get(qid=n)
        try:
            if question.ans==request.POST['q'+str(n)]:
                total_right+=1
            else:
                total_wrong+=1
            total_attmpt+=1
        except:
            pass
    points=(len(qid_list)-total_wrong)*10
    # how to store points in result in result table
    result=Result()
    result.username=Candidate.objects.get(username=request.session['username'])
    result.attempt=total_attmpt
    result.right=total_right
    result.wrong=total_wrong
    result.points=points
    result.save()
    #update candidate table
    candidate=Candidate.objects.get(username=request.session['username'])
    candidate.test_attempted+=1
    candidate.points=(candidate.points*(candidate.test_attempted-1)+points)/candidate.test_attempted
    candidate.save()
    return HttpResponseRedirect('result')


def testResultHistory(request):
   if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
   candidate=Candidate.objects.filter(username=request.session['username'])
   results=Result.objects.filter(username_id=candidate[0].username)
   context={'candidate':candidate,'results':results}
   res=render(request,'candidate_hitry.html',context)
   return res



def showTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    #fetch result from result table
    result=Result.objects.filter(resultid=Result.objects.latest('resultid').resultid,username_id=request.session['username'])
    context={'result':result}
    res=render(request,'show_test.html',context)
    return res

def logoutViews(request):
    if 'name' in request.session.keys():
        del request.session['username']
        del request.session['name']
    return HttpResponseRedirect("login")
