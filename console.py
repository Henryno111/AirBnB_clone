#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def split_command(line):
    """a function to split the input"""
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)]", line)
    if brackets is None:
        if curly_braces is None:
            return [i.strip(",") for i in split(line)]
        else:
            tokens = split(line[:brackets.span()[0]])
            token = [i.strip(",") for i in tokens]
            token.append(brackets.group())
            return (token)
    else:
        tokens = split(line[:curly_braces.span()[0]])
        token = [i.strip(",") for i in tokens]
        token.append(curly_braces.group())
        return (token)


class HBNBCommand(cmd.Cmd):
    """Define a new class HBNBCommand"""

    prompt = "(hbnb)"
    __classes_name =
    {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}


    def emptycommand(self):
        """handle the case of an empty line"""
        pass

    def do_quit(self, line):
        """command to exit the programm"""
        return True

    def do_EOF(self, line):
        """handle the end of file"""
        print("")
        return True

    def do_create(self, line):
        """create a new instance of BaseModel class"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        else:
            print(eval(line)().id)
            storage.save()

    def do_show(self, line):
        """show the string represnetation of an instance bzsed
        on the class name and id"""
        args = split_command(line)
        object_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(args[0], args[1])])

    def do_all(self, line):
        """pritns all string representation of instances
        basend on class name"""
        args = split_command(line)
        object_dict = storage.all()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        else:
            new_list = []
            for o in object_dict.values():
                new_list.append(o.__str__())
            print(new_list)


    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = split_command(line)
        object_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object_dict.keys():
            print("** no instance found **")
        else:
            del object_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def update(self, line):
        """update the instance based on class name and the id"""
        args = split_command(line)
        object_dict = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in object_dict.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        if len(args) == 4:
            o = object_dict["{}.{}".format(args[0], args[1])]
            if args[2] in o.__dict__.keys():
                valtype = type(o.__dict__[args[2]])
                o.__dict__[args[2]] = valtype(args[3])
            else:
                o.__dict__[args[2]] = args[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
