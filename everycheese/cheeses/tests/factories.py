from django.template.defaultfilters import slugify
import factory
import factory.fuzzy
from ..models import Cheese

class CheeseFactory(factory.django.DjangoModelFactory):
    

    name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice([choice[0] for choice in Cheese.Firmness.choices])
    country_of_origin = factory.Faker('country_code')

    class Meta:
        model = Cheese
        abstract = False

