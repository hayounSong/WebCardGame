from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CardGame)
admin.site.register(Card)
admin.site.register(User)
admin.site.register(Attack)
admin.site.register(Defense)