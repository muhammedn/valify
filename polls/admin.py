from django.contrib import admin
from .models import Poll, Vote


# Register your models here.

class VoteInLine(admin.TabularInline):
    model = Vote
    extra = 3


class PollAdmin(admin.ModelAdmin):
    inlines = [VoteInLine]


admin.site.register(Poll, PollAdmin)
