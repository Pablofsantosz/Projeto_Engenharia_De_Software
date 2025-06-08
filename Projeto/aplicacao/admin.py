from django.contrib import admin
from .models import CID, ReceitaTemplate, Consulta

# Register your models here to make them accessible in the Django admin panel.
admin.site.register(CID)
admin.site.register(ReceitaTemplate)
admin.site.register(Consulta)