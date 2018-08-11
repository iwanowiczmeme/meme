from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import generic
from .forms import InputSignalForm
from .models import InputSignal


@login_required
def storage(request):

    insta = InputSignal(author=request.user)
    print(request.user)

    form = InputSignalForm(request.POST, request.FILES, instance=insta)

    if request.method == 'POST':
        if form.is_valid():
            signal = form.save(commit=False)
            signal.save()

            return redirect('storage-main')
    else:
        form = InputSignalForm(instance=insta)

    return render(request,  'storage.html', {'form': form})


@login_required
def storage_main(request):
    return render(request, 'storage_main.html')


@login_required
def storage_list(request):

    signals = InputSignal.objects.filter(author=request.user)
    return render(request, 'storage_list.html', {'signals': signals})


@login_required
def delete(request, pk):

    if request.method == 'DELETE':
        signal = get_object_or_404(InputSignal, pk=pk)
        signal.delete()

    return HttpResponseRedirect('/')
