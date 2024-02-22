from faker import Faker

fake = Faker(['en_US'])


def Name(records, ntype):
    name = []
    for i in range(records):
        if ntype == 'Full Name':
            name.append(fake.name())
        elif ntype == 'First':
            name.append(fake.name().split(" ")[0])
        else:
            name.append(fake.name().split(" ")[1])

    return name


def Phone(records):
    phone = []
    for i in range(records):
        phone.append(fake.unique.numerify('##########'))
    return phone


def Email(records):
    email = []
    for i in range(records):
        nm = fake.name().split(" ")
        email.append(nm[0] + fake.unique.numerify('###') + "@" + fake.domain_name())
    return email


def Amount(min=0, max=9999):
    return 1


def Text(lenght=10):
    return "t"


def Address():
    return "A"


def Date():
    return 'D'
