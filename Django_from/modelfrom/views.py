from django.shortcuts import render, HttpResponseRedirect
from .forms import Registion
from .models import Vser
from django.contrib import messages
# Create your views here.
def User (request):
     if request.method == 'POST':
       fm = Registion(request.POST)
       if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         ps = fm.cleaned_data['password']
         ms = fm.cleaned_data['massages']
         reg = Vser(name=nm, email=em, password=ps, massages=ms)
         reg.save()
         fm = Registion()
         messages.add_message(request, messages.SUCCESS, 'Your Request has been submited' )

     else:
        fm = Registion()
     Student = Vser.objects.all()
     return render(request, 'home.html', {'from':fm, 'Std':Student})