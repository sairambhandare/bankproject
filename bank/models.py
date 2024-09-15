from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="branches")
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=70)
    state = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.branch} - {self.ifsc}"
