from django.http import HttpResponse


class PrerenderMiddleware:
    BOT_UA = [
        "googlebot", "bingbot", "yandex", "facebookexternalhit", "twitterbot", "linkedinbot"
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ua = request.META.get("HTTP_USER_AGENT", "").lower()
        is_bot = any(bot in ua for bot in self.BOT_UA)

        if is_bot:
            import requests
            prerender_url = f"http://206.81.17.158:3000/render/{request.build_absolute_uri()}"
            try:
                response = requests.get(prerender_url, timeout=5)
                return HttpResponse(response.content, content_type="text/html")
            except:
                pass

        return self.get_response(request)
