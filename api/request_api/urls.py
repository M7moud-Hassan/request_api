from rest_framework_nested import routers
from .views import RequestViewSet,HeaderViewSet,BodyViewSet

router = routers.DefaultRouter()
router.register('requests', RequestViewSet, basename='requests')
request_router = routers.NestedDefaultRouter(
    router, 'requests', lookup='request')
request_router.register('headers', HeaderViewSet , basename='request-headers')
request_router.register('bodies', BodyViewSet , basename='request-bodies')
urlpatterns = router.urls+request_router.urls
