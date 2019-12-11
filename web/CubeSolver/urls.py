"""CubeSolver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path    # 引入正则表达式模块 使得访问的时候忽略网址字母大小写
from cube_solver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'(?i)^cubesolver$', views.cube_solver_index),
    re_path(r'(?i)^cubesolvertest$', views.cube_solver_test_index),
    re_path(r'(?i)^cube$', views.cube_index),
    re_path(r'(?i)^deepcube$', views.deepcube_index),
    path('solver', views.solver),
    path('initState', views.initState),
    path('solve', views.solve)
]
