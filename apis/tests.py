from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

# Create your tests here.


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title='A good title',
            subtitle='An excellent subtitle',
            author='Tom Christie',
            isbn='12345678910',
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
