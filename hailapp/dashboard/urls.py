from django.conf.urls import url
from .views import MapView, SendClaimView, OpenClaimsView, \
                   CompletedClaimsView, AdjustersView, CreateAdjusterView, \
                   AdjusterProfileView, AdjusterProfileUpdateView, UpdateClaimsView, \
                   AdjusterDelete, login_view

from rest_framework.authtoken import views
from api.views import LocationUpdate, ClaimsAPI, PushIDUpdateAPI, UpdateClaimAPIView, \
                      ClaimFieldsAPI, ClaimFieldPhotoAPI

urlpatterns = [

    url(r'^accounts/login/$', login_view, name='login'),

	### VIEWS

    url(r'^$', MapView.as_view(), name='map'),
    url(r'^claims/send/$', SendClaimView.as_view(), name='send_claim'),
    url(r'^claims/open/$', OpenClaimsView.as_view(), name='open_claims'),
    url(r'^claims/completed/$', CompletedClaimsView.as_view(),
                                                    name='completed_claims'),
    url(r'^claims/update/(?P<pk>\d+)/$', UpdateClaimsView.as_view(), name='update_claim'),

    url(r'^adjusters/list$', AdjustersView.as_view(), name='adjusters'),
    url(r'^adjusters/profile/(?P<pk>\d+)/$', AdjusterProfileView.as_view(), name='show_adjuster'),
    url(r'^adjusters/profile/(?P<pk>\d+)/update/$', AdjusterProfileUpdateView.as_view(), name='update_adjuster'),
    url(r'^adjusters/new/$', CreateAdjusterView.as_view(),
                                                    name='create_adjuster'),
    url(r'^adjusters/delete/(?P<pk>\d+)/$', AdjusterDelete.as_view(),
                                                    name='delete_adjuster'),

    ### API

    url(r'^api/token-auth$', views.obtain_auth_token),
    url(r'^api/claims$', ClaimsAPI.as_view()),
    url(r'^api/claims/update/(?P<pk>\d+)$', UpdateClaimAPIView.as_view()),
    url(r'^api/pushid_update$', PushIDUpdateAPI.as_view()),
    url(r'^api/location-update$', LocationUpdate.as_view()),

    url(r'^api/claimfields/(?P<pk>\d+)$', ClaimFieldsAPI.as_view(), name='claim_fields'),
    url(r'^api/claimfields/(?P<pk>\d+)/photo/upload$', ClaimFieldPhotoAPI.as_view()),
]
