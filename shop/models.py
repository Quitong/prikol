from django.db.models import CharField, DecimalField, Model, CASCADE, ForeignKey


class Category(Model):
    name = CharField(max_length=200)


class Goods(Model):
    name = CharField(max_length=200)
    cost = DecimalField(max_digits=19, decimal_places=2)
    category = ForeignKey('Category',CASCADE)

    def __str__(self):
        return 'Goods'+self.name