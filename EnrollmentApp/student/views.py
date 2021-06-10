from django.shortcuts import render

from .forms import StudentForm
from .models import StudentData


# Create your views her
# View to list out all the Students data
def showdata(request):
    studentdata = StudentData.objects.all()

    context = {"studentdata": studentdata, }

    return render(request, 'dappx/base.html', context)


# View for enrolling new student
def update(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        # print("else")
        form = StudentForm()

    return render(request, 'dappx/new.html', {'form': form})


# view to display details of particular student
def display(request, studentname):
    data= StudentData.objects.get(studentname=studentname)

    return render(request, 'dappx/student.html', {'data': data})
