from django.urls import path
from . import views




urlpatterns = [
    
   


    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('habits/', views.habits, name="habits"),

	path('create_goal/<str:pk>/', views.goals, name="create_goal"),
    path('update_goal/<str:pk>/', views.updateGoals, name="update_goal"),
    path('delete_goal/<str:pk>/', views.deleteGoals, name="delete_goal"),


    
    #path('create_goal/', views.createGoals, name="create_goal"),  
	
    

    path('', views.home, name="home"),

]