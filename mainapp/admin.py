from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *



class MedicineAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='medicine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CoronaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='corona'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ForKidsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='forkids'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TechAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tech'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class OpticaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='optica'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Corona, CoronaAdmin)
admin.site.register(ForKids, ForKidsAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(Optica, OpticaAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)



