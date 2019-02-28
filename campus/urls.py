from django.conf.urls import url,include
from  campus import views



app_name ='campus'
urlpatterns = [
   
   
    url(r'^campus/$',views.campus_list,name="list"),
   

   # url(r'^create/$',views.campus_create,name="create"),

    url(r'^(?P<slug>[\w-]+)/$',views.campus_details,name="detail"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),

]

