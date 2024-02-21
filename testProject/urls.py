"""testProject URL Configuration

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

from workers.views import *

from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

router.register(prefix=r'order', viewset=OrderView)
router.register(prefix=r'client', viewset=ClientView)
router.register(prefix=r'product', viewset=ProductView)
router.register(prefix=r'employee', viewset=EmployeeView)

router.register(prefix=r'statistics/client', viewset=ClientStatisticsView)
router.register(prefix=r'statistics/employee', viewset=EmployeeStatisticsView)

urlpatterns = [
    path('', include(router.urls)),
]
