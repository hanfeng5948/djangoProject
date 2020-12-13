from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(SmInfo)
class SmInfoAdmin(admin.ModelAdmin):
    model = SmInfo
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
    list_display = ['ID', 'TITLE', 'ADDRESS', 'LAIYUAN', 'colored_name']
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

    def LM_lmcode(self, obj):
        return obj.LM.lmcode


@admin.register(lm)
class lmAdmin(admin.ModelAdmin):
    list_display = ['id', 'lmtitle', 'lmcode']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['lmtitle']
        return self.readonly_fields


admin.site.site_title = '佛教网站后台管理'
admin.site.site_header = '佛教网站'
