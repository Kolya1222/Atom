from django.contrib import admin

from main.models import status, clients,User

admin.site.register(User)
@admin.register(status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('stat',)}

@admin.register(clients)
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('first_name',"middle_name",)}