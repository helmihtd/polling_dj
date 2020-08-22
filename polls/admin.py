from django.contrib import admin
from .models import Question, Choice

# admin site untuk mengubah tampilan dari django admin
admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.index_title = "Selamat datang di Polling administrator"

# kode ini untuk menampilkan question dan choice dalam satu halaman admin django

# masukkan choice di bawah dan tambahkan extra tabel
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# question menjadi yang utama, paling atas tampilkan question text
# tampilkan date information juga
# tampilkan itu semua dengan choice inline di bawahnya
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# dibawah ini opsional
# jika pakai kode di atas, maka question dan choice akan ditampilkan satu halaman admin django
# admin.site.register(Question)
# admin.site.register(Choice)