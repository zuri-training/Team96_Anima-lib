from django.contrib import admin
from .models import *
# from .models import User
# from .models import Message
# from .models import Lib
# from .models import My_Lib
admin.site.register(Profile)
# admin.site.register(User)
admin.site.register(Message)
admin.site.register(Lib)
admin.site.register(My_Lib)

# Register your models here.
