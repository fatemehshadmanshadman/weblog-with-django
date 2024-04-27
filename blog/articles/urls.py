from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="articles"
urlpatterns = [
    # path('',views.list,name="list"),
    path('create',views.create_article,name="create"), # type: ignore
    path('<slug>',views.detail,name="detail"),
]
urlpatterns+=staticfiles_urlpatterns()
