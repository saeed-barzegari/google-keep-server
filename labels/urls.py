from rest_framework.routers import DefaultRouter

from labels import views

router = DefaultRouter()
router.register(r'', views.LabelViewSet, basename='label')
urlpatterns = router.urls