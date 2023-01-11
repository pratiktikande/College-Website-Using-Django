from django.shortcuts import render 
from .models import blogdetails,maingallery,newspaper,staffdetails,company,placementss,placementdetails,projectss,projectsdetails,tripss,tripsdetails,staffs,patent,alumini,calender,cutoff,syllabus,question,firstyearquestion,placementstestquestion,conference,course,publication,chart,messagebox,admissionform,Apply
def index(request):
    tripsdetail=tripsdetails.objects.all()
    # courses=course.objects.all()
    projectsdetail=projectsdetails.objects.all()
    number1=len(tripsdetail)
    number2=len(projectsdetail)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 
    project=projectss.objects.all()
    numberofprojects=len(project)
    trip=tripss.objects.all()
    numberoftrips=len(trip)
    placements=placementdetails.objects.all()
    place=company.objects.all()
    numberofplaced=len(place)
    messages=messagebox.objects.all()
    params={'tripsdetail':tripsdetail,'projectdetail':projectsdetail,'number1':number1,'number2':number2,'allsys':allsys,'number':numberofsyl,'project':project,'number3':numberofprojects,'trips':trip,'number4':numberoftrips,'placement':placements,'number5':numberofplaced,'place':place,'message':messages}
    return render( request,'index.html',params)
def about(response):
    return render(response,'aboutus.html')
def bachlers(response):
    return render(response,'bachlers.html')
def publicat(response):
    publications=publication.objects.all()
    numberofpublications=len(publications)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys,'publication':publications,'number':numberofpublications}
    return render(response,'publication.html',params)
def patents(response):
    patents=patent.objects.all()
    numberofpatent=len(patents)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    params={'patents':patents,'number':numberofpatent,'allsys':allsys}
    return render(response, 'patent.html',params)
def calenders(response):
    calenders=calender.objects.all()
    numberofcalender=len(calenders)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    params={'calender':calenders,'allsys':allsys,'number':numberofcalender}
    return render(response, 'academiccallender.html',params)
def procedure(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render(response,'admissionprocedure.html',params)
def cutoffs(response):
    cutoffs=cutoff.objects.all()
    numberofcutoffs=len(cutoffs)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    params={'cutoff':cutoffs,'allsys':allsys,'number':numberofcutoffs}
    return render(response,'mhtcetcutoff.html',params)
def syllabuss(response):
    allsys1=[]
    branchs=syllabus.objects.values('branch','id')
    branchfil={item['branch'] for item in branchs}
    for bra in branchfil:
        syl=syllabus.objects.filter(branch=bra)
        numberofsyl2=len(syl)
        allsys1.append([syl,numberofsyl2]) 
    numberofsyl1=len(branchs) 
    print(numberofsyl1)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys1':allsys1,'allsys':allsys,'number':numberofsyl1}
    return render(response,'syllabus.html',params)
def questions(response):
    allsys1=[]
    questions=question.objects.values('branch','id')
    branchfil={item['branch'] for item in questions}
    for bra in branchfil:
        syl=question.objects.filter(branch=bra)
        numberofsyl=len(syl)
        allsys1.append([syl,numberofsyl]) 
    numberofsyl1=len(questions) 
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    allfysys=[]
    questionss=firstyearquestion.objects.values('sem','id')
    branchfil={item['sem'] for item in questionss}
    for bra in branchfil:
        syl1=firstyearquestion.objects.filter(sem=bra)
        numberofsyl2=len(syl1)
        allfysys.append([syl1,numberofsyl2]) 
    numberofsyl2=len(questionss) 
    print(allsys)
    params={'allsys1':allsys1,'allsys':allsys,'allfysys':allfysys,'number':numberofsyl1,'number2':numberofsyl2}
    return render(response,'questionpaper.html',params)
def masters(response):
    return render(response,'masters.html')
def elearning(response):
    return render(response,'elearning.html')
def principal(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render(response,'principal.html',params)
def chairman(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render(response,'chairman.html',params)
def secretary(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render(response,'secretary.html',params)
def bachlers(request):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render( request,'bachlers.html',params)
def admission(response):
    forms=admissionform.objects.all()
    number=len(forms)
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys,'form':forms,'number':number}
    return render(response,'admission.html',params)
def apply(request):
    if request.method=='POST':
        name1= request.POST.get('firstname', '')
        lastname= request.POST.get('lastname', '')
        contactnumber= request.POST.get('contact', '')
        city= request.POST.get('city', '')
        course= request.POST.get('course', '')
        date=request.POST.get('date','')
        apply1=Apply(firstname=name1,lastname=lastname,contactnumber=contactnumber,city=city,course=course)
        apply1.save()
    return render( request,'apply.html')
def basic(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    return render(response,'basic.html')
def blog(request):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    blog_details=blogdetails.objects.all()
    numberofblog=len(blog_details)
    params={'blog_details':blog_details,'number':numberofblog,'allsys':allsys}
    return render( request,'blog.html',params)
def companies(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    companys=company.objects.all()
    numberofcompany=len(companys)
    params={'company':companys,'allsys':allsys,'number':numberofcompany}
    return render(response,'companies.html',params)
def courses(request):
    return render( request,'courses.html')
def register(request):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render( request,'alumini registration.html',params)
def libraryoverview(request):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs)
    params={'allsys':allsys}
    return render( request,'libraryoverview.html',params)
def gallery(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    gallery=maingallery.objects.all()
    numberofgall=len(gallery)
    params={'gallery':gallery,'allsys':allsys,'number':numberofgall}
    return render(response,'gallery.html',params)
def aluminis(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    aluminis=alumini.objects.all()
    numberofalumini=len(aluminis)
    params={'aluminis':aluminis,'allsys':allsys,'number':numberofalumini}
    return render(response,'alumini.html',params)
def news(request):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    newspapers=newspaper.objects.all()
    numberofnews=len(newspapers)
    params={'newspaper':newspapers,'allsys':allsys,'number':numberofnews}
    return render( request,'news.html',params)
def placement(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    placements=placementdetails.objects.all()
    place=placementss.objects.all()
    charts=chart.objects.all()
    numberofplaced=len(place)
    params={'placement':placements,'allsys':allsys,'number':numberofplaced,'place':place,'chart':charts}
    return render( response,'placements.html',params)
def projects(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    projectsdetail=projectsdetails.objects.all()
    project=projectss.objects.all()
    numberofprojects=len(project)
    params={'project':project,'allsys':allsys,'number':numberofprojects,'projectdetail':projectsdetail}
    return render( response,'projects.html',params)
def research(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    return render(response,{'allsys':allsys},'research.html')
def sports(request):
    return render( request,'sports.html')
def student(response):
    return render(response,'student.html')
def trips(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    trip=tripss.objects.all()
    tripsdetail=tripsdetails.objects.all()
    numberoftrip=len(trip)
    params={'trips':trip,'allsys':allsys,'number':numberoftrip,'tripsdetail':tripsdetail}
    return render(response,'trips.html',params)
def staff(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    staff_details=staffdetails.objects.all()
    staffss=staffs.objects.all()
    numberofstaff=len(staff_details)
    params={'staff_details':staff_details,'number':numberofstaff,'allsys':allsys,'staff':staffss}
    return render(response,'staff.html',params)

def placementtestmaterial(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    question=placementstestquestion.objects.all()
    numberofquestion=len(question)
    params={'question':question,'allsys':allsys,'number':numberofquestion}
    return render(response,'placementtestmaterial.html',params)


def conferences(response):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 

    question=conference.objects.all()
    numberofquestion=len(question)
    params={'question':question,'allsys':allsys,'number':numberofquestion}
    return render(response,'conference.html',params)

def courses(request,id):
    allsys=[]
    branchs=course.objects.values('dergree','id')
    branchfil={item['dergree'] for item in branchs}
    numberofsyl=len(branchfil)
    for bra in branchfil:
        syl=course.objects.filter(dergree=bra)
        numberofsyl=len(syl)
        allsys.append([syl,numberofsyl]) 
    numberofsyl1=len(branchs) 
    coursess=course.objects.filter(id=id)
    print(courses)
    return render(request, "course.html", {'coursess':coursess,'allsys':allsys})
# Create your views here.
