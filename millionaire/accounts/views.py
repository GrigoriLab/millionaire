from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='accounts/home.html'



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
        else:
            return HttpResponse("not valid info")
    else:
        form = UserCreationForm()
        args = {'form' : form}
        return render(request,'accounts/reg_form.html', args)
