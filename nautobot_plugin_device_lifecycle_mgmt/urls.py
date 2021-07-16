"""Django urlpatterns declaration for nautobot_plugin_device_lifecycle_mgmt plugin."""
from django.urls import path
from nautobot.extras.views import ObjectChangeLogView
from . import views
from .models import EoxNotice


urlpatterns = [
    path("", views.EoxNoticesListView.as_view(), name="devicelifecycle_list"),
    path("<uuid:pk>/", views.EoxNoticeView.as_view(), name="devicelifecycle"),
    path("add/", views.EoxNoticeCreateView.as_view(), name="devicelifecycle_add"),
    path("delete/", views.EoxNoticeBulkDeleteView.as_view(), name="devicelifecycle_bulk_delete"),
    path("edit/", views.EoxNoticeBulkEditView.as_view(), name="devicelifecycle_bulk_edit"),
    path("<uuid:pk>/delete/", views.EoxNoticeDeleteView.as_view(), name="devicelifecycle_delete"),
    path("<uuid:pk>/edit/", views.EoxNoticeEditView.as_view(), name="devicelifecycle_edit"),
    path(
        "<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="devicelifecycle_changelog",
        kwargs={"model": EoxNotice},
    ),
    path("import/", views.EoxNoticeBulkImportView.as_view(), name="devicelifecycle_import"),
]
