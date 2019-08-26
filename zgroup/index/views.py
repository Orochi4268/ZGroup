from django.shortcuts import render, redirect
from django.urls import URLPattern

from zgroup import urls as root_urls


def get_all_urls(urls, prefix, result):
    for url in urls:
        part = url.pattern.regex.pattern.strip("^$")
        if isinstance(url, URLPattern):
            result.append(prefix+str(url.pattern))
        else:
            get_all_urls(url.url_patterns, prefix + part, result)
    return result


# Create your views here.
def _index(request):
    urls = get_all_urls(root_urls.urlpatterns, '/', [])
    return render(request, 'index/index.html', {'urls': urls})
