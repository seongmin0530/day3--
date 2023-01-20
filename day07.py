#class_mix in

class PrettyMixin():

    def dump(self):         #특정 기능만 수행할 수 있게끔....?
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.time_print()
t.name = "kkkk"


