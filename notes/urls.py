from rest_framework.routers import DefaultRouter

from notes import views

router = DefaultRouter()
router.register(r'', views.NoteViewSet, basename='note')
urlpatterns = router.urls
