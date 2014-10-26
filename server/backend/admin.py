from django.contrib import admin
from backend.models import Party, User


class PartyAdmin(admin.ModelAdmin):
    fields = ('tag', 'password', 'admins', 'songs')
    list_display = ('tag',)


class UserAdmin(admin.ModelAdmin):
    fields = ('session', 'party', 'upvoted_songs', 'downvoted_songs')
    list_display = ('id', 'session', 'party')

admin.site.register(Party, PartyAdmin)
admin.site.register(User, UserAdmin)