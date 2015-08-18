from django.shortcuts import render_to_response, get_object_or_404
from django.utils import *
from django.http import HttpResponse

from django.template import Context, loader
from jobs.models import Job

from django.shortcuts import get_object_or_404, render_to_response


# Create your views here.

def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    return render_to_response('jobs/job_list.html',
                              {'object_list': object_list})

def detail(request, job_id):
    j = get_object_or_404(Job, pk=job_id)
    return render_to_response('jobs/job_detail.html',
                              {'job': j})