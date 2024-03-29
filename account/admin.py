from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account



class AccountAdmin(UserAdmin):
	list_display = ('first_name','username', 'email')
	search_fields = ('first_name','username', 'email')
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)