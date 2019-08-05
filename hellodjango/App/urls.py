from django.conf.urls import url
#跟路由
from App import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^hello/$',views.hello),
    url(r'^list/$',views.list_user)
]
