from rest_framework import routers
from .api_views import  *

router = routers.DefaultRouter()
router.register("flats", FlatViewset )
router.register("agents", AgentViewset)

urlpatterns = router.urls
