from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'services', 'product', 'methodology', 'resources', 'about', 'careers', 'contact']

    def location(self, item):
        return reverse(item)

class ServiceDetailSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['asic-verification', 'rtl-design', 'fpga-prototyping', 'functional-coverage', 'uvm-testbench', 'embedded-systems']

    def location(self, item):
        return reverse('service_detail', kwargs={'service_slug': item})

class DomainDetailSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['riscv', 'otn', 'amba', 'aerosac']

    def location(self, item):
        return reverse('domain_detail', kwargs={'domain_slug': item})
