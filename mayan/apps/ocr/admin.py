from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    DocumentTypeSettings, DocumentVersionPageOCRContent,
    DocumentVersionOCRError
)


@admin.register(DocumentVersionPageOCRContent)
class DocumentVersionPageOCRContentAdmin(admin.ModelAdmin):
    pass
    #list_display = ('document_page',)


@admin.register(DocumentTypeSettings)
class DocumentTypeSettingsAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'auto_ocr')


@admin.register(DocumentVersionOCRError)
class DocumentVersionOCRErrorAdmin(admin.ModelAdmin):
    list_display = ('document_version', 'datetime_submitted')
    readonly_fields = ('document_version', 'datetime_submitted', 'result')
