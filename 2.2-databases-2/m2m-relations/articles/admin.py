from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_exist = False
        count_is_main = 0
        for form in self.forms:
            try:
                if form.cleaned_data['tag']:
                    tag_exist = True
            except KeyError:
                pass
            try:
                if form.cleaned_data['is_main'] is True:
                    count_is_main += 1
            except KeyError:
                pass
            if tag_exist is False:
                raise ValidationError('Не выбран ни один раздел')
            elif count_is_main < 1:
                raise ValidationError('Не выбран главный раздел')
            elif count_is_main > 1:
                raise ValidationError('Главный раздел может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
