import pytest
from django.test import TestCase
from django.urls import reverse


# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
