from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from os import listdir
from os.path import isfile, join

def main(request):
    fs = FileSystemStorage()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'main/home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    onlyfiles = [file for file in listdir(settings.MEDIA_ROOT) if isfile(join(settings.MEDIA_ROOT, file))]
    return render(request, 'main/home.html', {"files" : onlyfiles})