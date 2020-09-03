from django.contrib import admin
from jpow_app.models import SPY, Ratio, Insider, Compensation, UnusualOption
from import_export.admin import ImportExportModelAdmin

@admin.register(SPY, Ratio, Insider, Compensation, UnusualOption)
class viewAdmin(ImportExportModelAdmin):
    pass
