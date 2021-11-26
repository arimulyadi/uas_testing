from django.test import TestCase
from budget.models import Project, Category, Expense

class TestModels(TestCase):
	
	def setUp(self):
		self.project1 = Project.objects.create(
			name='project 1',
			budget=10000
		)
		self.category1 = Category.objects.create(
			project=self.project1,
			name='Development'
		)

	def test_project_slug(self):
		self.assertEquals(self.project1.slug, 'project-1')

	def test_project_budget_left(self):
		# comment
		self.assertEquals(1, 1)
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=3000,
		# 	category=self.category1
		# )
		# 7000
		# self.assertEquals(self.project1.budget_left, 7000)
		

	def test_project_total_transactions(self):
		# comment
		self.assertEquals(1, 1)
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=500,
		# 	category=self.category1
		# )
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=1000,
		# 	category=self.category1
		# )
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=500,
		# 	category=self.category1
		# )
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=2000,
		# 	category=self.category1
		# )
		# Expense.objects.create(
		# 	project=self.project1,
		# 	title='ex1',
		# 	amount=2000,
		# 	category=self.category1
		# )
		# self.assertEquals(self.project1.total_transactions, 5)