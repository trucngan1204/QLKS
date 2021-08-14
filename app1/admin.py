from app1 import admin, db
from flask_admin.contrib.sqla import ModelView
from app1.models import Customer, Receptionist, Room, Service, Statistical, Accountant, Invoice, LogoutView
from flask_login import current_user


class ReceptionistModelview(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


class StatisticalModelview(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(ModelView(Customer, db.session))
admin.add_view(ReceptionistModelview(Receptionist, db.session))
admin.add_view(ModelView(Room, db.session))
admin.add_view(ModelView(Accountant, db.session))
admin.add_view(ModelView(Invoice, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(StatisticalModelview(Statistical, db.session))
admin.add_view(LogoutView(name="Logout"))








