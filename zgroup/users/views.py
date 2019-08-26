from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(request):
    redirect_back = request.POST.get('next', request.GET.get('next', '/'))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    context = {'form': form, 'next': redirect_back}

    return render(request, 'users/register.html', context)
