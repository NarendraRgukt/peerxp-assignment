from django.urls import path
from account import views
app_name="account"

urlpatterns=[
    path("login/token/",views.UserTokenView.as_view(),name="user-token-generation-view")
]