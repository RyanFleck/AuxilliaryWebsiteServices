from slugify import slugify

from services.viewcounts.models import PageViewsModel


def get_page_views(url: str):
    """Returns the number of views for a given page object."""

    # Pre-processing checks: Client should not pass full or partial URL.
    if not url.startswith("/"):
        raise Exception("Partial URL detected, only POST the page path.")
    if ("http" in url) or ("localhost" in url):
        raise Exception("Full URL detected, only POST the page path.")

    # Boil down url to slug/path:
    path = url_to_path(url)
    print(f"User is at {path}")

    # Creates a new object if none exists.
    page, created = PageViewsModel.objects.get_or_create(path=path)

    # Add a view to the model
    if not created:
        page.views = page.views + 1
        page.save()

    return page.views


def url_to_path(url: str):
    """Converts an incoming url into a path-slug."""
    return slugify(url, max_length=199)
