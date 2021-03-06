import re


class MobileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        mobile_agent_re = re.compile(r'.*(iphone|mobile|android)', re.IGNORECASE)

        if not mobile_agent_re.match(request.META['HTTP_USER_AGENT']):
            request.is_mobile = True

        response = self.get_response(request)

        return response
