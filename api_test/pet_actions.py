
# from api_test.api import PetAPI
from api_test.api.pet_api import PetAPI
from utils.data_generator import DataGenerator
import json

from utils.json_modifier import JsonModifier
from utils.json_reader import JsonReader

class PetActions:

    def __init__(self):
        self.pet_api = PetAPI()

    def upload_pet_image_and_validate(self, image_path: str):

        # Generate dynamic pet id
        pet_id = DataGenerator.generate_pet_id()

     
        response = self.pet_api.upload_pet_image(pet_id, image_path)

        assert response.status_code == 200, \
                f"Expected 200 but got {response.status_code}"

        response_json = response.json()

        assert response_json["code"] == 200

            # print( response.json())
            
        assert "File uploaded" in response_json["message"]

        return response_json
    

    def get_pet_by_id_and_validate(self, pet_id, valid):
     
        response = self.pet_api.get_pet_by_id(pet_id)

        response_json = response.json()
        
        if valid:
            assert response.status_code == 200, \
                f"Expected 200 but got {response.status_code}"
            
            assert response_json["id"] == pet_id

            assert response_json["name"] != None

            
        else:
            assert response.status_code == 404, \
                f"Expected 404 but got {response.status_code}"    
            
            assert response_json["type"] == "error"
            
            assert "Pet not found" in response_json["message"]

        print(response_json)

        return response_json
    

    def create_pet_from_json(self):

    
        payload = JsonReader.read_json("create_pet.json")


        payload = JsonModifier.generate_random_id(payload)
        payload = JsonModifier.update_field(payload, "name", "automation_dog")
        payload = JsonModifier.update_field(payload, "category.name", "Automation Dogs")
        payload = JsonModifier.update_field(payload, "tags.0.name", "api_test")

   
        response = self.pet_api.create_pet(payload)


        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

        response_json = response.json()

        assert response_json["id"] == payload["id"]
        assert response_json["name"] == "automation_dog"
        assert response_json["category"]["name"] == "Automation Dogs"
        assert response_json["tags"][0]["name"] == "api_test"

        return response_json
    

    def delete_pet_flow(self):

        # Step 1: Create pet first (so we have valid ID)
        payload = JsonReader.read_json("create_pet.json")
        payload = JsonModifier.generate_random_id(payload)

        create_response = self.pet_api.create_pet(payload)
        assert create_response.status_code == 200

        pet_id = payload["id"]

        # Step 2: Delete pet
        delete_response = self.pet_api.delete_pet(pet_id)

        assert delete_response.status_code == 200
        assert delete_response.json()["message"] == str(pet_id)

        return pet_id


    def get_pet_by_status_and_validate(self, status="sold"):

        response = self.pet_api.find_pet_by_status(status)

        assert response.status_code == 200

        response_json = response.json()

        assert isinstance(response_json, list)

        if len(response_json) > 0:
            for pet in response_json:
                assert pet["status"] == status

        return response_json