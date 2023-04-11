from django.urls import path

from todo_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('delete/<int:task_id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),

    path('taliview/',views.TaskListview.as_view(),name='taliview'),
    path('detailview/<int:pk>',views.TaskDetailview.as_view(),name='detailview'),
    path('updateview/<int:pk>', views.TaskUpdateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>', views.TaskDeleteview.as_view(), name='deleteview')

]