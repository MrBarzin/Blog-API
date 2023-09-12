from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path,include

API_TITLE = 'Blog API' # new
API_DESCRIPTION = 'A Web API for creating and editing blog posts.' # new
schema_view = get_schema_view(title=API_TITLE)
documentation = include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)

urlpatterns = [
    path('schema/',schema_view),
    path('doc/',documentation),
    path('admin/', admin.site.urls),
    path('api/v1/',include('posts.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/rest-auth/',include('dj_rest_auth.urls')),
    path('api/v1/registrations/',include('dj_rest_auth.registration.urls'))

]
