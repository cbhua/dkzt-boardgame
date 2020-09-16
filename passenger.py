

class Passenger:
    object = []
    profession_checked = []
    association_checked = []
    actived_profession = False

    def __init__(self, association, profession, object):
        self.association = association
        self.profession = profession
        self.object.append(object)

    def num_object(self):
        return len(self.object)

    def add_object(self, object):
        self.object.append(object)

    def lost_object(self, object):
        self.object.remove(object)

    def active_profession(self):
        self.profession.active()

    def check_profession(self, passenger_num):
        self.profession_checked.append(passenger_num)

    def check_association(self, passenger_num):
        self.association_checked.append(passenger_num)

    def print_object(self):
        print("objects")