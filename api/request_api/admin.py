from django.contrib import admin
from .models  import Headers,Body,Requests
# Register your models here.
admin.site.register(Requests)
admin.site.register(Headers)
admin.site.register(Body)