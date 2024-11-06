from django.contrib import admin

from core.models import Tovar, Kategoriya, Teg, TovarlarTeglar, KategoriyalarTeglar, CustomUser

from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

class UserAdmin2(UserAdmin):
    def __init__(self, *args, **kwargs):
        self.fieldsets[1][1]["fields"] = ("first_name", "last_name", "email", "phone_number")
        super(self.__class__, self).__init__(*args, **kwargs)

admin.site.register(CustomUser, UserAdmin2)


class TegInline(admin.TabularInline):
    model = TovarlarTeglar


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    inlines = [TegInline]


@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    pass


@admin.register(Teg)
class TegAdmin(admin.ModelAdmin):
    pass


@admin.register(TovarlarTeglar)
class TovarlarTeglarAdmin(admin.ModelAdmin):
    pass


@admin.register(KategoriyalarTeglar)
class KategoriyalarTeglarAdmin(admin.ModelAdmin):
    pass
