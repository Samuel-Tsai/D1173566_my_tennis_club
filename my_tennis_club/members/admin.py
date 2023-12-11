
from django.contrib import admin
from .models import Member,Court

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "Age")
  
admin.site.register(Member, MemberAdmin)

class CourtAdmin(admin.ModelAdmin):
    list_display = ("courtname", "kind", "location")

admin.site.register(Court, CourtAdmin)