from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MaternalRecordForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'maternal_care/index.html')





@login_required
def record(request):
    form = MaternalRecordForm()
    if request.method == 'POST':
        form = MaternalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Data saved successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Data is not saved')
    else:
        return render(request, 'maternal_care/record.html')


    return redirect('index')

