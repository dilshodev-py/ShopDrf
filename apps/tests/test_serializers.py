# from django.test import TestCase
#
# from apps.models import Category
# from apps.serializers import CategoryModelSerializer
#
#
# class TestCategorySerializer(TestCase):
#     def setUp(self):
#         Category.objects.create(name="text")
#         Category.objects.create(name="Uy Jihozlari")
#
#
#     def test_serializer(self):
#         obj = Category.objects.get(name = "text")
#         data = CategoryModelSerializer(obj).data
#         assert isinstance(data , dict)
#         assert data['id'] == 1
#         assert data['name'] == "text"
#
#     def test_deserializer(self):
#         data = {"name" : "text"}
#         obj  = CategoryModelSerializer(data=data)
#         assert obj.is_valid()
#         assert obj.validated_data['name'] == 'text'

import datetime
from apps.tests.conf_fixtures import *
import pytest

from apps.models import Category
from apps.serializers import CategoryModelSerializer


@pytest.mark.django_db
def test_category_deserializer():
    category1 = {
        "id" : 1,
        "name" : "Texnika",
        "created_at" : datetime.datetime.now()
    }
    category2 = {
        "id": 2,
        "name": "py",
        "created_at": datetime.datetime.now()
    }
    obj1 = CategoryModelSerializer(data = category1)
    obj2 = CategoryModelSerializer(data = category2)
    assert obj1.is_valid()
    print("100"*1000)
    assert not obj2.is_valid()
    assert obj1.validated_data['name'] == 'Texnika'

@pytest.mark.django_db
def test_category_serializer(categories):
    category = Category.objects.first()
    data = CategoryModelSerializer(category).data
    assert isinstance(data , dict)
    assert data['id'] == 1
    assert data['name'] == 'Texnika'


