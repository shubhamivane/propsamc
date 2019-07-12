from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def index(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        fs = FileSystemStorage()
        dt = str(datetime.now()).replace(':', '_').replace('-', '_').replace('.', '_').replace(' ', '_')
        filename = fs.save(excel_file.name.split('.')[0]+'_'+dt+'.xls', excel_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'index.html')
