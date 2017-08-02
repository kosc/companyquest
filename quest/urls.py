from django.conf.urls import url
from rest_framework import routers
from quest.views import ChannelViewSet, CampaignViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'campaigns', CampaignViewSet)

urlpatterns = router.urls
