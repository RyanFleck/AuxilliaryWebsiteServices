import pytest

from services.viewcounts.models import PageViewsModel
from services.viewcounts.utils import get_page_views, url_to_path

pytestmark = pytest.mark.django_db


def test_get_page_views():
    # A new page should be created when this page views count is requested
    assert get_page_views("/2020/semver") == 1
    assert get_page_views("/2020/semver") == 2
    assert get_page_views("/2020/semver") == 3

    # There should be one of these models, with a correct view count.
    assert PageViewsModel.objects.filter(path="2020-semver").count() == 1
    assert PageViewsModel.objects.get(path="2020-semver").views == 3


def test_url_to_path():
    assert url_to_path("/2020/semver") == "2020-semver"

    # Partially-full url should raise exception.
    with pytest.raises(Exception):
        assert url_to_path("ryanfleck.ca/2020/semver") == "2020-semver"

    # Full URL should throw exception.
    with pytest.raises(Exception):
        assert url_to_path("https://ryanfleck.ca/2020/semver") == "2020-semver"
