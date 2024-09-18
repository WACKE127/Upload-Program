from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadHandler
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
import os

def home(request):
    return render(request, "upload_file.html")

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            path = default_storage.save('uploads/' + file.name, ContentFile(file.read()))
            file_path = os.path.join(default_storage.location, path)

            # Create a UploadHandler instance and populate additional fields
            file_metadata = form.save(commit=False)
            file_metadata.file_path = file_path
            file_metadata.file_size = file.size
            file_metadata.file_name = file.name
            file_metadata.save()

            messages.success(request, 'File uploaded successfully!')
            return redirect('upload_file')
            # return render(request, 'upload_file.html', {'form': form}) 
    else:
        form = UploadForm()
    return render(request, 'upload_file.html', {'form': form})
