from django.urls import path

from task_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path("dash/", views.dash, name="dash"),
    path('user_register/', views.user_register, name='user_register'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('create_task/', views.create_task, name='create_task'),
    path('view_my_tasks/',views.view_my_tasks,name='view_my_tasks'),
    path('view_all_tasks/', views.view_all_tasks, name='view_all_tasks'),
    path('update_task/<int:id>/', views.update_task, name='update_task'),
    path('delete_task/<int:id>/',views.delete_task,name='delete_task'),
    path('mark_task_complete/<int:id>/',views.mark_task_complete,name='mark_task_complete'),
    path('mark_task_not_completed/<int:id>/',views.mark_task_not_completed,name='mark_task_not_completed')

]