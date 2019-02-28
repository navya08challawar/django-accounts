from django.conf.urls import url
from  accounts import views

app_name ='accounts'

urlpatterns =[
   url(r'^signup/$',views.signup_view,name="signup"),
   

   ]