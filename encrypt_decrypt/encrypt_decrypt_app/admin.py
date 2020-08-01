from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Encryption, User, Contact, CipherGame, Completed

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Extra User Information',
            {
                'fields': (
                    'score',
                    'rank',
                    'favorite_encryption',
                    'messages',
                    
                ),
            },
        ),

    )

admin.site.register(Encryption)
admin.site.register(Contact)
admin.site.register(User, CustomUserAdmin)
admin.site.register(CipherGame)
admin.site.register(Completed)
