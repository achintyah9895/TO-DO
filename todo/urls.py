
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('loginn/',views.loginn),
    path('todo/',views.todo),
    path('edit_todo/<int:srno>',views.edit_todo,name='edit_todo'),

    #if a url mathing the pattern, run views.delete_todo
    #pattern:capture from url int:srno, int-integer(type converter), srno -variable// srno can change but make necessary changes
    path('delete_todo/<int:srno>',views.delete_todo),
    path('sign_out/',views.sign_out, name='sign_out'),
]
