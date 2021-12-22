from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter()
router.register('',blogAPI,'blog')

urlpatterns = []
urlpatterns += router.urls