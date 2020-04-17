from django.shortcuts import render,redirect
from django.contrib import messages
from app33.forms import StudentForm,CourseForm
from app33.models import CourseModel,StudentModel

def showIndex(request):
    all_c = CourseModel.objects.all()
    all_s = StudentModel.objects.all()
    return render(request,"index.html",{"cform":CourseForm(),"sform":StudentForm(),"call":all_c,"sall":all_s})


def save_course(request):
    if request.method == "POST":
        cf = CourseForm(request.POST)
        if cf.is_valid():
            i = request.POST["cid"]
            n = request.POST["name"]
            f = request.POST["fee"]
            CourseModel(cid=i, name=n, fee=f).save()
            mess = "Course is Saved"
            messages.success(request, mess)
            return redirect('main')
        else:
            return render(request, "index.html", {"cform": cf, "sform": StudentForm()})
    else:
        return redirect('main')


def save_student(request):
    i = request.POST["sid"]
    n = request.POST["name"]
    c = request.POST["contact"]
    cid = request.POST.getlist("courseid")
    st = StudentModel(sid=i,name=n,contact=c)
    st.save()
    st.courseid.set(cid)

    mess = "Student is Saved"
    messages.success(request, mess)
    return redirect('main')