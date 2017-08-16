from abstractFactory.AbstractFactory import AbstractFactory

factory = AbstractFactory()
benz_hatchback = factory.create_benz_factory().create_hatchback()
print(benz_hatchback.price())