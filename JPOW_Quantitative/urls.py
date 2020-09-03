from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from jpow_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home_page, name = "home"),
    url(r'^about$', views.about_page, name = "about"),
    url(r'^dashboard$', views.dashboard_home, name = "dashboard_home"),
    url(r'^logout$', views.log_out, name = "logout"),
    url(r'^retailSentiment', views.retail_sentiment, name = "retail_sentiment"),
    url(r'^insiderTrading', views.insider_trading, name = "insider_trading"),
    url(r'^ceoCompensation', views.ceo_comp, name = "ceo_comp"),
    url(r'^unusualActivity', views.options, name = "options"),
]
