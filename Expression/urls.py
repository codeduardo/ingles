from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.show_expr,name="Expression"),
    path('/delete_expr/<int:id>',views.del_expr,name="del_expr"),
]

