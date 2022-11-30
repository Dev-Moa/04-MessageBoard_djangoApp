from django.test import TestCase
from .models import posts
from django.urls import reverse
# Create your tests here.

# class PostTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.posts = posts.objects.create(text="This is db test")
#     def test_model_content(self):
#         self.assertEqual(self.posts.text,"This is db test" )

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = posts.objects.create(text="This is db test")
    # db test
    def test_model_content(self):
        self.assertEqual(self.posts.text, "This is db test")
    # url test
    def test_url_exist_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_homepage(self): # new
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "This is db test")