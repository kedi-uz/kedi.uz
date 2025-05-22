from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle, AuthRateThrottle

from apps.common.api_endpoints.views import router as common_router
from apps.book.api_endpoints.views import router as book_router

app = NinjaAPI(
    throttle=[
        AnonRateThrottle("10/s"),
        AuthRateThrottle("20/s"),
    ]
)

app.add_router("/common/", common_router)
app.add_router("/book/", book_router)
