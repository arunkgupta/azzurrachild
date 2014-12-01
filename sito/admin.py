from django.contrib import admin
from sito.models import *
from image_cropping import ImageCroppingMixin
# Register your models here.
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Post, MyModelAdmin)
admin.site.register(Page, MyModelAdmin)
admin.site.register(News, MyModelAdmin)
admin.site.register(Galleria, MyModelAdmin)
admin.site.register(Immagini, MyModelAdmin)

# Register your models here.
