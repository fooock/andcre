import time

from utils import *


class Project(object):
    def __init__(self, name, package, absolute_path):
        self.name = name
        self.package = package
        self.abs_path = absolute_path

    def create_app(self):
        """ Create the project! """
        self.create_gradle_wrapper()
        self.create_root_files()
        self.create_build_system()
        self.create_quality()
        self.create_module()

    def create_gradle_wrapper(self):
        """ Create the project gradle wrapper """
        from_dir = os.path.join('templates', 'gradle', 'wrapper')
        copy_dir(from_this(from_dir), absolute_path_from(self.abs_path, os.path.join('gradle', 'wrapper')))

    def create_root_files(self):
        """ Create only the files that live in the root directory """
        create_file(absolute_path_from(self.abs_path, 'settings.gradle'), "include ':app'")
        create_file(absolute_path_from(self.abs_path, 'build.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'build.gradle'))))
        create_file(absolute_path_from(self.abs_path, 'README.md'), "# {}".format(self.name))
        create_file(absolute_path_from(self.abs_path, 'LICENSE.txt'), '')
        create_file(absolute_path_from(self.abs_path, '.gitignore'),
                    read_file_content(from_this(os.path.join('templates', 'gitignore'))))
        create_file(absolute_path_from(self.abs_path, 'TODO.md'), '* Add application icon')
        create_file(absolute_path_from(self.abs_path, 'CHANGELOG.md'), "* v0.1 Project started! ({})"
                    .format(time.strftime("%c")))
        create_file(absolute_path_from(self.abs_path, 'gradlew'),
                    read_file_content(from_this(os.path.join('templates', 'gradle', 'gradlew.sh'))))
        create_file(absolute_path_from(self.abs_path, 'gradlew.bat'),
                    read_file_content(from_this(os.path.join('templates', 'gradle', 'gradlew.bat'))))
        # Make files executable
        make_file_executable(absolute_path_from(self.abs_path, 'gradlew'))
        make_file_executable(absolute_path_from(self.abs_path, 'gradlew.bat'))

    def create_build_system(self):
        """ Create the build system folder with the project info, automatic version and project dependencies """
        build_folder = absolute_path_from(self.abs_path, 'buildsystem')
        create_dir(build_folder)
        create_file(absolute_path_from(build_folder, 'dependencies.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'buildsystem', 'dependencies.gradle'))))
        create_file(absolute_path_from(build_folder, 'version.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'buildsystem', 'version.gradle'))))
        create_file(absolute_path_from(build_folder, 'project.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'buildsystem', 'project.gradle'))))

    def create_quality(self):
        """ Create the quality folder with static analysis tools, lint and style checkers """
        quality_folder = absolute_path_from(self.abs_path, 'quality')
        create_dir(quality_folder)
        create_file(absolute_path_from(quality_folder, 'quality.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'quality', 'quality.gradle'))))
        create_file(absolute_path_from(quality_folder, 'jacoco.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'quality', 'jacoco.gradle'))))
        create_file(absolute_path_from(quality_folder, 'LICENSE'),
                    read_file_content(from_this(os.path.join('templates', 'quality', 'LICENSE'))))
        copy_dir(from_this(os.path.join('templates', 'quality', 'checkstyle')), absolute_path_from(quality_folder, 'checkstyle'))
        copy_dir(from_this(os.path.join('templates', 'quality', 'findbugs')), absolute_path_from(quality_folder, 'findbugs'))
        copy_dir(from_this(os.path.join('templates', 'quality', 'lint')), absolute_path_from(quality_folder, 'lint'))
        copy_dir(from_this(os.path.join('templates', 'quality', 'pmd')), absolute_path_from(quality_folder, 'pmd'))

    def create_module(self):
        """ Create the Android application module! """
        app_folder = absolute_path_from(self.abs_path, 'app')
        application_name = "{}Application".format(self.name)
        activity_name = "{}Activity".format(self.name)
        internal_pkg = internal_package(self.package)

        create_dir(absolute_path_from(app_folder, 'libs'))
        src_folder = absolute_path_from(app_folder, 'src')
        base_folder = absolute_path_from(app_folder, os.path.join('src', 'main'))
        drawable_folder = absolute_path_from(base_folder, os.path.join('res', 'drawable'))
        layout_folder = absolute_path_from(base_folder, os.path.join('res', 'layout'))
        values_folder = absolute_path_from(base_folder, os.path.join('res', 'values'))

        android_test_folder = absolute_path_from(src_folder, os.path.join('androidTest', 'java', self.package))
        test_folder = absolute_path_from(src_folder, os.path.join('test', 'java', self.package))
        debug_folder = absolute_path_from(src_folder, os.path.join('debug', 'java', self.package))
        release_folder = absolute_path_from(src_folder, os.path.join('release', 'java', self.package))
        main_folder = absolute_path_from(base_folder, os.path.join('java', self.package))

        create_dir(src_folder)
        create_dir(android_test_folder)
        create_dir(test_folder)
        create_dir(debug_folder)
        create_dir(release_folder)
        create_dir(main_folder)
        create_dir(drawable_folder)
        create_dir(layout_folder)
        create_dir(values_folder)

        create_file(absolute_path_from(app_folder, 'proguard-rules.pro'), '')
        create_file(absolute_path_from(app_folder, 'build.gradle'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'build.gradle'))) % internal_pkg)
        create_file(absolute_path_from(android_test_folder, 'ExampleInstrumentedTest.java'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'ExampleInstrumentedTest.java')))
                    % (internal_pkg, internal_pkg))
        create_file(absolute_path_from(test_folder, 'ExampleUnitTest.java'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'ExampleUnitTest.java'))) % internal_pkg)
        create_file(absolute_path_from(main_folder, "{}.java".format(application_name)),
                    read_file_content(from_this(os.path.join('templates', 'module', 'BaseApplication.java'))) % (
                        internal_pkg, application_name))
        create_file(absolute_path_from(debug_folder, 'DefaultApplication.java'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'DebugApplication.java'))) % (
                        internal_pkg, application_name))
        create_file(absolute_path_from(release_folder, 'DefaultApplication.java'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'ReleaseApplication.java'))) % (
                        internal_pkg, application_name))
        create_file(absolute_path_from(release_folder, 'CrashLibrary.java'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'CrashLibrary.java'))) % internal_pkg)
        create_file(absolute_path_from(base_folder, 'AndroidManifest.xml'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'AndroidManifest.xml'))) % (
                        internal_pkg, activity_name))
        create_file(absolute_path_from(main_folder, "{}.java".format(activity_name)),
                    read_file_content(from_this(os.path.join('templates', 'module', 'MainActivity.java'))) % (
                        internal_pkg, activity_name))
        create_file(absolute_path_from(layout_folder, 'activity_main.xml'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'activity_main.xml'))) %
                    (internal_pkg, activity_name))
        create_file(absolute_path_from(values_folder, 'strings.xml'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'strings.xml'))) % activity_name)
        create_file(absolute_path_from(values_folder, 'styles.xml'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'styles.xml'))))
        create_file(absolute_path_from(values_folder, 'colors.xml'),
                    read_file_content(from_this(os.path.join('templates', 'module', 'colors.xml'))))
