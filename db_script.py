from app import db
from app.models import City, Midname, Name, Street, Surname


if __name__ == '__main__':
    # City
    with open('./static/data/city_clear.txt', 'r') as f:
        for line in f.readlines():
            city = City(city=line.strip().replace('\n', ''))
            db.session.add(city)
        db.session.commit()
    # Midnames
    with open('./static/data/midnames_female_clear.txt', 'r') as f:
        for line in f.readlines():
            midname = Midname(midname=line.strip().replace('\n', ''), gender=0)
            db.session.add(midname)
        db.session.commit()
    with open('./static/data/midnames_male_clear.txt', 'r') as f:
        for line in f.readlines():
            midname = Midname(midname=line.strip().replace('\n', ''), gender=1)
            db.session.add(midname)
        db.session.commit()
    # Names
    with open('./static/data/names_female_clear.txt', 'r') as f:
        for line in f.readlines():
            name = Name(name=line.strip().replace('\n', ''), gender=0)
            db.session.add(name)
        db.session.commit()
    with open('./static/data/names_male_clear.txt', 'r') as f:
        for line in f.readlines():
            name = Name(name=line.strip().replace('\n', ''), gender=1)
            db.session.add(name)
        db.session.commit()
    # Street
    with open('./static/data/street_clear.txt', 'r') as f:
        for line in f.readlines():
            street = Street(street=line.strip().replace('\n', ''))
            db.session.add(street)
        db.session.commit()
    # Surnames
    with open('./static/data/surnames_female_clear.txt', 'r') as f:
        for line in f.readlines():
            surname = Surname(surname=line.strip().replace('\n', ''), gender=0)
            db.session.add(surname)
        db.session.commit()
    with open('./static/data/surnames_male_clear.txt', 'r') as f:
        for line in f.readlines():
            surname = Surname(surname=line.strip().replace('\n', ''), gender=1)
            db.session.add(surname)
        db.session.commit()