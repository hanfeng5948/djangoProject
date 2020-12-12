from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(SmInfo)
class SmInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('寺庙信息', {
            'fields': ('ID', 'TITLE', 'ADDRESS', 'ZHUCHI', 'PAIXU', 'LAIYUAN')
        }),
        ('栏目信息', {
            'classes': ('collapse',),
            'fields': ('LM',),
        }),
    )
    # radio_fields = {'LM': admin.VERTICAL}
    ordering = ['ID']
    sortable_by = ['ID', 'TITLE', 'ADDRESS']
    list_display = ['ID', 'TITLE', 'ADDRESS', 'LAIYUAN']
    list_filter = ['LM__lmtitle']
    list_per_page = 15
    list_max_show_all = 40
    list_editable = ['ADDRESS']
    search_fields = ['TITLE', 'ADDRESS']
    date_hierarchy = 'CREATETIME'
    save_as = True
    actions_on_top = False
    actions_on_bottom = True
    list_display_links = ['TITLE']
    readonly_fields = ['ID', 'PAIXU', ]


@admin.register(lm)
class lmAdmin(admin.ModelAdmin):
    list_display = ['id', 'lmtitle', 'lmcode']
