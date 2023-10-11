from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from employeer.models import Employeer
from employeer.forms import EmployeerForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# def index(request):
#     return render(request, 'employeer/index.html', {
#         'employeers': Employeer.objects.all(),
#         'form': EmployeerForm()
#         })

# def add_employeer(request):
#     if request.method == "POST":
#         form = EmployeerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'employeer/add_employeer.html', {'form': EmployeerForm()})

# def view_employeer(request, pk):
#     employeer = get_object_or_404(Employeer, pk=pk)
#     return render(request, 'employeer/view_employeer.html', {'employeer': employeer})

# def edit_employeer(request, pk):
#     if request.method == "POST":
#         employeer = get_object_or_404(Employeer, pk=pk)
#         form = EmployeerForm(request.POST, instance=employeer)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     employeer = get_object_or_404(Employeer, pk=pk)
#     return render(request, 'employeer/edit_employeer.html', {
#         'form': EmployeerForm(instance=employeer),
#         'employeer': employeer
#         })

# def delete_employeer(request, pk):
#     if request.method == "POST":
#         employeer = get_object_or_404(Employeer, pk=pk)
#         employeer.delete()
#         return redirect('index')
#     return HttpResponse("Not allowed")