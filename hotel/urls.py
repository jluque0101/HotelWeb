from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views, forms
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
	url(r'^booking/', BookingPageView.as_view(), name='booking'),
    url(r'^gallery/', GalleryPageView.as_view(), name='gallery'),
    url(r'^contact/', ContactPageView.as_view(), name='contact'),
    url(r'^transport/', TransportPageView.as_view(), name='transport'),
    # url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    # url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    # url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    # url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    # url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    # url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    # url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    # url(r'^misc$', MiscView.as_view(), name='misc'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Development
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = media + staticfiles_urlpatterns() + urlpatterns
