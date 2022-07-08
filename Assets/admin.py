from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PostWelcome, PostCCB, RegisterCCB, PostEFCC, RegisterEFCC

admin.site.register(PostWelcome)
admin.site.register(PostCCB)
admin.site.register(RegisterCCB)
admin.site.register(PostEFCC)
admin.site.register(RegisterEFCC)
