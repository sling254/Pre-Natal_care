from django.shortcuts import render, redirect, get_object_or_404
from .forms import MaternalRecordForm
from django.contrib import messages
from .models import MaternalRecord

# Create your views here.

def index(request):
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

