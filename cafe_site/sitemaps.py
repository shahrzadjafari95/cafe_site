from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["cafe_site:home", "cafe_site:about", "cafe_site:contact"]

    def location(self, item):
        return reverse(item)


