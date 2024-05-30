from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Visit
from .forms import ClientForm, VisitForm
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'patients/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'patients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')

def visit_create(request):
    client_id = request.GET.get('client_id')
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = VisitForm(initial={'client': client_id})
    return render(request, 'patients/visit_form.html', {'form': form})

def generate_pdf(request, pk):
    client = get_object_or_404(Client, pk=pk)
    visits = Visit.objects.filter(client=client)
    html = render_to_string('patients/report.html', {'client': client, 'visits': visits})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{client.id}.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
