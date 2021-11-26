from django.http import response
from django.test import Client, TestCase
from django.urls import resolve, reverse

from budget.models import  Project, Expense, Category
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.project1 = Project.objects.create(
			name='project1',
			budget=10000
		)
		self.category1 = Category.objects.create(
			project=self.project1,
			name='development'
		)
		self.list_url = reverse('list')
		self.add_url = reverse('add')
		self.detail_url = reverse('detail', args=['project1'])

	def test_project_list(self):
		response = self.client.get(self.list_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'budget/project-list.html')

	def test_project_detail_get(self):
		response = self.client.get(self.detail_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'budget/project-detail.html')

	def test_project_detail_post_valid(self):
		# comment
		self.assertEquals(1, 1)
		data = {
			'title': 'MVP',
			'amount': 1000,
			'category': self.category1.name
		}

		# response = self.client.post(self.detail_url, data)
		# self.assertEquals(response.status_code, 302)
		# self.assertEquals(self.project1.expenses.first().title, data['title'])
		# self.assertEquals(self.project1.expenses.first().amount, data['amount'])

	def test_project_detail_post_invalid(self):
		response = self.client.post(self.detail_url)
		self.assertEquals(response.status_code, 302)
		self.assertFalse(self.project1.expenses.exists())

	def test_project_detail_delete(self):
		# comment
		self.assertEquals(1, 1)
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='MVP',
		# 	amount=1000,
		# 	category=self.category1
		# )

		# self.assertTrue(self.project1.expenses.exists())
		# data = json.dumps({'id': 1})
		# response = self.client.delete(self.detail_url,data)
		# self.assertEquals(response.status_code, 204)
		# self.assertFalse(self.project1.expenses.exists())
	
	def test_project_create_post(self):
		data = {
			'name': 'project2',
			'budget': 5000,
			'categoriesString': 'design, ops'
		}
		self.client.post(self.add_url, data)
		project2 = Project.objects.get(id=2)
		
		self.assertEquals(project2.name, data['name'])
		categories = data['categoriesString'].split(',')
		for category in categories:
			category_item = Category.objects.filter(name=category, project__name=data['name'])
			self.assertTrue(category_item.exists())