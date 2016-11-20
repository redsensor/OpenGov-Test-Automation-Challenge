# Weppy - web testing framework with page objects implementation. 
Easily automate your website testing automation process. Just replace website link, locators, put your own assertions and have fun :)
___
Language used: **Python 2.7**

**Unittest** used as testing framework, **nose** as test runner.

Tests use ChromeDriver, please make sure it is installed. Otherwise change it to Firefox in ```seleniumwrapper/SeleniumWrapper.py```.

All the requirements can be pulled and installed from ```requirements.txt``` file using ```virtualenv```.

To run test go to core/tests folder and execute them. 
You can also run all tests from folder using unittest, just execute ```python -m unittest discover <test_directory>```.

