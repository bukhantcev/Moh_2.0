from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users', include('users.urls')),
    path('ajax/', include('ajax.urls')),
    path('users/', include('accounts.urls')),
    path('room/', include('room.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# http: // 127.0.0.1: 8000 / accounts / login / длявхода,
# http: // 127.0.0.1: 8000 / accounts / logout / длявыхода,
# http: // 127.0.0.1: 8000 / accounts / password - change / длясменыпароля,
# http: // 127.0.0.1: 8000 / accounts / password - reset / для сброс пароля.
#http://127.0.0.1:8000/registration/

