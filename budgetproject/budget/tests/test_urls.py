from django.test import SimpleTestCase
from django.urls import resolve, reverse

from budget.views import ProjectCreateView, project_list, project_detail

class TestUrls(SimpleTestCase):

	def test_list_url(self):
		url = reverse('list')
		self.assertEquals(resolve(url).func, project_list)

	def test_add_url(self):
		url = reverse('add')
		self.assertEquals(resolve(url).func.view_class, ProjectCreateView)
	
	def test_detail_url(self):
		url = reverse('detail', args=['slug'])
		self.assertEquals(resolve(url).func, project_detail)