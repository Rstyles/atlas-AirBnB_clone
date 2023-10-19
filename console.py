#!/usr/bin/python3
"""The console for AirBnB clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg) -> bool:
        """Exit the console"""
        return True

    def do_EOF(self, arg) -> bool:
        """Exit the console"""
        return True

    def emptyline(self) -> None:
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
