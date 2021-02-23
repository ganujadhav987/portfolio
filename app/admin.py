from django.contrib import admin

# Register your models here.
from app.model.assets import Assets
from app.model.contact import Contact
# from app.model.assets import Assets
# from app.model.assets import Assets

admin.site.register(Assets)
admin.site.register(Contact)