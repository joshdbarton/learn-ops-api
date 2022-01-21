from django.contrib import admin

# Register your models here.
from .models import (
    NssUser,
    LearningRecordEntry,
    LearningRecord,
    LearningWeight
)


@admin.register(LearningWeight)
class LearningWeightAdmin(admin.ModelAdmin):
    list_display = ['label', 'weight',]

@admin.register(LearningRecord)
class LearningRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'weight',]

@admin.register(LearningRecordEntry)
class LearningRecordEntryAdmin(admin.ModelAdmin):
    list_display = ['record', 'instructor', 'note']

@admin.register(NssUser)
class NssUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'slack_handle', 'github_handle']
