from django.contrib import admin
from Cinema.models import Cinemas
# Register your models here.

@admin.register(Cinemas)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['Movie_Name','Actor_Character_Name','Actress_Character_Name','Actor_Name','Actress_Name']




#admin.site.register(Cinemas)