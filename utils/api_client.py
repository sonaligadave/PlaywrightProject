from playwright.sync_api import APIRequestContext


class APIClient:

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get_pet(self):
        response = self.request.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
        print(response)
        assert response.status == 200
        return response.json()
