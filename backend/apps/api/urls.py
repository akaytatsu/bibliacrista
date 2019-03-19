from rest_framework.routers import DefaultRouter
from apps.bible.views import BibleViewSet

router = DefaultRouter()
router.register(r'bible', BibleViewSet, base_name='bible')
urlpatterns = router.urls
