from django.shortcuts import render
import time
from django.core.cache import cache


def fetch(request, data_requested):
    if cache.get(data_requested):
        data_response = cache.get(data_requested)
        comment = "from Redis Cache server"

    else:
        data_response = "Getting response for << " + data_requested + " >> "
        comment = "from DB server"
        time.sleep(10)
        cache.set(data_requested, data_response)
    return render(request, "fetch.html", context={'data': data_response+comment})
