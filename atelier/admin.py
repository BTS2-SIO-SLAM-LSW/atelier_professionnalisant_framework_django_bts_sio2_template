from django.contrib import admin
from .models import Client, Technicien, Incident, Intervention, PieceJointe

admin.site.register(Client)
admin.site.register(Technicien)
admin.site.register(Incident)
admin.site.register(Intervention)
admin.site.register(PieceJointe)
