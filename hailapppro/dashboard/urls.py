from django.conf.urls import url
from .views import MapView, SendClaimView, OpenClaimsView, \
                   CompletedClaimsView, AdjustersView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='map'),
    url(r'^send/$', SendClaimView.as_view(), name='send_claim'),
    url(r'^open/$', OpenClaimsView.as_view(), name='open_claims'),
    url(r'^completed/$', CompletedClaimsView.as_view(), name='completed_claims'),
    url(r'^adjusters/$', AdjustersView.as_view(), name='adjusters'),
]
