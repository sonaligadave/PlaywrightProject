import json
import os


class JsonReader:

    @staticmethod
    def read_json(file_name: str):

        base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_path, "utils/testdata", file_name)

        with open(file_path, "r") as file:
            return json.load(file)