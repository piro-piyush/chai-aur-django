from django.shortcuts import render, get_object_or_404
from .models import Chai
# Create your views here.
def chai(request):
    chais = Chai.objects.all
    return render(request,'chai/chai.html',{'chais':chais})
def chai_description(request, chai_id):
    chai = get_object_or_404(Chai, pk=chai_id)
    return render(request,'chai/chai_description.html',{'chai': chai})
