from django.contrib import admin

from .models import Chat, Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
  fields = ('text','created_at', 'author', 'receiver', 'chat')  
  list_display = ('created_at', 'author', 'text', 'receiver')    
  search_fields = ('text',)

   # Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
