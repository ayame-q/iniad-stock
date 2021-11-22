from importlib import import_module
from allauth.account.views import LogoutView
from allauth.socialaccount import providers
from django.urls import path

urlpatterns = [
    path("logout", LogoutView.as_view(), name="logout")
]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
