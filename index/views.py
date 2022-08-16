from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Teacher, Testimonial, Passout, Student10, Student12
# Create your views here.
def indexs(request):
    img=Teacher.objects.all()
    new_testimonial=Testimonial.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        new_emp=Contact(name=name,email=email,subject=subject,message=message)
        new_emp.save()
        return HttpResponse('Thanku for Message') 
    
    return render(request,'indexs.html',{'img' : img, 'new_testimonial' :new_testimonial})
    

def student12(request):
    new_student12=Student12.objects.all()
    return render(request,"student12.html",{'new_student12':new_student12})

def student10(request):
    new_student10=Student10.objects.all()
    return render(request,"student10.html",{'new_student10':new_student10})

def passout(request):
    new_passout=Passout.objects.all()
    return render(request,"passout.html",{'new_passout':new_passout})
# def form(request):
