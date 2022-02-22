import datetime
from django.http import request
from django.shortcuts import render
from .models import *
from datetime import datetime

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method =='POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['tlid'] = member.id
            return render(request, 'TLsec.html', {'member':member})
        else:
            context={'msg':'Invalid uname or password'}
            return render(request,'login.html',context)
            

def devindex(request):
    return render(request,'devindex.html')  
def devdashboard(request):
    return render(request,'devdashboard.html')
def devReportedissues(request):
    return render(request,'devReportedissues.html')
def devreportissue(request):
    return render(request,'devreportissue.html')
def devreportedissue(request):
    return render(request,'devreportedissue.html')
def devsuccess(request):
    return render(request,'devsuccess.html')
def devissues(request):
    return render(request,'devissues.html')
def devsample(request):
    return render(request,'devsample.html')


#*********************praveesh*********************


def Devapplyleav(request):
    return render(request,'Devapplyleav.html')
def Devapplyleav1(request):
    return render(request,'Devapplyleav1.html')
def Devapplyleav2(request):
    return render(request,'Devapplyleav2.html')
def Devleaverequiest(request):
    return render(request,'Devleaverequiest.html')
def Devattendance(request):
    return render(request,'Devattendance.html')
def Tattend(request):
    return render(request,'Tattend.html')
def Devapplyleav3(request):
    return render(request,'Devapplyleav3.html')



#**************************maneesh*********************


def DEVprojects(request):
    return render(request,'DEVprojects.html')
def DEVtable(request):
    return render(request,'DEVtable.html')
def DEVtaskmain(request):
    return render(request,'DEVtaskmain.html')   
def DEVtaskform(request):
    return render(request,'DEVtaskform.html')
def DEVtask(request):
    return render(request,'DEVtask.html')
def DEVsuccess(request):
    return render(request,'DEVsuccess.html')



#**************************Rohit**************************


def TSdashboard(request):
    return render(request,'TSdashboard.html')
def TStask(request):
    return render(request,'TStask.html')
def TSproject(request):
    return render(request,'TSproject.html')
def TSprojectdetails(request):
    return render(request,'TSprojectdetails.html')
def TSassigned(request):
    return render(request,'TSassigned.html')
def TSsubmitted(request):
    return render(request,'TSsubmitted.html')
def TSsucess(request):
    return render(request,'TSsucess.html')


#****************************amal*******************


def tldashboard(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLdashboard.html',{'mem':mem})
    
def tlprojects(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    
    mem = user_registration.objects.filter(id=tlid)
    display = project_taskassign.objects.filter(user_id=tlid)
    return render(request, 'TLprojects.html',{'display':display,'mem':mem})



def tlprojecttasks(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    projectid=request.GET.get('prid')
    mem = user_registration.objects.filter(id=tlid)
    mem1 = test_status.objects.filter(project_id=projectid)
    mem2 = tester_status.objects.filter(tester_id=tlid)
    display = project_taskassign.objects.filter(user_id=tlid).filter(project_id=projectid)
    return render(request, 'TLprojecttasks.html',{'display':display,'mem':mem,'mem1':mem1,'mem2':mem2})

def tltaskstatus(request):
    a=test_status()
    if request.method=="POST":
        a.date=datetime.datetime.now()
        a.workdone = request.POST.get('work_done')
        a.files = request.FILES['attach_file']
        print(a.date)
        a.save()
        return render(request, 'TLprojecttasks.html',{'a':a})
        

    else:
        c = test_status.objects.all()
        return render(request,'TLprojecttasks.html',{'c':c}) 

def tltesterstatus(request):
    
    mem = tester_status.objects.get()
    return render(request, 'TLprojecttasks.html',{'mem':mem})

def tlprojectdetails(request):
    if request.method == 'POST':
        # team = tester_status.objects.get(id=request.POST.get('team_id'))
        team = tester_status()
        team.prostatus = request.POST.get("status")
        team.progress = request.POST.get("progre")
        team.save()
        # base_url = reverse('TLProjectTasks')
        # query_string = urlencode({'prid': team.project_id})
        # url = '{}?{}'.format(base_url, query_string)
        # return redirect(url)
        render(request, 'TLprojecttasks.html')

def tlsplittask(request):
    return render(request, 'TLsplittask.html')
def tlgivetask(request):
    return render(request, 'TLgivetask.html')


#**************************abin*************************


def TLattendance(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    
    return render(request, 'TLattendance.html',{'mem':mem})
        
def TLattendancesort(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.raw('select id,date,status from app_attendance where date between "'+fromdate+'" and "'+todate+'"')
        
    return render(request, 'TLattendance.html',{'mem1':mem1,'mem':mem})
    
def TLreportissues(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLreportissues.html',{'mem':mem})
def TLreportedissue1(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    var=reported_issue.objects.filter(reporter_id=tlid)

    return render(request, 'TLreportedissue1.html',{'mem':mem,'var':var})
def TLreportedissue2(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    rid=request.GET.get('rid')
    var=reported_issue.objects.filter(id=rid)
    mem = user_registration.objects.filter(id=tlid)

    return render(request, 'TLreportedissue2.html',{'mem':mem,'var':var})
def TLreport1(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
        
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLreport1.html',{'mem':mem})
def TLreportsuccess(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    
    mem = user_registration.objects.filter(id=tlid)
    
    if request.method == 'POST':
        
        vars = reported_issue()
        vars.issue=request.POST.get('report')
        vars.reported_date=datetime.now()
        vars.reported_to_id=2
        vars.reporter_id=tlid
        vars.status='pending'
        vars.save()
    return render(request,'TLreportsuccess.html',{'mem':mem})


#***********************bibin*****************************


def TLtasks(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    else:
        tl = "dummy"
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLtasks.html',{'mem':mem})
def TLleave(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLleave.html',{'mem':mem})
    
def TLleavereq(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    else:
        tlid = "dummy"
    mem = user_registration.objects.filter(id=tlid)
    return render(request, 'TLleavereq.html',{'mem':mem,'var':vars})
def tl_leave_form(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
 
    mem = user_registration.objects.filter(id=tlid)

    if request.method == "POST":
        leaves = leave()
        leaves.from_date = request.POST['from']
        leaves.to_date = request.POST['to']
        leaves.leave_status = request.POST['haful']
        leaves.reason = request.POST['reason']
        leaves.user_id = request.POST['tl_id']
        leaves.status = "pending"
        leaves.save()
    return render(request, 'TLleavereq.html',{'mem':mem})
    
    
    
def TLreqedleave(request):
    if request.session.has_key('tlid'):
        tlid = request.session['tlid']
    else:
        tlid = "dummy"
    mem = user_registration.objects.filter(id=tlid)
    var = leave.objects.all()
    return render(request,'TLreqedleave.html', {'var': var, 'mem':mem})
    
def TLgivetasks(request):
    return render(request, 'TLgivetasks.html')
def TLgavetask(request):
    return render(request, 'TLgavetask.html')
def TLsuccess(request):
    return render(request, 'TLsuccess.html')



# project manager module
def promanagerindex(request):
    return render(request, 'promanagerindex.html')

def pmanager_dash(request):
    return render(request, 'pmanager_dash.html')

def projectmanager_projects(request):
    return render(request, 'projectmanager_projects.html')

#nirmal
def projectmanager_assignproject(request):
    return render(request, 'projectmanager_assignproject.html')

#jensin
def projectmanager_createproject(request):
    return render(request, 'projectmanager_createproject.html')

#maneesh
def projectmanager_description(request):
    return render(request, 'projectmanager_description.html')

def projectmanager_table(request):
    return render(request, 'projectmanager_table.html')

def projectmanager_upprojects(request):
    return render(request, 'projectmanager_upprojects.html')

#praveesh

def projectmanager_accepted_projects(request):
    return render(request, 'projectmanager_accepted_projects.html')

def projectmanager_rejected_projects(request):
    return render(request, 'projectmanager_rejected_projects.html')



#bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    return render(request, 'projectman_emp.html')

def projectmanDev(request):
    return render(request, 'projectman_dev.html')

def projectmanDevDashboard(request):
    return render(request, 'projectman_dev_Dashboard.html')

def projectman_developer_attendance(request):
    return render(request, 'projectman_developer_attendance.html')

def projectman_team(request):
    return render(request, 'projectman_team.html')

def projectman_team_profile(request):
    return render(request, 'projectman_team_profile.html')

def projectman_team_attendance(request):
    return render(request,'projectman_team_attendance.html')

def projectMANattendance(request):
    return render(request, 'projectMANattendance.html')

def projectMANreportedissues(request):
    return render(request, 'projectMANreportedissues.html')

def projectMANreportedissue(request):
    return render(request, 'projectMANreportedissue.html')

def projectMANreportissue(request):
    return render(request, 'projectMANreportissue.html')

def projectmanagerreportedissue2(request):
    return render(request, 'projectmanagerreportedissue2.html')

def MANreportsuccess(request):
    return render(request, 'MANreportsuccess.html')

def projectMANleave(request):
    return render(request, 'projectMANleave.html')

def projectMANleavereq(request):
    return render(request, 'projectMANleavereq.html')

def projectMANreqedleave(request):
    return render(request, 'projectMANreqedleave.html') 

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    return render(request,'projectManager_tl.html')

def projectManager_tl_dashboard(request):
    return render(request,'projectManager_tl_dashboard.html')

def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')


def projectmanager_currentproject(request):
    return render(request, 'projectmanager_currentproject.html')

def projectmanager_currentdetail(request):
    return render(request, 'projectmanager_currentdetail.html')

def projectmanager_currentteam(request):
    return render(request, 'projectmanager_currentteam.html')

def projectmanager_completeproject(request):
    return render(request, 'projectmanager_completeproject.html')

def projectmanager_completedetail(request):
    return render(request, 'projectmanager_completedetail.html')

def projectmanager_completeteam(request):
    return render(request, 'projectmanager_completeteam.html')

def projectmanager_teaminvolved(request):
    return render(request, 'projectmanager_teaminvolved.html')

def projectmanager_devteam(request):
    return render(request, 'projectmanager_devteam.html')

def projectmanager_currenttl(request):
    return render(request, 'projectmanager_currenttl.html')

def projectmanager_completetl(request):
    return render(request, 'projectmanager_completetl.html')

def projectmanager_tlreported(request):
    return render(request, 'projectmanager_tlreported.html')


def branch(request):
    a=branch_registration()
    
    if request.method=="POST":
        a.status = request.FILES['photo']
        
        a.save()
        return render(request,'branch.html',{'a':a})
        

    else:
        return render(request,'branch.html')