#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, arg):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_create(self, arg):
        """Creates a new instance.
        """
        if not arg:
            print("** class name missing **")
	    return
	try:
	    new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints instance based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
	    if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
	    instances = storage.all()

            if key in instances:
		 print(instances[key])
	    else:
                    print("** no instance found **")

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_destroy(self, arg)
        """Deletes an instance based on the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
	if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1])
	instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances of all instances of a class.
        """
	instances = storage.all()
        if not arg:
            print([str(obj) for obj in instances.values()])
	elif arg in storage.classes:
	    print([str(obj) for obj in instances.values()
                      if type(obj).__name__ == arg])
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Counts the instances of a class.
        """
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    args[0] + '.')]
            print(len(matches))

    def do_update(self, arg):
        """Updates an instance based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
	else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(instances[key], attribute, value)
                instances[key].save()
	
	def do_quit(self, arg):
            """Quit command to exit the program."""
            return True

	def do_EOF(self, arg):
            """Exit the program."""
	    print()
            return True

	def emptyline(self):
     	    """Doesn't do anything on ENTER."""
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
