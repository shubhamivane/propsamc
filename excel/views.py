from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
import pandas as pd
from googlegeocoder import GoogleGeocoder
        
def index(request):
    uploaded_file_url = None
    if request.method == 'POST':
        print(settings.BASE_DIR)
        geocoder = GoogleGeocoder(settings.API_KEY)
        excel_file = request.FILES['file']
        fs = FileSystemStorage()
        dt = str(datetime.now()).replace(':', '_').replace('-', '_').replace('.', '_').replace(' ', '_')
        name = excel_file.name.split('.')[0]
        ext = excel_file.name.split('.')[1]
        filename = fs.save(name+'_'+dt+'.'+ext, excel_file)
        df = pd.read_excel(os.path.join(settings.BASE_DIR, 'files',filename))
        cols = list(df.columns)
        rows, _ = df.shape
        lat_list = []
        lng_list = []
        for idx in range(rows):
            address = df[cols[0]][idx]
            search = geocoder.get(address)
            lat_list.append(search[0].geometry.location.lat)
            lng_list.append(search[0].geometry.location.lng)
        df['Latitude'] = lat_list
        df['Longitude'] = lng_list
        print(lat_list)
        df.to_excel(os.path.join(settings.BASE_DIR, 'files',filename))            
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
        })
    return render(request, 'index.html', {
        'uploaded_file_url': uploaded_file_url, 
    })
