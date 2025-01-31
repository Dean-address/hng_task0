from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from datetime import datetime, timezone


class InfoView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        email = "alabikhalid.12@gmail.com"
        current_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        github_url = "https://github.com/Dean-address/hng_task0"

        return Response(
            {
                "email": email,
                "current_datetime": current_date,
                "github_url": github_url,
            }
        )
