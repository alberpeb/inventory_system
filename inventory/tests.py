from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

class ProductAPITestCase(TestCase):
    """
        Test module for Product Model
    """

    def setUp(self):
        Product.objects.create(
            name="Xiaomi Poco C51",
            description="Xiaomi Android phone",
            price=80,
            quantity=7,
            category="ELECTRONICS"
        )

        Product.objects.create(
            name="Xiaomi Redmi Note 12 4g",
            description="Xiaomi Android phone",
            price=154,
            quantity=5,
            category="ELECTRONICS"
        )

        Product.objects.create(
            name="iPhone 13",
            description="iPhone 13, 128GB",
            price=629,
            quantity=10,
            category="ELECTRONICS"
        )
        
        Product.objects.create(
            name="iPhone 14 Pro",
            description="iPhone 14, 512GB",
            price=1199,
            quantity=7,
            category="ELECTRONICS"
        )

        ####
        Product.objects.create(
            name="shirt",
            description="white shirt",
            price=28,
            quantity=70,
            category="CLOTHING"
        )

        Product.objects.create(
            name="dress",
            description="blue dress",
            price=30,
            quantity=50,
            category="CLOTHING"
        )

        Product.objects.create(
            name="shoes",
            description="nike shoes",
            price=22,
            quantity=30,
            category="CLOTHING"
        )
        
        Product.objects.create(
            name="pullover",
            description="grey pullover",
            price=10,
            quantity=20,
            category="CLOTHING"
        )

        ####
        Product.objects.create(
            name="flour",
            description="all-purpose flour",
            price=15,
            quantity=7,
            category="FOOD"
        )

        Product.objects.create(
            name="soda",
            description="baking soda",
            price=2,
            quantity=51,
            category="FOOD"
        )

        Product.objects.create(
            name="butter",
            description="butter in ounces",
            price=8,
            quantity=9,
            category="FOOD"
        )
        
        Product.objects.create(
            name="eggs",
            description="eggs",
            price=12,
            quantity=5,
            category="FOOD"
        )

 