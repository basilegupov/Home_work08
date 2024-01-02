import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if isinstance(cats[0], Cat):
        return [cat._asdict() for cat in cats]
    elif isinstance(cats[0], dict):
        return [Cat(**cat) for cat in cats]


cats = [Cat(nickname='Mick', age=5, owner='Sara'),
        Cat(nickname='Barsik', age=7, owner='Olga'),
        Cat(nickname='Simon', age=3, owner='Yura')]
print(convert_list(cats))
cats = ([{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'},
         {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'},
         {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}])
print(convert_list(cats))
