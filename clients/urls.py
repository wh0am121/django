from django.urls import path

from . import views


app_name = "clients"
urlpatterns = [
    path("", views.index, name="index"),
    path("policyholders/", views.list_all_clients, name="list-all-clients"),
    path("policyholders/<int:pk>/", views.client_detail, name="client-detail"),
    path("policyholders/new/", views.create_client, name="create-client"),
    path("policyholders/<int:pk>/edit/", views.edit_client, name="edit-client"),
    path("policyholders/<int:pk>/delete/", views.delete_client, name="delete-client"),
    path("policyholders/<int:pk>/insurance/<int:id>/", views.insurance_detail, name="insurance-detail"),
    path("policyholders/<int:pk>/insurance/new", views.create_insurance, name="create-insurance"),
    path("policyholders/<int:pk>/insurance/<int:id>/edit", views.edit_insurance, name="edit-insurance"),
    path("policyholders/<int:pk>/insurance/<int:id>/delete", views.delete_insurance, name="delete-insurance"),
    path("policyholders/<int:pk>/insurance/<int:id>/visa", views.visa, name="visa"),
    path("policyholders/<int:pk>/insurance/<int:id>/mastercard", views.mastercard, name="mastercard"),
    path("policyholders/<int:pk>/insurance/<int:id>/kaspi", views.kaspi, name="kaspi"),
    path("policyholders/<int:pk>/insurance/<int:id>/qiwi", views.qiwi, name="qiwi"),
    path("policyholders/<int:pk>/insurance/<int:id>/payments", views.payments, name="payments"),
]