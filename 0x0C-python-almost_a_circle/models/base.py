#!/usr/bin/python3

""" Base class """


import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON. """
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_list)
        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return a list from a JSON string representation."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

# advance task 20

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV and save to a file."""
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                data = obj.to_csv()  # Define to_csv method in child classes
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file and return
                                    a list of instances."""
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data = [int(value) if i == 0 else int(value) for i,
                            value in enumerate(row)]
                    # Use create method to instantiate objects
                    instance = cls.create(*data)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list
