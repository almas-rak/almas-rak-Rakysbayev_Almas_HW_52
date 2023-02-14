from django.urls import path

from to_do_list_app.views.base import index_view
from to_do_list_app.views.to_dos import add_view, detail_view

urlpatterns = [
    path("", index_view),
    path("todo/add", add_view),
    path("todo/", detail_view)

]
