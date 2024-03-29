"""crea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crea_admin.views import ver_cliente, ver_propiedades, ver_propiedad, index, ver_empleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cliente/', ver_cliente, name="cliente"),
    path('empleado/', ver_empleado, name="empleado"),
    path('propiedades/', ver_propiedades),
    path('propiedad/<int:codigo_propiedad>/', ver_propiedad ,name="detalle_propiedad")
]
