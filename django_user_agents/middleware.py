from django.utils.deprecation import MiddlewareMixin  # for compatibility witih Django<1.10
from django.utils.functional import SimpleLazyObject

from .utils import get_user_agent


class UserAgentMiddleware(MiddlewareMixin):
    # A middleware that adds a "user_agent" object to request
    def process_request(self, request):
        request.user_agent = SimpleLazyObject(lambda: get_user_agent(request))
