
from django.test import TestCase , Client

from apps.models import Category


class TestCategoryList(TestCase):
    def setUp(self):
        Category.objects.create(name="tex")
        Category.objects.create(name="Uy Jihozlari")
        self.client = Client()

    def test_get(self):
        response = self.client.get('/api/v1/category')
        self.assertEqual(response.status_code , 200)
        self.assertEqual(len(response.data) , 2)

    def test_create(self):
        response = self.client.post('/api/v1/category' , data={"name" : "text"})
        self.assertEqual(response.status_code , 201)
        self.assertEqual(response.data["name"] ,"text" )


