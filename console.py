#!/usr/bin/python3
""" Import different modules """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def do_EOF(self, line):
        """This methods triggers EOF to exit the program."""
        return True

    def do_quit(self, line):
        """This methods uses 'quit' to exit the program."""
        return True

    def do_create(self, line):
        """This method creates a new instance of BaseModel and
        saves it to json file.
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")

        else:
            if args[0] in self.classes:
                new_instance = self.classes[args[0]]()
                storage.new(new_instance)
                storage.save()
                print(new_instance.id)

            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """This method prints the string representation
        of an instance based on the class name and id."""

        args = line.split()
        if len(args) < 1:
            print("** class name missing **")

        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = args[0] + "." + args[1]
            if key not in storage._FileStorage__objects:
                print("** no instance found **")
            else:
                print(storage._FileStorage__objects[key])

    def do_destroy(self, line):
        """This method deletes an instance based on the class name and id."""

        args = line.split()
        if len(args) < 1:
            print("** class name missing **")

        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = args[0] + "." + args[1]
            if key not in storage._FileStorage__objects:
                print("** no instance found **")
            else:
                del storage._FileStorage__objects[key]
                storage.save()

    def do_all(self, line):
        """This method prints all string representation of
        all instances based or not on the class name."""

        args = line.split()
        if len(args) <= 1:
            for value in storage._FileStorage__objects.values():
                print(str(value))

        elif args[1] not in self.classes.keys():
            print("** class doesn't exist **")

        else:
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == args[1]:
                    print(str(value))

    def do_update(self, line):
        """This method updates an instance based on the class name and id
        by adding or updating attribute
        and saves the change into the JSON file."""

        args = line.split()
        if len(args) < 1:
            print("** class name missing **")

        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            key = args[0] + "." + args[1]
            if key not in storage._FileStorage__objects:
                print("** no instance found **")

            else:
                newAttributes = storage._FileStorage__objects[key]
                if hasattr(newAttributes, args[2]):
                    attr_type = type(getattr(newAttributes, args[2]))
                else:
                    attr_type = type(args[3])
                setattr(newAttributes, args[2], attr_type(args[3]))
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
