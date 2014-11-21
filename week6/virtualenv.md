#Virtual Environments
A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.3 while also maintaining a project which requires Django 1.0.

##virtualenv
virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Install virtualenv via pip:
```
$ pip install virtualenv
```

##Basic Usage
Create a virtual environment for a project:
```
$ cd my_project_folder
$ virtualenv venv
```
**virtualenv venv** will create a folder in the current directory which will contain the Python executable files, and a copy of the **pip** library which you can use to install other packages. The name of the virtual environment (in this case, it was **venv**) can be anything; omitting the name will place the files in the current directory instead.

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named **venv**.

You can also use a Python interpreter of your choice.
```
$ virtualenv -p /usr/bin/python2.7 venv
```
This will use the Python interpreter in **/usr/bin/python2.7**

To begin using the virtual environment, it needs to be activated:
$ source venv/bin/activate
The name of the current virtual environment will now appear on the left of the prompt (e.g. (venv)Your-Computer:your_project UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the venv folder, isolated from the global Python installation.

Install packages as usual, for example:
```
$ pip install requests
```
If you are done working in the virtual environment for the moment, you can deactivate it:
```
$ deactivate
```

This puts you back to the system’s default Python interpreter with all its installed libraries.

To delete a virtual environment, just delete its folder. (In this case, it would be rm -rf venv.)

After a while, though, you might end up with a lot of virtual environments littered across your system, and its possible you’ll forget their names or where they were placed.

##Other Notes
Running virtualenv with the option --no-site-packages will not include the packages that are installed globally. This can be useful for keeping the package list clean in case it needs to be accessed later. [This is the default behavior for virtualenv 1.7 and later.]

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run
```
$ pip freeze > requirements.txt
```
This will create a **requirements.txt** file, which contains a simple list of all the packages in the current environment, and their respective versions. Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:
```
$ pip install -r requirements.txt
```
This can help ensure consistency across installations, across deployments, and across developers.

Lastly, remember to exclude the virtual environment folder from source control by adding it to the ignore list.
