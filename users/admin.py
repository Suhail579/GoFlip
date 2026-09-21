# Register your models here.
from django.contrib import admin

from users.models import Bookss, Mobiles, Bikes, Electronicss, Cars, CoustomUser, Furniture, Gadgets

admin.site.register(Bookss)
admin.site.register(Mobiles)
admin.site.register(Bikes)
admin.site.register(Electronicss)
admin.site.register(Cars)
admin.site.register(CoustomUser)
admin.site.register(Furniture)
admin.site.register(Gadgets)

