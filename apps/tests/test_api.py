# import json
#
# from django.test import TestCase , Client
# from django.urls import reverse_lazy
#
# from apps.models import Category
#
#
# class TestCategoryList(TestCase):
#     def setUp(self):
#         Category.objects.create(name="tex")
#         Category.objects.create(name="Uy Jihozlari")
#         self.client = Client()
#
#     def test_get(self):
#         response = self.client.get('/api/v1/category')
#         self.assertEqual(response.status_code , 200)
#         self.assertEqual(len(response.data) , 2)
#
#     def test_create(self):
#         response = self.client.post('/api/v1/category' , data={"name" : "text"})
#         self.assertEqual(response.status_code , 201)
#         self.assertEqual(response.data["name"] ,"text" )
#
#     def test_delete(self):
#         category = Category.objects.first()
#         path = "/api/v1/category"
#         response = self.client.delete(f"{path}/{category.id}")
#         assert response.status_code == 204
#
#     def test_update(self):
#         category = Category.objects.first()
#         path = "/api/v1/category"
#         response = self.client.put(
#             f"{path}/{category.id}" ,
#             data=json.dumps({"name" : "Texnik"}),
#             content_type='application/json', follow=True
#         )
#         assert response.status_code == 200
#         assert response.data['id'] == category.id
#         assert response.data['name'] == "Texnik"
from http import HTTPStatus
from os.path import join

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile, SimpleUploadedFile
from django.test.client import Client
from rest_framework.reverse import reverse

from apps.tests.conf_fixtures import *
from core.settings import BASE_DIR


@pytest.mark.django_db
def test_category_list(client, categories):
    path = reverse('category-list-create')
    response = client.get(path)
    assert len(response.data) == 4
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_category_create(client, categories):
    path = reverse('category-list-create')
    response = client.post(path, data={"name": "Food"})
    categories_count = Category.objects.count()
    assert response.status_code == HTTPStatus.CREATED
    assert response.data["name"] == "Food"
    assert categories_count == 5


@pytest.mark.django_db
def test_product_create(client: Client  , categories):
    path = reverse('product-list-create')
    with open(join(BASE_DIR, 'img.png') , 'rb') as f:
        file = SimpleUploadedFile(
            name='img.png',
            content=f.read(),
            content_type='image/png'
        )
        data = {
            "name": "string",
            "price": 7.1,
            "discount": 100,
            "quantity": 90,
            "description": "string",
            "image": file,
            "category": 1
        }
        response = client.post(path, data=data , format='multipart')
    assert response.status_code == 201
    assert response.data['id'] == 1



