from django.contrib.auth.models import User
from django.test import TestCase

from catalogue.models import Category, Product


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='cc', slug='cc')
        User.objects.create(username='am')
        self.data1 = Product.objects.create(title='product2', category_id=1, created_by_id=1,
                                            slug='product2', price='9.99', image='placeholder')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(data, Product)
        self.assertEqual(str(data), 'product2')
