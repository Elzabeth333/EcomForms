from django.urls import path
from .views import home , add_product, edit_product , delete_product, registration , user_login , admin_home , user_home , user_logout

urlpatterns = [
    path('', home , name = 'home'),
    path('add/', add_product , name='add_product'),
    path('edit_product/<int:product_id>/',edit_product, name='edit_product'),
    path("delete_product/<int:product_id>/",delete_product, name='delete_product'),
    path('register/', registration, name ='registration'),
    path('login/', user_login, name ='user_login'),
    path('admin_home/', admin_home, name ='admin_home'),
    path('user_home/', user_home, name ='user_home'),
    path('logout/',user_logout,name='sign_out'),
]

