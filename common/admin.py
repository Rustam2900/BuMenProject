from django.contrib import admin
from django.contrib.admin.models import LogEntry
from modeltranslation.admin import TranslationAdmin

from common.models import Settings, Quotes, FAQ, Advertising, News
# from simple_history.admin import SimpleHistoryAdmin

# from audit_log.models import

# admin.site.register(LogEntry)


@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        if Settings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Quotes)
admin.site.register(FAQ)
admin.site.register(News)
admin.site.register(Advertising)
