from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


# from audit_log.models.managers import AuditLog
# from simple_history.models import HistoricalRecords


class Settings(BaseModel):
    objects = models.Manager()
    email = models.EmailField()
    links = models.URLField()
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_text = models.TextField(_('location_text'))

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _("Settings")
        db_table = 'settings'

    def __str__(self):
        return "Settings"


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    banner = models.ImageField(null=True, upload_to='common/news/%Y/%m')
    content = RichTextUploadingField()
    slug = models.SlugField(unique=True, null=True)

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _("News")
        db_table = 'news'

    def __str__(self):
        return self.title


class Quotes(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('Quotes')
        verbose_name_plural = _("Quotes")
        db_table = 'quotes'

    def __str__(self):
        return self.title


class AboutApp(BaseModel):
    caption = models.CharField(max_length=50)
    text = models.TextField()
    order = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = _("ilova haqida malumotlar")
        verbose_name_plural = _("ilova haqida malumotlar")

    def save(self, *args, **kwargs):
        if self.order is None:
            order = 1
            last_about_app = AboutApp.objects.order_by('order').last()
            if last_about_app:
                order = last_about_app.order + 1
            self.order = order
        super().save(*args, **kwargs)


class Advertising(BaseModel):
    image = models.ImageField(upload_to='advertising/%Y/%m/')
    link = models.URLField(null=True)

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('Advertising')
        verbose_name_plural = _("Advertising")
        db_table = 'advertising'

    def __str__(self):
        return f"image {self.id}"


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(null=True)

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name = _('FAQ')
        verbose_name_plural = _("FAQ")
        db_table = 'faq'

    def save(self, *args, **kwargs):
        if self.order is None:
            order = 1
            last_faq = FAQ.objects.order_by('order').last()
            if last_faq:
                order = last_faq.order + 1
            self.order = order
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
