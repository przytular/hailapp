from django.conf.urls import url
from .views import MapView, SendClaimView, OpenClaimsView, \
                   CompletedClaimsView, AdjustersView, CreateAdjusterView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='map'),
    url(r'^claims/send/$', SendClaimView.as_view(), name='send_claim'),
    url(r'^claims/open/$', OpenClaimsView.as_view(), name='open_claims'),
    url(r'^claims/completed/$', CompletedClaimsView.as_view(),
                                                    name='completed_claims'),

    url(r'^adjusters/list$', AdjustersView.as_view(), name='adjusters'),
    url(r'^adjusters/new/$', CreateAdjusterView.as_view(),
                                                    name='create_adjuster'),
]
