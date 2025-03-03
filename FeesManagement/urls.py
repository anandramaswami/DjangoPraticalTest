"""
URL configuration for FeesManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminlogin),
    path('home',views.adminhome,name='home'),
    path('students',views.studentstable),
    path('feescategory',views.feescategorytable),
    path('delete/<int:delete_id>',views.delete_student),
    path('edit/<int:edit_id>',views.edit_student),
    path('edit/update', views.update_student, name='update'),
    path('viewstudent/<int:view_id>',views.view_student),
    path('logout/',views.adminlogout),
    path('feesupdate',views.fees_update),
    path('editfee/<int:fee_id>',views.student_fee_edit)
]
