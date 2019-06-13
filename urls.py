from django.conf.urls import url, include
from rest_framework import routers
from back.api import views
from back.api.views import CustomObtainAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'User')
router.register(r'contact', views.ContactView, 'Contact')
# router.register(r'contact', views.ContactList, 'Contact')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),

]