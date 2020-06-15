from django.urls import path
from Blog_App import views

app_name='Blog_App'

urlpatterns = [

   path('',views.BlogList.as_view(),name='blog_list'),
   path('write/',views.CreateBlog.as_view(),name='create_blog'),
   path('details/(?P<slug>[-a-zA-Z0-9_]+)/$',views.blog_details,name='blog_details'),
   path('liked/<pk>/',views.liked,name='liked_post'),
   path('unliked/<pk>/',views.Unliked,name='unliked_post'),
   path('my-blog/',views.Myblogs.as_view(),name='my_blog'),
   path('edit-blog/<pk>/',views.UpdateBlogs.as_view(),name='edit_blog'),
   path('delete/<pk>/', views.DeleteBlog.as_view(),name='delete_blog')
]
