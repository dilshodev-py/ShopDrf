import pytest
from apps.tests.conf_fixtures import *
from apps.models import Category


@pytest.mark.django_db
def test_category(categories):
    category = Category.objects.get(name='Texnika')
    assert category.name == "Texnika"
    assert category.id == 1
