# andcre

[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-andcre-green.svg?style=flat-square)](https://android-arsenal.com/details/1/6058)

Andcre (android creator) is a python script to create professional and ready to use Android projects.

![](https://github.com/fooock/andcre/blob/master/media/andcre_project.png) "Project created with andcre"

## Requirements
andcre works with `python3`

## Getting started
First clone this repo
```sh
$ git clone https://github.com/fooock/andcre.git
$ cd andcre
```
Now install the dependencies
```sh
$ pip3 install -r requirements.txt
```
Create the environment variable **ANDCRE** to point to your android workspace.
This is where the projects will be created.
```sh
$ export ANDCRE=/home/user/AndroidProjects
```
If the environment variable is not found, the program will request it every time a new project is created

Execute the script or set the `andcre.bat` or `andcre` to the `$PATH` to execute this program from any place!

## Features
andcre create android projects with a lot of useful files and tools. It include support for android lint, findbugs, checkstyle and pmd. Automatically create a git repo, add all project files, commit and create the first tag.

### Project files
* Create automatically a `README.md` file, that contains the project name.
* Create a `CHANGELOG.md` file and automatically write the name of the current version
and the current date
* Create the `TODO.md` file
* Create `LICENSE` file
* Create the `.gitignore` file with the common android ignored files/directories
* Create the root `build.gradle` file

### Build system
The andcre script create a folder in the root project directory called `buildsystem`.
It contains three files:
* `dependencies.gradle`: Contains the dependencies of the project (test dependencies and
application dependencies)
* `version.gradle`: Contain all things related to the project version
* `project.gradle`: Project properties like target sdk, build tools version etc

The `version.gradle` file is based in [this great post from Dmytro Danylyk on hackernoon](https://hackernoon.com/configuring-android-project-version-name-code-b168952f3323)

### Gradle wrapper
The gradle version used is the `gradle-4.3.1`

### Quality tools
In the project root, a directory called `quality` is created. It contains all files needed to execute the static analysis tools and style checkers like findbugs, checkstyle, pmd and android lint. To generate all these reports execute
```sh
$ ./gradlew check
```
Note that if you add more modules to the project, this task is applied. The reports are generated in the `<project>/app/build/reports` directory

All quality files [are from this fantastic repo!](https://github.com/Piasy/AndroidCodeQualityConfig)

### App debug options
The application create a custom `DefaultApplication` for the `debug` builds and initialize for default custom configurations not needed in application releases. The debug options are:
* Initialize `Timber` with the `Timber.DebugTree()`
* Detect all kind of problems and log it using the `StrictMode.setThreadPolicy()` and `StrictMode.setVmPolicy` methods.
* Setup `LeakCanary`. Only compile in `debugCompile` (see app/build.gradle) 
* Initialize the default values for `Stetho`

**Note**: This configuration **only** applies to debug builds! 

### Git
When the project is created a new git repository is initialized. You can use the gradle task `printVersion` to check out it.

### App module
For default the `AndroidManifest.xml` has the `INTERNET` permission. For each build type (debug/release) a `DefaultApplication` is created with different log configurations.
* For the **debug** type a `Timber.DebugTree()` is initialized.
* For the **release** type a custom `CrashReportingTree()` is created. This tree discards automatically all `DEBUG` and `VERBOSE` logs, and can be able to report all errors and warnings using the `CrashLibrary` class

The applicatiod id for the debug build type has the `.debug` suffix.

### Apk generation
All apk's are generated in the `build/outputs/apk` directory. The name of the apk correspond to the project name with the current version. For example, your module name is `app`, and the version is `0.1`, the resulting apk's will be:
* For the `debug` build type: `app-0.1-debug.apk`
* For the `release` build type: `app-0.1-release.apk`

### Include open source notices
The `play-services-oss-licenses` library is included to show the list of licenses used by the libraries included in the application. To show the list you only need to call the code:

```java
final Intent intent = new Intent(this, OssLicensesMenuActivity.class);
startActivity(intent);
```
You can change the activity title. For more info see [the documentation](https://developers.google.com/android/guides/opensource)

## Final Android project
The result project structure is like this:

![](https://github.com/fooock/andcre/blob/master/media/img1.png)

![](https://github.com/fooock/andcre/blob/master/media/img2.png)

![](https://github.com/fooock/andcre/blob/master/media/img3.png)

### Suggestions
Open an [issue](https://github.com/fooock/andcre/issues) or create a new [pull request](https://github.com/fooock/andcre/pulls)

### License
```
Copyright 2017 newhouse (nhitbh at gmail dot com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```