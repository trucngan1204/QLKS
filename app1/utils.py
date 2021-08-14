import hashlib

from app1.models import *

# def read_data(path='data/room.json'):
#     with open(path, encoding='utf-8') as f:
#         return f.load()


def read_room(cate_id=None, kw=None, from_price=None, to_price=None):
    room = Room.query

    if cate_id:
        room = Room.filter(Room.category_id == cate_id)

    if kw:
        room = Room.filter(Room.name.contains(kw))

    if from_price and to_price:
        room = room.filter(Room.price.__gt__(from_price),
                                   Room.price.__lt__(to_price))

    return room.all()


def get_Room_by_id(room_id):
    # room = read_data('data/Room.json')
    return Room.query.get(room_id)

def check_login(username, password, role=UserRole.ADMIN):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    user = User.query.filter(User.username == username,
                             User.password == password,
                             User.user_role == role).first()

    return user

def get_user_by_id(user_id):
    return User.query.get(user_id)


def add_user(name, numberphone, username, password, avatar_path):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, numberphone=numberphone,
             username=username, password=password,
             avatar=avatar_path)
    try:
        db.session.add(u)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False




