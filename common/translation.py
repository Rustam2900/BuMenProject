from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('location_text',)


@register(models.AboutApp)
class AboutAppTranslations(TranslationOptions):
    fields = ('caption', 'text')


@register(models.FAQ)
class FAQTranslations(TranslationOptions):
    fields = ('question', 'answer')
