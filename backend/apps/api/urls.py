from rest_framework.routers import DefaultRouter
from apps.biblia.views import BibliaViewSet

router = DefaultRouter()
router.register(r'biblia', BibliaViewSet, base_name='biblia')
urlpatterns = router.urls
