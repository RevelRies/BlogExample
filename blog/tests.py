from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        ''' проверка на открытие страницы без ошибок по url '''
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        ''' проверка на открытие страницы без ошибок по name страницы '''
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        ''' проверка на название шаблона для страницы по ее name '''
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_template_content(self):
        ''' проверка на содержание шаблона для страницы по ее name '''
        response = self.client.get(reverse('home'))
        self.assertContains(response, "<h1>Home Page</h1>")


class AboutpageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        ''' проверка на открытие страницы без ошибок по url '''
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_url_available_by_name(self):
        ''' проверка на открытие страницы без ошибок по name страницы '''
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        ''' проверка на название шаблона для страницы по ее name '''
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_template_content(self):
        ''' проверка на содержание шаблона для страницы по ее name '''
        response = self.client.get(reverse('about'))
        self.assertContains(response, "<h1>About</h1>")


