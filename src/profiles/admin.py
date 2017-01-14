from django.contrib import admin
from .models import Profile


class profieAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile


admin.site.register(Profile, profieAdmin)


