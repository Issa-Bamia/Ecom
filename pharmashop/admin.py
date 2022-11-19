from django.contrib import admin
from .models import Categorie,Produit, Commande


# Register your models here.
admin.site.site_header = "PHARMA-SHOP"
admin.site.site_title = "COSIT-SHOP"
admin.site.index_title ="Administrateur"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom','date_ajout')
    
class AdminProduit(admin.ModelAdmin):
    list_display = ('titre','prix','categorie','date_ajout',)
    search_fields = ('titre',)
    list_editable = ('prix',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items','nom','email','address', 'ville', 'pays','total', 'date_commande',)
    
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Produit, AdminProduit)
admin.site.register(Commande, AdminCommande)