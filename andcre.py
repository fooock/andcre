import sys
import subprocess

from utils import *
from project import Project
from colorama import init, Fore, Style
init()


banner = """
 ____ _  _ ___  ____ ____ ____
 |__| |\ | |  \ |    |__/ |___
 |  | | \| |__/ |___ |  \ |___

"""


def set_workspace(where):
    if not where:
        where = os.getcwd()
    else:
        if check_if_exist_file(where):
            return where
        else:
            print(Fore.RED + " [-] Directory '{}' not exists!\n".format(where) + Fore.RESET)
            sys.exit()
    os.environ['ANDCRE'] = where
    return where


def apply_workspace():
    while True:
        resp = input(" [+] Do you want to apply for this session? (y/n): ")
        if resp in ('y', 'Y'):
            return True
        elif resp in ('n', 'N'):
            return False
        else:
            print(Fore.RED + " [-] Invalid option '{}'\n".format(resp) + Fore.RESET)


def set_project_name():
    while True:
        project_name = input(" [+] Project name? (ex. hello android): ")
        if not project_name:
            print(Fore.RED + " [-] The project name is not valid!\n" + Fore.RESET)
        else:
            return project_name


def set_package_name():
    while True:
        package_name = input(" [+] Package name? (ex. com.fooock.app): ")
        if not package_name:
            print(Fore.RED + " [-] Invalid package name!\n" + Fore.RESET)
        else:
            return package_name


def delete_existing_project():
    while True:
        delete = input("    [+] Delete? (y/n): ")
        if delete in ('y', 'Y'):
            return True
        elif delete in ('n', 'N'):
            return False
        else:
            print(Fore.RED + " [-] Invalid option '{}'".format(delete) + Fore.RESET)


def initialize_git_repo(current):
    os.chdir(current)
    result = subprocess.Popen(['git', 'init'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res1 = result.communicate()[0]
    subprocess.Popen(['git', 'add', '.'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    subprocess.Popen(['git', 'commit', '-m', 'First commit'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    subprocess.Popen(['git', 'tag', '-a', '0.1', '-m', 'First alpha version'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    print(Fore.MAGENTA + " [+] " + str(res1, 'utf-8') + Fore.RESET)


def main():
    print(Style.BRIGHT + Fore.BLUE + banner + Fore.RESET + Style.RESET_ALL)

    try:
        os.environ['ANDCRE']
    except KeyError:
        print(Fore.YELLOW + " ** Important: $ANDCRE environment variable not found ** " + Fore.RESET)
        if apply_workspace():
            where = input("    [+] Where? ({}): ".format(os.getcwd()))
        else:
            print(Fore.RED + " [-] Bye bye!\n" + Fore.RESET)
            sys.exit()

        workspace = set_workspace(where)
        print(Fore.GREEN + " [+] Ok! Workspace in '{}' \n".format(workspace) + Fore.RESET)

    project_name = set_project_name()
    package_name = set_package_name()

    abs_project_name = absolute_path_from(os.environ['ANDCRE'], camel_case(project_name))
    normalized_package_name = normalize_package_name(package_name)

    if check_if_exist_file(abs_project_name):
        print(Fore.YELLOW + " [+] Directory '{}' exists, do you want to delete it?".format(abs_project_name)
              + Fore.RESET)
        if delete_existing_project():
            delete_dir(abs_project_name)
            print(Fore.GREEN + " [+] Deleted '{}' folder!\n".format(abs_project_name) + Fore.RESET)
        else:
            print(Fore.RED + " [-] Don't remove old project, aborting...\n" + Fore.RESET)
            sys.exit()

    create_dir(abs_project_name)
    print(Fore.GREEN + " [+] Created '{}' directory in '{}'".format(project_name, os.environ['ANDCRE']) + Fore.RESET)

    project = Project(camel_case(project_name), normalized_package_name, abs_project_name)
    project.create_app()
    initialize_git_repo(abs_project_name)
    print(Fore.GREEN + Style.BRIGHT + " [+] Completed!\n" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
