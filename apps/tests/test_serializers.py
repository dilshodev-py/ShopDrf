from django.test import TestCase

from apps.models import Category
from apps.serializers import CategoryModelSerializer


class TestCategorySerializer(TestCase):
    def setUp(self):
        Category.objects.create(name="text")
        Category.objects.create(name="Uy Jihozlari")


    def test_serializer(self):
        obj = Category.objects.get(name = "text")
        data = CategoryModelSerializer(obj).data
        assert isinstance(data , dict)
        assert data['id'] == 1
        assert data['name'] == "text"

    def test_deserializer(self):
        data = {"name" : "text"}
        obj  = CategoryModelSerializer(data=data)
        assert obj.is_valid()
        assert obj.validated_data['name'] == 'text'









