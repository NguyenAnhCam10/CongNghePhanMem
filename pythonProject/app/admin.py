from app import app, db
from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.model import Category, Product, User, UserRole
from flask_login import current_user, logout_user
admin = Admin(app =app, name ='eCommerceApp', template_mode='bootstrap4')
class ProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active', 'created_date']
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    column_editable_list = ['name']
    can_export = True





class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class CategoryView(AuthenticatedView):
    column_list = ['name', 'products']

class AuthendicatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class logoutView(AuthendicatedBaseView):
    @expose("/")
    def Index(self):
        logout_user()
        return redirect('/admin')

class StatsView(AuthendicatedBaseView):
    @expose("/")
    def Index(self):
       #...
        return self.render('/admin/stats.html')
admin.add_view(CategoryView(Category, db.session))
admin.add_view(AuthenticatedView(Product, db.session))
admin.add_view(AuthenticatedView(User, db.session))
admin.add_view(logoutView(name='Đăng xuất'))
admin.add_view(StatsView(name='Thống kê'))