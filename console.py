#!/usr/bin/python3
"""The console for AirBnB clone
"""
import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    available_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def emptyline(self) -> None:
        pass

    def do_create(self, arg):
        """Creates a new instance of an abject
        Usage:
            $ create <class name>
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            class_name: str = arg.split()[0]
            if class_name not in self.available_classes:
                print("** class doesn't exist **")
            else:
                obj = eval(class_name)()
                obj.save()
                print(f"{obj.id}")

    def do_show(self, arg):
        """Prints an instance of an object
        Usage:
            $ show <class name> <id>
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        for key in all_objs:
            if all_objs[key].id == args[1]:
                print(str(all_objs[key]))
                return
        print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance of an object
        Usage:
            $ destroy <class name> <id>
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** no instance found **")
            return

        all_objs = storage.all()
        for key in all_objs:
            if all_objs[key].id == args[1]:
                del all_objs[key]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """Displays all instances
        Usage:
            $ all
            $ all <class name>
        """
        args = arg.split()
        all_objs = storage.all()
        if len(args) < 1:
            for key in all_objs:
                print(str(all_objs[key]))
            return
        if args[0] not in self.available_classes:
            print("** class doesn't exist **")
            return
        for key in all_objs:
            if key.split(".")[0] == args[0]:
                print(str(all_objs[key]))
        return

    def do_update(self, arg):
        args = arg.split()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
