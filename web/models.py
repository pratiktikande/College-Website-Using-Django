from django.db import models
class maingallery(models.Model):
    maingallery_id=models.AutoField
    Type=models.CharField(max_length=30,default="")
    ocassion=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    name=models.CharField(max_length=30,default="")
    details=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to ='gallery/images' ,default="")
    def __str__(self):
        return self.name
class alumini(models.Model):
    alumini_id=models.AutoField
    # Type=models.CharField(max_length=30,default="")
    # ocassion=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    name=models.CharField(max_length=30,default="")
    details=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to ='alumini/images' ,default="")
    def __str__(self):
        return self.name
class newspaper(models.Model):
    newspaper_id=models.AutoField
    Type=models.CharField(max_length=30,default="")
    ocassion=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    name=models.CharField(max_length=30,default="")
    details=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to ='newspaper/images' ,default="")
    def __str__(self):
        return self.name
class blogdetails(models.Model):
    blogdetails_id=models.AutoField
    name=models.CharField(max_length=30,default="")
    blog_details1=models.CharField(max_length=250,default="")
    blog_details2=models.CharField(max_length=2000,default="")
    Type=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    image=models.ImageField(upload_to ='blog/images' ,default="")
    writer=models.CharField(max_length=30,default=name)
    def __str__(self):
        return self.name  
class company(models.Model):
    company_id=models.AutoField
    name=models.CharField(max_length=30,default="")
    company_details=models.CharField(max_length=200,default="")
    Type=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    image=models.ImageField(upload_to ='company/images' ,default="")
    def __str__(self):
        return self.name 

class patent(models.Model):
    patent_id=models.AutoField
    title=models.CharField(max_length=100,default="")
    patentnumber=models.CharField(max_length=100,default="")
    year=models.CharField(max_length=100,default="")
    members=models.CharField(max_length=200,default="")
    date=models.DateField(default="2000-12-31")
    def __str__(self):
        return self.title 

class calender(models.Model):
    calender_id=models.AutoField
    link=models.CharField(max_length=500,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.year

class syllabus(models.Model):
    syllabus_id=models.AutoField
    branch=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    title=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title

class question(models.Model):
    question_id=models.AutoField
    branch=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    sem=models.CharField(max_length=100,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.year
class firstyearquestion(models.Model):
    question_id=models.AutoField
    sem=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.year
class placementstestquestion(models.Model):
    question_id=models.AutoField
    title=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title
class conference(models.Model):
    conference_id=models.AutoField
    title=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title
class publication(models.Model):
    conference_id=models.AutoField
    title=models.CharField(max_length=100,default="")
    link=models.CharField(max_length=500,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title
class cutoff(models.Model):
    cutoff_id=models.AutoField
    link=models.CharField(max_length=500,default="")
    title=models.CharField(max_length=100,default="")
    year=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title 

class Apply(models.Model):
    apply_id= models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    contactnumber=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    date=models.CharField(default="",max_length=100)
    def __str__(self):
        return self.firstname 

class admissionform(models.Model):
    cutoff_id=models.AutoField
    link=models.CharField(max_length=500,default="")
    Branch=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.Branch

class course(models.Model):
    course_id=models.AutoField
    details=models.CharField(max_length=4000,default="")
    title=models.CharField(max_length=100,default="")
    shorttitle=models.CharField(max_length=100,default="")
    duration=models.CharField(max_length=50,default="")
    programecode=models.CharField(max_length=50,default="")
    coursetype=models.CharField(max_length=50,default="")
    modeofstudy=models.CharField(max_length=50,default="")
    dergree=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.title

class staffdetails(models.Model):
    staffdetails_id=models.AutoField
    name=models.CharField(max_length=30,default="")
    staff_details=models.CharField(max_length=200,default="")    	
    Date_of_joining=models.DateField(default="2000-12-31")
    Designation=models.CharField(max_length=100,default="")
    Eductaion=models.CharField(max_length=300,default="")
    Subject_of_Teaching=models.CharField(max_length=100,default="")
    Teaching_Experience=models.CharField(max_length=100,default="")
    review=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to ='staff/images' ,default="")
    def __str__(self):
        return self.name

class staffs(models.Model):
    staff_id=models.AutoField
    total_staff=models.CharField(max_length=30,default="")
    total_departments=models.CharField(max_length=30,default="")
    totalnontechingstaff=models.CharField(max_length=30,default="")

class placementss(models.Model):
    placement_id=models.AutoField
    name=models.CharField(max_length=30,default="")
    package=models.CharField(max_length=30,default="")
    company_name=models.CharField(max_length=30,default="")
    candidate_details=models.CharField(max_length=200,default="")    	
    Date_of_allotment=models.DateField(default="2000-12-31")
    jobpost=models.CharField(max_length=100,default="")
    Education=models.CharField(max_length=300,default="")
    Subject=models.CharField(max_length=100,default="")
    review_by_interviewer=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to ='placement/images' ,default="")
    def __str__(self):
        return self.name
class placementdetails(models.Model):
    placementsdetails_id=models.AutoField
    companies_visited=models.CharField(max_length=30,default="")
    averagepackage=models.CharField(max_length=200,default="")
    highestpackage=models.CharField(max_length=30,default="")
    numberofplacement=models.CharField(max_length=30,default="")
class projectss(models.Model):
    projects_id=models.AutoField
    name=models.CharField(max_length=30,default="")
    motive=models.CharField(max_length=100,default="")
    Type=models.CharField(max_length=30,default="")
    project_details=models.CharField(max_length=200,default="")    	
    Date_of_project=models.DateField(default="2000-12-31")
    Achievements=models.CharField(max_length=300,default="")
    Subject=models.CharField(max_length=100,default="")
    review=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to ='projects/images' ,default="")
    image1=models.ImageField(upload_to ='projects/images' ,default="")
    image2=models.ImageField(upload_to ='projects/images' ,default="")
    image3=models.ImageField(upload_to ='projects/images' ,default="")
    def __str__(self):
        return self.name
class projectsdetails(models.Model):
    projectsdetails_id=models.AutoField
    total_projects=models.CharField(max_length=30,default="")
    Bestproject=models.CharField(max_length=30,default="")
    numberofprojectcoordinated=models.CharField(max_length=30,default="")
class tripss(models.Model):
    maingallery_id=models.AutoField
    Type=models.CharField(max_length=30,default="")
    place=models.CharField(max_length=30,default="")
    date=models.DateField(default="2000-12-31")
    details=models.CharField(max_length=700,default="")
    image=models.ImageField(upload_to ='trip/images' ,default="")
    image1=models.ImageField(upload_to ='trip/images' ,default="")
    image2=models.ImageField(upload_to ='trip/images' ,default="")
    image3=models.ImageField(upload_to ='trip/images' ,default="")
    def __str__(self):
        return self.place
class tripsdetails(models.Model):
    tripsdetails_id=models.AutoField
    total_trips=models.CharField(max_length=30,default="")
    Besttrip=models.CharField(max_length=30,default="")
class chart(models.Model):
    Highestpackage=models.CharField(max_length=30,default="")
    Averagepackage=models.CharField(max_length=30,default="")
    Companiesrecruiting=models.CharField(max_length=200,default="")
    studentselected=models.CharField(max_length=200,default="")
    year=models.CharField(max_length=30,default="")
    studentselectedinbranch_comp=models.CharField(max_length=30,default="")
    studentselectedinbranch_IT=models.CharField(max_length=30,default="")
    studentselectedinbranch_Civil=models.CharField(max_length=30,default="")
    studentselectedinbranch_Mech=models.CharField(max_length=30,default="")
    studentselectedinbranch_Data=models.CharField(max_length=30,default="")
    studentselectedinbranch_Aiml=models.CharField(max_length=30,default="")
    studentselectedinbranch_Auto=models.CharField(max_length=30,default="")
    studentselectedinbranch_Electronics=models.CharField(max_length=30,default="")
    studentselectedinbranch_Electronicsandtele=models.CharField(max_length=30,default="")
    studentselectedinbranch_humanities=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.year

class messagebox(models.Model):
    date=models.DateField(default="03-31")
    title=models.CharField(default="",max_length=50)
    link=models.CharField(default="",max_length=300,blank=True)
# Create your models here.
