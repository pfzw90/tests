import requests
import unittest
import pprint
from unittest.mock import patch
import urllib.parse
from yadisk import YandexFolderCreator


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.uploader = YandexFolderCreator('XXX')

    def test_create_folder(self):
        test_directory = 'Test 1 2'
        self.assertEqual(self.uploader.create_folder(test_directory).status_code, 201)
        folders_resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                               params={"path": '/'},
                               headers={"Authorization": f'OAuth {self.uploader.token}'})

        folders_list = [f['name'] for f in folders_resp.json().get('_embedded').get('items') if f['type'] == 'dir']
        self.assertIn('Test 1 2', folders_list)