from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from django.utils.translation import ugettext_lazy as _

from .models import AppGroup, AppLink, Theme


class AppLinkInline(admin.TabularInline):
    model = AppLink
    fields = (
        "name",
        "link",
        "icon",
    )
    fk_name = "app_group"
    extra = 0


@admin.register(AppGroup)
class AppGroupAdmin(OrderedModelAdmin):
    list_display = (
        "name",
        "move_up_down_links",
    )
    fields = (
        "name",
        "slug",
        "icon",
        "models",
    )
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("models",)
    inlines = (AppLinkInline,)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    fields = ('name', 'active', 'dm_bc', 'dm_hover_bc', 'dm_c', 'dm_drop_bc', 'dm_drop_hover_bc', 'dm_drop_c')
