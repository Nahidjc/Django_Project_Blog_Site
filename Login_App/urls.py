from django.urls import path
from Login_App import views
app_name = 'Login_App'


urlpatterns = [
   path('signup/',views.Sign_Up,name='sign_up'),
   path('login/',views.Login,name='login'),
   path('logout/',views.Logout,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('change_profile/',views.user_change,name='change_profile'),
   path('password/',views.pass_change,name='pass_change'),
   path('add_Pic/',views.add_pro_pic,name='add_pro_pic'),
   path('change-pic/',views.change_pro_pic,name='change_pro_pic'),
]
