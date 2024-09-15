from django.test import TestCase

from bank.models import Branch, Bank


class BankBranchTestCase(TestCase):
    def setUp(self):
        bank = Bank.objects.create(name="Test Bank")
        Branch.objects.create(bank=bank, branch="Test Branch", ifsc="TEST0001234")

    def test_branch_ifsc(self):
        branch = Branch.objects.get(ifsc="TEST0001234")
        self.assertEqual(branch.branch, "Test Branch")
