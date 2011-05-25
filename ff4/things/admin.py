from things.models import QuizQuestion, QuizAnswer, Image, QuizAnswerByImage, Collage
from django.contrib import admin
import pdb;

def make_featured(modeladmil, request, queryset):
    queryset.update(featured=1)

make_featured.short_description = "Make selected collages featured"

def unfeature(modeladmil, request, queryset):
    queryset.update(featured=0)

unfeature.short_description = "Make selected collages unfeatured"

class CollageAdmin(admin.ModelAdmin):
    fields = ['filename','username','featured','in_gallery','background_img']
    list_display = ('filename','username','featured','in_gallery','background_img')
    actions = [make_featured,unfeature]



admin.site.register(Collage,CollageAdmin)

