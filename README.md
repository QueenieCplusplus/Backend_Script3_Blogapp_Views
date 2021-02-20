# Backend_Script3_Blogapp_Views
urls, views and templates

步驟 1 ~ 17, 請詳見 file 截圖。

1. 先至 app-level 的 site dir 修改 urls.py (截圖2錯誤示範，截圖4為正確示範。)

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


2. 至 blog app 下層的 views.py 修改函數 katesfun。

          from django.shortcuts import render

           # Create your views here
           # kblogs/views.py

           from django.http import HttpResponse
           from datetime import datetime

           def katesfun(request):
               #return HttpResponse("Poupou cate said hi to you :)")
               return render(request, 'show_poupou.html', {
                   'current_time': str(datetime.now()),
               })
           ~     
           
3. 至 top level site 創建 templates 資料夾， 利用 mkdir 指令與 pod 指令。 （範例：截圖 7、12） 

4. 回到 app level site 的 settings.py 手動加入 templates 路徑，溫馨提醒範例如截圖 10a。 （範例：截圖 8 ~ 10a，結構圖詳見截圖 11）       
           
5. 製作 templates called show_poupou.html for katesfun to render。

    進入結構中：
    
           (k0219) KatesAndroiddeMacBook-Pro:kblog katesandroid$ cd ..
           (k0219) KatesAndroiddeMacBook-Pro:site0219 katesandroid$ ls
           db.sqlite3	kblog		manage.py	site0219	templates
           (k0219) KatesAndroiddeMacBook-Pro:site0219 katesandroid$ cd templates
           (k0219) KatesAndroiddeMacBook-Pro:templates katesandroid$ ls
           show_poupou.html
           (k0219) KatesAndroiddeMacBook-Pro:templates katesandroid$ vim show_poupou.html

                      <!-- show_poupou.html -->

                      <!DOCTYPE html>
                      <html>
                          <head>
                              <title>here we come from PattyAppier!</title>
                              <style>
                                  body {
                                     background-color: lightyellow;
                                  }
                                  em {
                                      color: LightSeaGreen;
                                  }
                              </style>
                          </head>
                          <body>
                              <h1>Poupoucat is hungry now, show time at:</h1>
                              <em>{{ current_time }}</em>
                          </body>
                      </html>
                      ~                                                                               
                      ~                                                                               
                      ~                                                                               
                      "show_poupou.html" 20L, 431C

6. 回到 top level site 執行 python manage.py runserver。

![](https://raw.githubusercontent.com/QueenieCplusplus/Backend_Script3_Blogapp_Views/main/17.png)


ref: https://djangogirlstaipei.gitbooks.io/django-girls-taipei-tutorial/content/django/templates.html

