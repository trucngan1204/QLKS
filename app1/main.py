import os

from flask import render_template, request, redirect
from flask_login import login_user
from app1 import app, login, utils
from app1.models import User
import hashlib


@app.route("/")
def index():
    return render_template("index.html" )


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password","")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password.strip()).first()
        if user:
            login_user(user=user)

    return redirect("/admin")


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route("/Room")
def Room_list():
    # kw = request.args.get("kw")
    # cust_id = request.args.get("Customer _id")
    # from_price = request.args.get("from_price")
    # to_price = request.args.get("to_price")
    #
    # room = utils.read_room(cust_id=cust_id,
    #                                kw=kw,
    #                                from_price=from_price,
    #                                to_price=to_price)
    #
    # return render_template('Room-list.html',
    #                        room=room)

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    room = utils.read_room(cate_id=cate_id, kw=kw, from_price=from_price, to_price=to_price)

    return render_template('Room-list.html',
                           room = room)


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password == confirm:
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            avatar = request.files["avatar"]

            avatar_path = 'images/upload/%s' % avatar.filename
            avatar.save(os.path.join(app.root_path,
                                     'static/',
                                     avatar_path))
            if utils.add_user(name=name, email=email, username=username,
                              password=password, avatar_path=avatar_path):
                return redirect('/')
            else:
                err_msg = "Hệ thống đang có lỗi! Vui lòng quay lại sau!"
        else:
            err_msg = "Mật khẩu KHÔNG khớp!"

    return render_template('register.html', err_msg=err_msg)


if __name__ =="__main__":
    app.run(debug=True)
