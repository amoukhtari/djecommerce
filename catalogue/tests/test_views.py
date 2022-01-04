from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import reverse
from django.test import Client
from django.test.testcases import TestCase

from catalogue.models import Category, Product
from catalogue.views import products_all


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='am')
        Category.objects.create(name='cc', slug='cc')
        Product.objects.create(title='product2', category_id=1, created_by_id=1,
                               slug='product2', price='9.99', image='placeholder')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('catalogue:product_detail', args=['product2']))
        self.assertEqual(response.status_code, 200)

    def test_categories_detail_url(self):
        response = self.c.get(reverse('catalogue:category_list', args=['cc']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = products_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Homepage</title>', html)
        self.assertEqual(response.status_code, 200)
