from punch import views
from django.urls import path

urlpatterns = [
    path("",views.homepage),
    path("contactus",views.contactusx,name="contactus"),
    path("aboutus",views.aboutus),
    path("services",views.services,name="services"),
    path("datasave",views.savethis),



    path("delete-this/<int:dfg>",views.deletethisdata),
    path("update-this/<int:zxc>",views.updatethisdata),
    path("updatethis/<int:xmn>",views.nowupdatedata),
    path("search",views.searchthisdata,name="mysearch"),
    path("signup",views.signup,name="signup"),
    path("login",views.mylogin,name="login"),
    path("logout",views.mylogout,name="logout"),
    
]