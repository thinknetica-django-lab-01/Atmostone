import random
import string

from django.test import TestCase
from django.urls import reverse

from .models import Country, City, HotelFeature, Hotel


class MainPageViewTest(TestCase):
    def test_view_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('main:index'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse('main:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/index.html')


class HotelListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        num = 10
        letters = string.ascii_letters
        for i in range(num):
            Country.objects.create(title=''.join(random.choice(letters) for i in range(num)))

        countries = Country.objects.all()

        for i in range(num):
            City.objects.create(title=''.join(random.choice(letters) for i in range(num)),
                                country=random.choice(countries))

        cities = City.objects.all()

        stars_set = ['N', '1', '2', '3', '4', '5']

        for i in range(num):
            HotelFeature.objects.create(title=''.join(random.choice(letters) for i in range(num)))

        features = HotelFeature.objects.all()

        for i in range(num):
            title = ''.join(random.choice(letters) for i in range(num))
            Hotel.objects.create(title=title,
                                 city=random.choice(cities),
                                 address=''.join(random.choice(letters) for i in range(random.randint(10, 100))),
                                 rating=round(random.uniform(0, 10), 2),
                                 stars=random.choice(stars_set))
            Hotel.objects.get(title=title).features.set(random.sample(list(features), random.randint(0, 5)))

    def test_view_exists(self):
        resp = self.client.get('/hotels/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('main:hotel_list'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get(reverse('main:hotel_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/hotel_list.html')

    def test_pagination(self):
        resp = self.client.get(reverse('main:hotel_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['object_list']) == 3)


class HotelDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(title='Russia')
        City.objects.create(title='Moscow', country=Country.objects.get(title='Russia'))
        HotelFeature.objects.create(title='parking')
        HotelFeature.objects.create(title='gym')
        Hotel.objects.create(title='Raddison',
                             city=City.objects.get(title='Moscow'),
                             address='Some address',
                             rating=8.37,
                             stars='5')
        Hotel.objects.get(title='Raddison').features.set([HotelFeature.objects.get(title='parking'),
                                                          HotelFeature.objects.get(title='gym')])

    def test_view_exists(self):
        pk = Hotel.objects.get(title='Raddison').pk
        resp = self.client.get(f'/hotels/{pk}')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        pk = Hotel.objects.get(title='Raddison').pk
        resp = self.client.get(reverse('main:hotel_detail', kwargs={'pk': pk}))
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        pk = Hotel.objects.get(title='Raddison').pk
        resp = self.client.get(reverse('main:hotel_detail', kwargs={'pk': pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/hotel_detail.html')
