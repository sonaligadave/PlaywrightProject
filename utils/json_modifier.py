
import random


class JsonModifier:

    @staticmethod
    def update_field(payload: dict, key_path: str, value):


        keys = key_path.split(".")
        ref = payload

        for key in keys[:-1]:
            if key.isdigit():
                ref = ref[int(key)]
            else:
                ref = ref[key]

        last_key = keys[-1]

        if last_key.isdigit():
            ref[int(last_key)] = value
        else:
            ref[last_key] = value

        return payload



    @staticmethod
    def generate_random_id(payload: dict):
        payload["id"] = random.randint(10000, 99999)
        return payload