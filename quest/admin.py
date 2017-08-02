from django.contrib import admin
from .models import Channel, Campaign


class CampaignInstanceInline(admin.StackedInline):
    model = Campaign


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    inlines = [CampaignInstanceInline]


admin.site.register(Campaign)
