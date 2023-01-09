from django.shortcuts import render
from main.models import Skils, Messaga, Project, About, About_me
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    skils = Skils.objects.all()
    project = Project.objects.all()
    about = About.objects.last()
    about_me = About_me.objects.last()
    return render(request, 'index.html', {'skill': skils, 'project': project, 'about': about, 'about_me': about_me})
# def project(request):
#     project = Project.objects.all()
#     return render(request, {'project': project})

def message(request):
    if request.method == 'POST':
        message = Messaga()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.text = request.POST.get('message')
        message.save()
        return HttpResponseRedirect('/')

# def project(request):
#     if request.method == 'POST':
#         project = Project()
#         project.title = request.POST.get('title')
#         project.discription = request.POST.get('discription')
#         project.link = request.POST.get('link')
#         project.image = request.POST.get('img')






