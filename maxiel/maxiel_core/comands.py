import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maxiel.settings")
import django

django.setup()
from base.models import CommandElem


def command(query_str=''):
    query_str = query_str.lower()
    command_script = CommandElem.objects.filter(command=query_str).first()
    if command_script is not None:
        command_script = command_script.script.name
        command_script_name = command_script.split('/')[len(command_script.split('/')) - 1]
        command_script_name = command_script_name.split('.')[0]
        exec(f"from media.action import {command_script_name}")
        exec(f"{command_script_name}.Plugin(query=query_str).run()")
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        command(input("command: "))
