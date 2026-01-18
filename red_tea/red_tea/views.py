from django.shortcuts import render
import chai
def home(request):
    return render(request,'home.html')

def chais(request):
    return render(request,'chai.html')