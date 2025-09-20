from django.contrib import admin
from win32comext.mapi.mapitags import PR_PROFILE_UNRESOLVED_SERVER

from Myhealth.models import *

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
