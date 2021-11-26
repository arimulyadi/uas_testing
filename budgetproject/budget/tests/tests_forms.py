from django.test import SimpleTestCase
from budget.forms import ExpenseForm

class TestForms(SimpleTestCase):

	def test_expense_form_valid(self):
		data={
			'title': 'Expense1',
			'amount': 1000,
			'category': 'development'
		}
		form = ExpenseForm(data=data)
		self.assertTrue(form.is_valid())
	def test_expense_form_empty(self):
		data = {}
		form = ExpenseForm(data=data)
		self.assertFalse(form.is_valid())