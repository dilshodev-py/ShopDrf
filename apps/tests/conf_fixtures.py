import pytest

from apps.models import Category, Product


@pytest.fixture
def categories():
    Category.objects.create(name = "Texnika")
    Category.objects.create(name = "Sport")
    Category.objects.create(name = "Uy Jihozlari")
    Category.objects.create(name = "Kitoblar")

# @pytest.fixture
# def products():
#     Product.objects.create(name = "Texnika")
#     Product.objects.create(name = "Sport")
#     Product.objects.create(name = "Uy Jihozlari")
#     Product.objects.create(name = "Kitoblar")