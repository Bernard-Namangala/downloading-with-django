from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.db.models import F
from .models import Journal
import os


def index(request):
    journals = Journal.objects.all()
    context = {
        "journals": journals
    }
    return render(request=request, template_name='journals/index.html', context=context)


def download_journal(request, journal_id):
    # get the journal with provided id
    try:
        file = Journal.objects.get(id=journal_id)
    except Journal.DoesNotExist:
        return HttpResponse("file not found")

    # get absolute path of the file
    absolute_file_path = file.file.path

    # get the file name and extension of the file
    file_name, file_extension = os.path.splitext(file.file.name)

    # create response object
    response = FileResponse(open(absolute_file_path, 'rb'))

    # add content disposition header
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format(f"{file_name.split('/')[-1]}{file_extension}")

    # increment download count of the journal
    # using F to avoid race conditions
    file.download_count = F('download_count') + 1
    # save the journal after incrementing download count
    file.save()
    return response
