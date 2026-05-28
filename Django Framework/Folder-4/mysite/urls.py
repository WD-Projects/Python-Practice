from django.contrib import admin
from django.urls import path

from tasks.views import sample, unknown

from tasks.views import TaskListView


urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("", sample),
    # path("u/", unknown),
    path("", TaskListView.as_view()),
]


# def add(a: int, b: int) -> int:
#     """
#     Docstring for add

#     :param a: Description
#     :type a: int
#     :param b: Description
#     :type b: int
#     :return: Description
#     :rtype: int
#     """
#     return a + b


# add(1, "Hi")


# def xyz(a: dict):
#     print(a.)
