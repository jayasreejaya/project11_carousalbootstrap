from django.shortcuts import render

# Create your views here.
def bootstrap_jquery(request):
    return render(request,'bootstrap_jquery.html')