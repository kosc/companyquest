"""companyquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from quest.views import ChannelList, ChannelCreate, ChannelDetail, \
                        ChannelUpdate, ChannelDelete, \
                        CampaignList, CampaignCreate, CampaignDetail, \
                        CampaignUpdate, CampaignDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^channels$', ChannelList.as_view(), name='channel_list'),
    url(r'^channels/new$', ChannelCreate.as_view(), name='channel_new'),
    url(r'^channels/detail/(?P<slug>[-\w]+)/', ChannelDetail.as_view(), name='channel_detail'),
    url(r'^channels/edit/(?P<pk>\d+)$', ChannelUpdate.as_view(), name='channel_edit'),
    url(r'^channels/delete/(?P<pk>\d+)$', ChannelDelete.as_view(), name='channel_delete'),

    url(r'^campaigns$', CampaignList.as_view(), name='campaign_list'),
    url(r'^campaigns/new$', CampaignCreate.as_view(), name='campaign_new'),
    url(r'^campaigns/detail/(?P<pk>\d+)/', CampaignDetail.as_view(), name='campaign_detail'),
    url(r'^campaigns/edit/(?P<pk>\d+)$', CampaignUpdate.as_view(), name='campaign_edit'),
    url(r'^campaigns/delete/(?P<pk>\d+)$', CampaignDelete.as_view(), name='campaign_delete'),

    url(r'^api/', include('quest.urls', namespace='quest')),
]
