from django.test import TestCase
from quest.models import Channel, Campaign


class ChannelCRUDTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        super(ChannelCRUDTestCase, self).setUpTestData()
        self.channel_to_edit = Channel()
        self.channel_to_edit.name = 'name before edit'
        self.channel_to_edit.slug = 'slug before edit'
        self.channel_to_edit.bid_types = ['bdi']
        self.channel_to_edit.save()
        self.channel_to_delete = Channel()
        self.channel_to_delete.name = 'deleted channel'
        self.channel_to_delete.slug = 'deleted slug'
        self.channel_to_delete.bid_types = ['cdi']
        self.channel_to_delete.save()

    def test_create_channel(self):
        response = self.client.get('/channels/new')
        self.assertEqual(response.status_code, 200)
        new_channel_data = {
            'name': 'channel name',
            'slug': 'channel slug',
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
            'slug': 'slug after edit',
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
