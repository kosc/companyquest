from django.test import TestCase
from quest.models import Channel, Campaign


class ChannelCRUDTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        super(ChannelCRUDTestCase, self).setUpTestData()
        self.channel_to_edit = Channel()
        self.channel_to_edit.name = 'name before edit'
        self.channel_to_edit.slug = 'slug-before-edit'
        self.channel_to_edit.bid_types = ['bdi']
        self.channel_to_edit.save()
        self.channel_to_delete = Channel()
        self.channel_to_delete.name = 'deleted channel'
        self.channel_to_delete.slug = 'deleted-slug'
        self.channel_to_delete.bid_types = ['cdi']
        self.channel_to_delete.save()
        self.channel_to_read = Channel()
        self.channel_to_read.name = 'Readable channel'
        self.channel_to_read.slug = 'channel-slug'
        self.channel_to_read.bid_types = ['cdi']
        self.channel_to_read.save()

    def test_read_channel(self):
        response = self.client.get('/channels/detail/' + self.channel_to_read.slug + '/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Readable channel')
        self.assertContains(response, 'channel-slug')
        self.assertContains(response, 'cdi')

    def test_create_channel(self):
        response = self.client.get('/channels/new')
        self.assertEqual(response.status_code, 200)
        new_channel_data = {
            'name': 'channel name',
            'slug': 'channel-slug',
            'bid_types': 'cdi',
        }
        response = self.client.post(
                '/channels/new',
                new_channel_data,
                follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "channel name")

    def test_update_channel(self):
        edit_url = '/channels/edit/' + str(self.channel_to_edit.id)
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        edited_channel_data = {
            'name': 'name after edit',
            'slug': 'slug-after-edit',
            'bid_types': 'cdi',
        }
        response = self.client.post(edit_url, edited_channel_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name after edit")

    def test_delete_channel(self):
        delete_url = '/channels/delete/' + str(self.channel_to_delete.id)
        response = self.client.get('/channels')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "deleted channel")
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure")
        response = self.client.post(delete_url, {}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "deleted channel")


class CampaignCRUDTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        super(CampaignCRUDTestCase, self).setUpTestData()
        self.channel = Channel()
        self.channel.name = 'Channel Name'
        self.channel.slug = 'channel-slug'
        self.channel.bid_types = ['cdi']
        self.channel.save()
        self.campaign_to_edit = Campaign()
        self.campaign_to_edit.name = 'name before edit'
        self.campaign_to_edit.channel = self.channel
        self.campaign_to_edit.bid = 23.3
        self.campaign_to_edit.bid_type = 'bdi'
        self.campaign_to_edit.save()
        self.campaign_to_delete = Campaign()
        self.campaign_to_delete.name = 'deleted campaign'
        self.campaign_to_delete.channel = self.channel
        self.campaign_to_delete.bid = 24.5
        self.campaign_to_delete.bid_type = 'cdi'
        self.campaign_to_delete.save()
        self.campaign_to_read = Campaign()
        self.campaign_to_read.name = 'Readable campaign'
        self.campaign_to_read.channel = self.channel
        self.campaign_to_read.bid = 25.6
        self.campaign_to_read.bid_type = 'cdi'
        self.campaign_to_read.save()

    def test_read_campaign(self):
        response = self.client.get('/campaigns/detail/' + str(self.campaign_to_read.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Readable campaign')
        self.assertContains(response, 'Channel Name')
        self.assertContains(response, '25.6')
        self.assertContains(response, 'cdi')

    def test_create_campaign(self):
        response = self.client.get('/campaigns/new')
        self.assertEqual(response.status_code, 200)
        new_campaign_data = {
            'name': 'Campaign name',
            'channel': self.channel,
            'bid': 23.1,
            'bid_type': 'cdi',
        }
        response = self.client.post(
                '/campaigns/new',
                new_campaign_data,
                follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Campaign name")

    def test_update_campaign(self):
        edit_url = '/campaigns/edit/' + str(self.campaign_to_edit.id)
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        edited_campaign_data = {
            'name': 'name after edit',
            'channel': self.channel,
            'bid': 23.1,
            'bid_type': 'cdi',
        }
        response = self.client.post(edit_url, edited_campaign_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name after edit")

    def test_delete_campaign(self):
        delete_url = '/campaigns/delete/' + str(self.campaign_to_delete.id)
        response = self.client.get('/campaigns')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "deleted campaign")
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure")
        response = self.client.post(delete_url, {}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "deleted campaign")
