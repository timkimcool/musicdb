from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import AlbumBase, Review


class AlbumTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@emgail.com",
            password="testpass123",
        )

        cls.album = AlbumBase.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        cls.review = Review.objects.create(album - cls.AlbumBase, author=cls.user, review="GREAT")

    def test_album_listing(self):
        self.assertEqual(f"{self.album.title}", "Harry Potter")
        self.assertEqual(f"{self.album.author}", "JK Rowling")
        self.assertEqual(f"{self.album.price}", "25.00")

    def test_album_list_view(self):
        response = self.client.get(reverse("album_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "albums/album_list.html")

    def test_album_detail_view(self):
        response = self.client.get(self.album.get_absolute_url())
        no_response = self.client.get("/albums/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "GREAT")
        self.assertTemplateUsed(response, "albums/album_detail.html")
