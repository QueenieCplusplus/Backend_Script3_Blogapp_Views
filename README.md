# Backend_Script3_Blogapp_Views
urls, views and templates

步驟 1 ~ 17, 請詳見 file 截圖。

1. 先至 app-level 的 site dir 修改 urls.py

           (k0219) KatesAndroiddeMacBook-Pro:site0219 katesandroid$ cd site0219
           (k0219) KatesAndroiddeMacBook-Pro:site0219 katesandroid$ vim urls.py
           
           
           The `urlpatterns` list routes URLs to views. For more information please see:
           
            https://docs.djangoproject.com/en/3.1/topics/http/urls/
            
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
        from django.conf.urls import include, url
        # Import view functions from blog app.
        from kblog import views


        urlpatterns = [
        
            path('admin/', admin.site.urls),
            path('', views.katesfun, name='katesfun'),
            
            #url(r'^admin/', include(admin.site.urls)),
            #url(r'^pattyappier/$', katesfun),
        ]





![](https://raw.githubusercontent.com/QueenieCplusplus/Backend_Script3_Blogapp_Views/main/17.png)


ref: https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/templates.html
