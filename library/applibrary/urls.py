from django.urls import path
from . import views

urlpatterns = [
    path("addNewPerson/", views.add_person, name="add_person"),
    path("login/", views.sign_in, name='login'),
    path("logout/", views.sign_out, name='logout'),
    path("allBooks/", views.allBooks, name='allBooks'),
    path("lending/", views.showLending, name='lending'),
    path("lend/<int:b>", views.lend, name='lend'),
    path("return_book/<int:lend_id>", views.return_book, name='return_book'),
    path("report/", views.reports, name='reports')
]