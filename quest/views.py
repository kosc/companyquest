from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from rest_framework import viewsets
from quest.models import Channel, Campaign
from quest.serializers import ChannelSerializer, CampaignSerializer


class ChannelList(ListView):
    model = Channel


class ChannelDetail(DetailView):
    model = Channel

    def get_context_data(self, **kwargs):
        context = super(ChannelDetail, self).get_context_data(**kwargs)
        return context


class ChannelCreate(CreateView):
    model = Channel
    fields = ['name', 'slug', 'bid_types']
    success_url = reverse_lazy('channel_list')


class ChannelUpdate(UpdateView):
    model = Channel
    fields = ['name', 'slug', 'bid_types']
    success_url = reverse_lazy('channel_list')


class ChannelDelete(DeleteView):
    model = Channel
    success_url = reverse_lazy('channel_list')


class CampaignList(ListView):
    model = Campaign


class CampaignDetail(DetailView):
    model = Campaign

    def get_context_data(self, **kwargs):
        context = super(CampaignDetail, self).get_context_data(**kwargs)
        return context


class CampaignCreate(CreateView):
    model = Campaign
    fields = ['name', 'channel', 'bid', 'bid_type']
    success_url = reverse_lazy('campaign_list')


class CampaignUpdate(UpdateView):
    model = Campaign
    fields = ['name', 'channel', 'bid', 'bid_type']
    success_url = reverse_lazy('campaign_list')


class CampaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
