from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ClientForm, ImmobileForm, RegisterLocationForm
from .models import Immobile, ImmobileImage


# Create your views here.
def list_location(request):
    # Ordenar os imóveis pela coluna 'id' em ordem crescente
    immobiles = Immobile.objects.filter(is_locate=False).order_by('id')  
    context = {'immobiles': immobiles}
    return render(request, 'list-location.html', context)

def form_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-location')   
    return render(request, 'form-client.html', {'form': form})


def form_immobile(request):
    form = ImmobileForm() 
    if request.method == 'POST':
        form = ImmobileForm(request.POST, request.FILES)
        if form.is_valid():
            immobile = form.save()
            files = request.FILES.getlist('immobile') ## pega todas as imagens
            if files:
                for f in files:
                    ImmobileImage.objects.create( # cria instance para imagens
                        immobile=immobile, 
                        image=f)
            return redirect('list-location')   
    return render(request, 'form-immobile.html', {'form': form})


def form_location(request, id):
    get_locate = Immobile.objects.get(id=id)  # Aqui não precisa de `order_by` pois é apenas um objeto
    form = RegisterLocationForm()  
    if request.method == 'POST':
        form = RegisterLocationForm(request.POST)
        if form.is_valid():
            location_form = form.save(commit=False)
            location_form.immobile = get_locate  # Salva id do imóvel 
            location_form.save()  

            # Atualizar status do imóvel para "Alugado"
            immo = Immobile.objects.get(id=id)  # Aqui também é apenas um objeto, sem necessidade de `order_by`
            immo.is_locate = True  
            immo.save() 
            return redirect('list-location')  

    # Ordenar as imagens relacionadas ao imóvel pelo 'id'
    context = {'form': form, 'location': get_locate}
    return render(request, 'form-location.html', context)


## Relatório
def reports(request):
    immobile = Immobile.objects.all().order_by('id')  # Ordenar os imóveis por 'id'

    get_client = request.GET.get('client') 
    get_locate = request.GET.get('is_locate')
    get_type_item = request.GET.get('type_item') 

    get_dt_start = request.GET.get('dt_start')
    get_dt_end = request.GET.get('dt_end')

    if get_client: 
        immobile = Immobile.objects.filter(
					Q(reg_location__client__name__icontains=get_client) | 
					Q(reg_location__client__email__icontains=get_client)
                ).order_by('id')  # Ordenar resultado filtrado

    if get_dt_start and get_dt_end: 
        immobile = Immobile.objects.filter(
						reg_location__create_at__range=[get_dt_start, get_dt_end]
                ).order_by('id')  # Ordenar resultado filtrado

    if get_locate:
        immobile = Immobile.objects.filter(is_locate=get_locate).order_by('id')  # Ordenar resultado filtrado

    if get_type_item:
        immobile = Immobile.objects.filter(type_item=get_type_item).order_by('id')  # Ordenar resultado filtrado

    return render(request, 'reports.html', {'immobiles': immobile})



