from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.views.decorators.csrf import ensure_csrf_cookie
from feincms3.regions import Regions
from feincms3_meta.utils import meta_tags

from juso.pages.models import Page
from juso.pages.renderer import renderer

# Create your views here.


def get_landing_page(request):
    queryset = Page.objects.active().filter(
        is_landing_page=True,
        language_code=request.LANGUAGE_CODE
    )

    if queryset.exists():
        return queryset[0]

    return get_list_or_404(
        Page.objects.active(),
        is_landing_page=True,
    )[0]

@ensure_csrf_cookie
def page_detail(request, path=None):
    if path is None and not Page.objects.active().filter(path='/').exists():
        return redirect(get_landing_page(request).path)

    page = get_object_or_404(
        Page.objects.active(),
        path=f"/{path}/" if path else '/',
    )

    if page.redirect_to_url or page.redirect_to_page:
        return redirect(page.redirect_to_url or page.redirect_to_page)

    edit = request.user.is_authenticated and\
            request.user.section_set.filter(pk=page.site.section.pk).exists()

    page.activate_language(request)
    ancestors = list(page.ancestors().reverse())
    return render(
        request,
        page.template.template_name,
        {
            "page": page,
            "edit": edit,
            "header_image": page.get_header_image(),
            "meta_tags": meta_tags([page] + ancestors, request=request),
            "regions": Regions.from_item(
                page, renderer=renderer, timeout=60,
            ),
        },
    )
