from modeltranslation.translator import register, TranslationOptions
from common.models import Settings, AboutApp, FAQ, Page, Quotes


@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('location_text',)


@register(AboutApp)
class AboutAppTranslations(TranslationOptions):
    fields = ('caption', 'text')


@register(FAQ)
class FAQTranslations(TranslationOptions):
    fields = ('question', 'answer')


@register(Page)
class PageTranslations(TranslationOptions):
    fields = ('title', 'content')


@register(Quotes)
class QuotesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


