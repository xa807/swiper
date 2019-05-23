import os

from libs import oss
from unittest import TestCase


class TestOSS(TestCase):

    def test_upload(self):

        filename = 'mm6.jpg'
        key = oss.upload_file(filename)
        print(key)
        self.assertIsNotNone(key, '上传失败')

    def test_donwload(self):
        key = '6c1d825ea60945e7ac2eac093f74bd3c'
        filename = 'mm6_2.jpg'

        oss.download_file(key, filename)
        self.assertTrue(os.path.exists(filename), '下载失败')

    def test_delete(self):
        key = 'f1c1e77b61ec4bcfb9d8909bddad5822'
        oss.delete_file(key)

    def test_geturl(self):
        key = '2f8966d2d0a145e99ce2fbfb1ce33e0b'
        url = oss.get_url(key)
        self.assertIsNotNone(url, '获取图片路径失败')
        print(url)


    def test_get_small_url(self):
        key = '2f8966d2d0a145e99ce2fbfb1ce33e0b'
        url = oss.get_small_url(key)
        self.assertIsNotNone(url, '获取图片路径失败')
        print(url)
