from rest_framework import serializers
from quest.models import Channel, Campaign


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('name', 'slug', 'bid_types')


class CampaignSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(many=False, read_only=True)

    class Meta:
        model = Campaign
        fields = ('name', 'channel', 'bid', 'bid_type')
