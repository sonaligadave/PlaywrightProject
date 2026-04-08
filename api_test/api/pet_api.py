import requests


from config.settings import Config
class PetAPI:

    def __init__(self):
        self.base_url = Config.BASE_URL_API

    def upload_pet_image(self, pet_id: int, image_path: str):

        url = f"{self.base_url}/pet/{pet_id}/uploadImage"

        files = {
            "file": open(image_path, "rb")
        }

        headers = {
            "accept": "application/json"
        }

        response = requests.post(url, headers=headers, files=files)

        return response
    
    def get_pet_by_id(self, pet_id: int):

        url = f"{self.base_url}/pet/{pet_id}"

        headers = {
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)

        return response
    

    def create_pet(self, payload: dict):

        url = f"{self.base_url}/pet"

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=payload)

        return response


    def delete_pet(self, pet_id: int):
        return requests.delete(
            f"{self.base_url}/pet/{pet_id}",
            headers={"accept": "application/json"}
        )


    def find_pet_by_status(self, status: str):
        return requests.get(
            f"{self.base_url}/pet/findByStatus",
            headers={"accept": "application/json"},
            params={"status": status}
        )