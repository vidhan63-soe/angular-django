from django.urls import path, re_path
from EmployeeAPP import views

urlpatterns = [
    path('department/', views.departmentApi),  # For requests to /department/
    re_path(r'^department/([0-9]+)$', views.departmentApi),  # For requests to /department/123
]
