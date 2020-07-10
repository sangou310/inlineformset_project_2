from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import JutyuCreateForm, JutyuDetailFormset
from .models import JutyuHead


class JutyuListView(ListView):
    model = JutyuHead
    template_name = 'jutyu/jutyu_list.html'


def add_jutyu(request):
    form = JutyuCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        jutyu_head = form.save(commit=False)
        formset = JutyuDetailFormset(request.POST, instance=jutyu_head)
        if formset.is_valid():
            jutyu_head.save()
            formset.save()
            return redirect('jutyu_list')
        else:
            context['formset'] = formset

    else:
        context['formset'] = JutyuDetailFormset()

    return render(request, 'jutyu/jutyu_form.html', context)
