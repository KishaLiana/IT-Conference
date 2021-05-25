from django.shortcuts import render
from .models import Participants,Contact,Program
from django.core.files.storage import FileSystemStorage

def index(request):

    
    return render(request, 'index.html')
def register(request):
    folder='static/files'
    if "register" in request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        speaker = request.POST["speaker"]
        topic = request.POST["topic"]
        description = request.POST["description"]
        file = request.FILES['file']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(file.name,file)
        file_url = fs.url(filename)
        print(file_url)
        register = Participants(
                name              =name,
                email             =email,
                phone             =phone,
                speaker           =speaker,
                topic             =topic,
                description =description,
                file = file,
    )
        register.save()
        print("Registered successfully.....")
        return render(request, 'register.html')
    return render(request, 'register.html')
    
def contact(request):
    if "contact" in request.POST:
        conname = request.POST["name"]
        conemail = request.POST["email"]
        conmsg = request.POST["message"] 
        
        contact = Contact(name=conname,email=conemail,message=conmsg)

        contact.save()

        print("Message sent successfully.")
        return render(request, 'contact.html') 
    return render(request, 'contact.html')    


def schedule(request):
    p1 = Program.objects.filter(day="Day 1")
    p2 = Program.objects.filter(day="Day 2")
    p3 = Program.objects.filter(day="Day 3")
    p4 = Program.objects.filter(day="Day 4")
    
    context= {
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'p4':p4,
            }
    return render(request,'schedule.html',context)

def speakers(request):

    return render(request,'speakers.html')

