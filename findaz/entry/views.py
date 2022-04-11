from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterUserForm


# class EntryPage(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'entry/voyti.html'
#     success_url = 'mainpage/index.html'

def entrypage(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('MainPage')
            except:
                form.add_error(None, "OSHIBKA")
    else:
        form = RegisterUserForm
    return render(request, 'entry/voyti.html', {'form': form})