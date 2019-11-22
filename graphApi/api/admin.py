from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncDay

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
# web/admin.py
from django.contrib import admin
from .models import EmailSubscriber

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'notes', 'category')
    list_filter = ('category', 'id', 'name', 'notes', 'category')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)
    


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at") # display these table columns in the list view
    ordering = ("-created_at",) 
    date_hierarchy =("created_at")
    change_list_template='pages/admin/change_liste_dataemai.html'
    
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = EmailSubscriber.objects.annotate(date=TruncDay("created_at")).values("date").annotate(nombre_email=Count("id")).order_by("-date")
        
        # Serialize and attach the chart data to the template context
        data ={
            "chart_data":chart_data,
            "nom":"patrick ou pentest225",
        }
        print (chart_data)
        extra_context = extra_context or data

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


_register(models.Category, CategoryAdmin)
_register(models.Ingredient, IngredientAdmin)
