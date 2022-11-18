from django.shortcuts import redirect, render
from .models import Produit, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    produit_object = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        produit_object = Produit.objects.filter(titre__icontains=item_name)
    paginator = Paginator(produit_object, 4)
    page = request.GET.get('page')
    produit_object = paginator.get_page(page)
    return render(request, 'index.html', {'produit_object': produit_object})

def detail(request, myid):
    produit_object = Produit.objects.get(id=myid)
    return render(request,'detail.html', {'produit': produit_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, telephone=telephone, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
        
    return render(request,'checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom    
    return render(request,'confirmation.html', {'name': nom})