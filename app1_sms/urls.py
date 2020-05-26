from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as ddd


from . import api,views,views_at

router = routers.DefaultRouter()
router.register("smsonattente", api.smsonattenteViewSet)
router.register("sys_paramt", api.sys_paramtViewSet)
router.register("smstosend", api.smstosendViewSet)

urlpatterns = (
    path("test/", views.test),
    path("del_sms_to/", views_at.del_sms_to),
    path("test2/", views_at.get_sms),
    path("api/v1/", include(router.urls)),
    path("app1_sms/smsonattente/", views.smsonattenteListView.as_view(), name="app1_sms_smsonattente_list"),
    path("app1_sms/smsonattente/create/", views.smsonattenteCreateView.as_view(), name="app1_sms_smsonattente_create"),
    path("app1_sms/smsonattente/detail/<int:pk>/", views.smsonattenteDetailView.as_view(), name="app1_sms_smsonattente_detail"),
    path("app1_sms/smsonattente/update/<int:pk>/", views.smsonattenteUpdateView.as_view(), name="app1_sms_smsonattente_update"),
    path("app1_sms/sys_paramt/", views.sys_paramtListView.as_view(), name="app1_sms_sys_paramt_list"),
    path("app1_sms/sys_paramt/create/", views.sys_paramtCreateView.as_view(), name="app1_sms_sys_paramt_create"),
    path("app1_sms/sys_paramt/detail/<int:pk>/", views.sys_paramtDetailView.as_view(), name="app1_sms_sys_paramt_detail"),
    path("app1_sms/sys_paramt/update/<int:pk>/", views.sys_paramtUpdateView.as_view(), name="app1_sms_sys_paramt_update"),
    path("app1_sms/smstosend/", views.smstosendListView.as_view(), name="app1_sms_smstosend_list"),
    path("app1_sms/smstosend/create/", views.smstosendCreateView.as_view(), name="app1_sms_smstosend_create"),
    path("app1_sms/smstosend/detail/<int:pk>/", views.smstosendDetailView.as_view(), name="app1_sms_smstosend_detail"),
    path("app1_sms/smstosend/update/<int:pk>/", views.smstosendUpdateView.as_view(), name="app1_sms_smstosend_update"),
)
