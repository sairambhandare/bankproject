import graphene
from graphene_django import DjangoObjectType

from bank.models import Bank, Branch


class BankType(DjangoObjectType):
    class Meta:
        model = Bank


class BranchType(DjangoObjectType):
    class Meta:
        model = Branch


class Query(graphene.ObjectType):
    branches = graphene.List(BranchType)

    def resolve_branches(self, info):  # noqa
        return Branch.objects.select_related('bank').all()


schema = graphene.Schema(query=Query)