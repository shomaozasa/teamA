from django.shortcuts import render, redirect
from .models import Request, RequestFunction
from .forms import RequestForm, RequestFunctionForm
from django.forms import inlineformset_factory

def request(request):
    RequestFunctionFormSet = inlineformset_factory(
        Request,
        RequestFunction,
        form=RequestFunctionForm,
    )

    if request.method == 'POST':
        request_form = RequestForm(request.POST)
        formset = RequestFunctionFormSet(request.POST)
        if request_form.is_valid() and formset.is_valid():
            request_instance = request_form.save()
            formset.instance = request_instance
            formset.save()
            return redirect('index')
    else:
        request_form = RequestForm()
        formset = RequestFunctionFormSet()

    context = {
        'request_form': request_form,
        'formset': formset,
    }
    return render(request, 'index.html', context)
