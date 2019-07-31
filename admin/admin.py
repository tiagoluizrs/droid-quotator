from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()
# remove "Auth" menu's from admin
admin.site.unregister(User)
admin.site.unregister(Group)