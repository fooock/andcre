import os
import shutil
import stat


def make_file_executable(file):
    st = os.stat(file)
    os.chmod(file, st.st_mode | stat.S_IEXEC)


def camel_case(name):
    return ''.join(x for x in name.title() if not x.isspace())


def check_if_exist_file(dir_name):
    return os.path.exists(dir_name)


def normalize_package_name(package_name):
    return package_name.replace('.', os.sep)


def internal_package(package):
    return package.replace(os.sep, '.')


def absolute_path_from(base, current_dir):
    return os.path.join(base, current_dir)


def create_dir(dir_name):
    os.makedirs(dir_name)


def remove_read_only(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def delete_dir(dir_name):
    shutil.rmtree(dir_name, onerror=remove_read_only)


def create_file(name, content):
    file = open(name, 'w')
    file.write(content)
    file.close()


def read_file_content(name):
    file = open(name, 'r')
    content = file.read()
    file.close()
    return content


def copy_dir(from_dir, to_dir):
    shutil.copytree(from_dir, to_dir)
