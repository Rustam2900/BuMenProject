from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


# from audit_log.models.managers import AuditLog
# from simple_history.models import HistoricalRecords


class Settings(BaseModel):
    objects = models.Manager()
    email = models.EmailField()
    appstore_link = models.URLField()
    playmaket_link = models.URLField()
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_text = models.TextField(_('location_text'))
    telegram = models.CharField(max_length=70, null=True, blank=True)
    instagram = models.CharField(max_length=70, null=True, blank=True)
    linkedin = models.CharField(max_length=70, null=True, blank=True)
    facebook = models.CharField(max_length=70, null=True, blank=True)

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _("Settings")

    def __str__(self):
        return "Settings"


class Page(BaseModel):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(_("title"), max_length=255)
    content = RichTextUploadingField(_("content"))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("pages")


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    banner = models.ImageField(upload_to='common/news/%Y/%m')
    content = RichTextUploadingField()
    slug = models.SlugField(unique=True)
    top = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _("News")

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

    def __str__(self):
        return self.title


class AboutApp(BaseModel):
    caption = models.CharField(max_length=50)
    text = models.TextField()
    order = models.PositiveIntegerField()

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
    link = models.URLField()

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        verbose_name = _('Advertising')
        verbose_name_plural = _("Advertising")

    def __str__(self):
        return f"image {self.id}"


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField()

    # audit_log = AuditLog()
    # history = HistoricalRecords()

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name = _('FAQ')
        verbose_name_plural = _("FAQ")

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


class Partner(BaseModel):
    photo = models.ImageField(upload_to='common/partner/%Y/%m')
    link = models.URLField()

    class Meta:
        verbose_name = _("partner")
        verbose_name_plural = _("partners")
