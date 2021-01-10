from django.urls import path
from . import views




urlpatterns = [
    
   


    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('habits/', views.habits, name="habits"),

	path('create_goal/<str:pk>/', views.goals, name="create_goal"),
    path('update_goal/<str:pk>/', views.updateGoals, name="update_goal"),
    path('delete_goal/<str:pk>/', views.deleteGoals, name="delete_goal"),

    path('create_habit/<str:pk>/', views.createHabits, name="create_habit"),
    path('update_habit/<str:pk>/', views.updateHabits, name="update_habit"),
    path('delete_habit/<str:pk>/', views.deleteHabits, name="delete_habit"),


    
    #path('create_goal/', views.createGoals, name="create_goal"),  
	
    

    path('', views.home, name="home"),

]