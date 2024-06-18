from django.urls import path
from addform import views
urlpatterns = [
    path('addstudents/',views.add,name="addstudents"),
    path('delete/<int:id>/',views.delete,name="delete")
]
