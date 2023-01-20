# 10. 9
class Bear:
    def eats(self):
        return 'berries, (Bear)'


class Rabbit:
    def eats(self):
        return 'clover, (Rabbit)'


class Octothorpe:

    def eats(self):
        return 'campers, (Octothorpe)'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())