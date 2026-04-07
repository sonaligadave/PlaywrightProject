from utils.api_client import APIClient

def test_api_ui_hybrid( api_request):

    # API Step
    api_client = APIClient(api_request)
    response_data = api_client.get_inventory()

    assert "data" in response_data
