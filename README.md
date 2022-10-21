# django_test_parameters_of_model

Module for simple test parameters of model fields. It compares values of field parameters with expected. 
It needs for avoid random changes of parameters.

# Installation

### For using:

- Download [wheel package](https://github.com/nongreen/django_test_parameters_of_fields/raw/master/dist/django_test_parameters_of_models-1.0.0-py3-none-any.whl)
- If you use virtualenv, you need select needed environment by `virtualenv local name_your_env`
- Run command `python3 -m pip install path_to_wheel_package`

### For development:

- Clone it repo by `git clone https://github.com/nongreen/django_test_parameters_of_fields`
- Change directory to tests/test_project/
- Run commands:
  - `python manage.py makemigrations`
  - `python manage.py sqlmigrate test_app 0001`
  - `python manage.py migrate`

# How to use
[Example](https://github.com/nongreen/django_test_parameters_of_fields/blob/master/docs/example.py)

- Import module by `from expected_model import expected_model`
- Create ExpectedModel with parameters of fields like dictionaries. Example `id = {"primary_key": True}`, where `id`
is name in tested model, `"primary_key"` is tested parameter, `True` is expected value of parameter
- Create test with compare ExpectedModel with TestedModel like `ExpectedModel() == TestedModel()`. <p style="color: blue">Important: compare must not to be `TestedModel() == ExpectedModel()`</p>
