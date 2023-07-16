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
    brackets = re.search(r"\[(.*?)\]", line)
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
    """Define a new class HBNBCommand

    Attributes:
            prompt(str): the command types by the user.
    """

    prompt = "(hbnb) "
    __classes_name = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }


    def emptycommand(self):
        """handle the case of an empty line"""
        pass

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.do_count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


    def do_quit(self, line):
        """Quit command to exit the programm"""
        return True

    def do_EOF(self, line):
        """handle the end of file"""
        print("")
        return True

    def do_create(self, line):
        """create a new instance of BaseModel class"""
        args = split_command(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, line):
        """show the string represnetation of an instance bzsed
        on the class name and id"""
        args = split_command(line)
        object_dict = storage.all()
        if len(args) == 0:
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
                if len(args) > 0 and args[0] == o.__class__.__name__:
                    new_list.append(o.__str__())
                elif len(args) == 0:
                    new_list.append(o.__str__())
            print(new_list)

    def do_count(self, line):
        """ to count the instances number of any class"""
        args = split_command(line)
        c = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                c += 1
        print(c)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = split_command(line)
        object_dict = storage.all()
        if len(args) == 0:
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
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes_name:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in object_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            o = object_dict["{}.{}".format(args[0], args[1])]
            if args[2] in o.__dict__.keys():
                valtype = type(o.__dict__[args[2]])
                o.__dict__[args[2]] = valtype(args[3])
            else:
                o.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            o = object_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(o.__class__.__dict__[k])
                    o.__dict__[k] = valtype(v)
                else:
                    o.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
