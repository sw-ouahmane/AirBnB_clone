#!/usr/bin/python3
""" Module that contains class HBNBCommand """
from cmd import Cmd
from re import fullmatch


class HBNBCommand(Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_exit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Ignore empty line"""
        pass

    def do_create(self, line):
        """ create command for the program"""
        if not line:
            print("** class name missing **")
            return
        from models import classes_dict
        if line not in classes_dict:
            print("** class doesn't exist **")
            return
        model = classes_dict[line]()
        model.save()
        print(model.id)

    def do_show(self, line):
        """ show command for the program"""
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        class_name = line_split[0] if len(line_split) > 0 else None
        identifier = line_split[1] if len(line_split) > 1 else None
        if not class_name:
            print("** class name missing **")
            return
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        from models import storage
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name.strip("'\"") \
                    and obj.id == identifier.strip("'\""):
                print(str(obj))
                break
        else:
            print("** no instance found **")

    def do_all(self, line):
        """ all command for the program"""
        from models import storage, classes_dict
        res = []
        if line:
            line = line.split()[0]
            if all(line != key for key in classes_dict.keys()):
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                class_name, _ = key.split('.')
                if class_name == line:
                    res.append(str(obj))
        else:
            for key, obj in storage.all().items():
                class_name, _ = key.split('.')
                res.append(str(obj))
        print(res)

    def do_destroy(self, line):
        """ destroy command for the program"""
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        class_name = line_split[0] if len(line_split) > 0 else None
        identifier = line_split[1] if len(line_split) > 1 else None
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        if not identifier:
            print("** instance id missing **")
            return
        from models import storage
        for key, obj in storage.all().items():
            if obj.__class__.__name__ == class_name.strip("'\"") \
                    and obj.id == identifier.strip("'\""):
                storage.all().pop(key)
                storage.save()
                break
        else:
            print("** no instance found **")

    def do_update(self, line):
        """ update command for the program"""
        if not line:
            print("** class name missing **")
            return
        line_split = line.split()
        n: int = len(line_split)
        class_name = line_split[0] if n > 0 else None
        from models import classes_dict
        if all(class_name != key for key in classes_dict.keys()):
            print("** class doesn't exist **")
            return
        identifier = line_split[1] if n > 1 else None
        if not identifier:
            print("** instance id missing **")
            return
        att_name = line_split[2] if n > 2 else None
        if not att_name:
            print("** attribute name missing **")
            return
        value = line_split[3] if n > 3 else None
        if not value:
            print("** value missing **")
            return
        from models import storage
        for key, obj in storage.all().items():
            name, i = key.split(".")
            if name == class_name.strip("'\"")\
                    and i == identifier.strip('\'"'):
                setattr(obj, att_name.strip('{\'"'), value.strip(',}\'"'))
                obj.save()
                break
        else:
            print("** no instance found **")

    def do_count(self, line):
        """ count command for the program"""
        from models import storage, classes_dict
        count = 0
        if line:
            line = line.split()[0]
            if all(line != key for key in classes_dict.keys()):
                print("** class doesn't exit **")
                return
            for key, obj in storage.all().items():
                class_name, _ = key.split('.')
                if obj.__class__.__name__ == line:
                    count += 1
        else:
            count = len(storage.all())
        print(count)

    def default(self, line):
        """
        handle invalid commands and
        special commands like <class name>.<command>()
        """
        match = fullmatch(r"[A-Za-z]+\.[A-Za-z]+\(.*?\)", line)
        if match:
            split_line = line.split('.')
            from models import classes_dict
            if any(split_line[0] == key for key in classes_dict.keys()):
                parsed = split_line[1].split("(")
                args = ''
                parsed[1] = parsed[1].replace("){}:,\"", '')
                for c in parsed[1]:
                    if c in "){}:,\'\"":
                        continue
                    args += c
                args = args.split()
                commands = {"all": HBNBCommand.do_all,
                            "show": HBNBCommand.do_show,
                            "destroy": HBNBCommand.do_destroy,
                            "update": HBNBCommand.do_update,
                            "count": HBNBCommand.do_count}
                for key, command in commands.items():
                    if key == parsed[0]:
                        reconstructed_args = args.copy()
                        reconstructed_args.insert(0, split_line[0])
                        while True:
                            command(self, " ".join(reconstructed_args))
                            try:
                                reconstructed_args.pop(2)
                                reconstructed_args.pop(2)
                            except IndexError:
                                break
                            if len(reconstructed_args) <= 3:
                                break
                        break
                else:
                    print(f"*** Unknown syntax: {line}")
            else:
                print("** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
