from api_test.pet_actions import PetActions

pet_actions = PetActions()
    

def test_upload_pet_image():

    pet_actions = PetActions()

    image_path = "tests/sample_image.png"  

    response = pet_actions.upload_pet_image_and_validate(image_path)

    print("Response:", response)


def test_get_pet_details():

    response = pet_actions.get_pet_by_id_and_validate(1, True)

    print("Response:", response)


def test_get_pet_details_invalid():

    response = pet_actions.get_pet_by_id_and_validate(1000000, False)

    print("Response:", response)


def test_create_pet_from_json():


    response = pet_actions.create_pet_from_json()

    print("Pet Created:", response)


# Create Pet , make a get call to validate 
def test_create_pet_from_json_validate():


    response = pet_actions.create_pet_from_json()

    print("Pet Created:", response)

    response = pet_actions.get_pet_by_id_and_validate(int(response["id"]), True)

    print("Response:", response)

# Create Pet , make a get call to validate 
def test_delete_pet_from_json_validate():


    deleted_id = pet_actions.delete_pet_flow()

    print(f"Deleted Pet ID: {deleted_id}")

    response = pet_actions.get_pet_by_id_and_validate(deleted_id, False)

    print("Response:", response)


def test_find_pet_by_status():

    pets = pet_actions.get_pet_by_status_and_validate("sold")

    print(f"Found {len(pets)} sold pets")