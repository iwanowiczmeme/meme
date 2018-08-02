from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import generic
from .forms import UserInputSignalForm
from .models import UserInputSignal

@login_required
def storage(request):

    insta = UserInputSignal(author=request.user)
    print(request.user)

    form = UserInputSignalForm(request.POST or None, request.FILES or None,instance=insta)

    if request.method == 'POST':
        if form.is_valid():
            signal = form.save(commit=False)
            signal.save()

            return redirect('home')
    else:
        form = UserInputSignalForm(instance=insta)

    return render(request,  'storage.html', {'form': form})
