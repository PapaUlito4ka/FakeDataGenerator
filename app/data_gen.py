import app.models as models
import random
from app.phone_gen import make_phone


class FakeUser:
    def __init__(self, name_, surname_, midname_, city_, street_):
        self.id = random.getrandbits(32)
        self.initials = f'{surname_} {name_} {midname_}'
        self.address = f'{city_}, {street_}, {random.randint(1, 50)}'
        self.telnumber = make_phone()

    def to_dict(self):
        return {
            'id': self.id,
            'initials': self.initials,
            'address': self.address,
            'telnumber': self.telnumber
        }


def gen_fake_data(seed=0):
    random.seed(seed)
    
    male_names_db = models.Name.query.with_entities(models.Name.id).filter_by(gender=0).all()
    male_surnames_db = models.Surname.query.with_entities(models.Surname.id).filter_by(gender=0).all()
    male_midnames_db = models.Midname.query.with_entities(models.Midname.id).filter_by(gender=0).all()
    female_names_db = models.Name.query.with_entities(models.Name.id).filter_by(gender=1).all()
    female_surnames_db = models.Surname.query.with_entities(models.Surname.id).filter_by(gender=1).all()
    female_midnames_db = models.Midname.query.with_entities(models.Midname.id).filter_by(gender=1).all()
    
    city_db_len = models.City.query.count()
    street_db_len = models.Street.query.count()

    while True:
        gender = random.randint(0, 1)

        if gender == 0:            
            name = models.Name.query.get(random.choice(male_names_db)).name
            surname = models.Surname.query.get(random.choice(male_surnames_db)).surname
            midname = models.Midname.query.get(random.choice(male_midnames_db)).midname
        else:
            name = models.Name.query.get(random.choice(female_names_db)).name
            surname = models.Surname.query.get(random.choice(female_surnames_db)).surname
            midname = models.Midname.query.get(random.choice(female_midnames_db)).midname

        city = models.City.query.get(random.randint(1, city_db_len)).city
        street = models.Street.query.get(random.randint(1, street_db_len)).street

        fake_user = FakeUser(
            name,
            surname,
            midname,
            city,
            street
        )
        yield fake_user
