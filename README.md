# django_test_parameters_of_model

Module for simple test parameters of model fields. It compares values of field parameters with expected. 
It needs for avoid random changes of parameters.

# How to use

- Create ExpectedModel with parameters of fields like dictionaries. Example `id = {"primary_key": True}`, where `id`
is name in tested model, `"primary_key"` is tested parameter, `True` is expected value of parameter
- Create test with compare ExpectedModel with TestedModel like `ExpectedModel() == TestedModel()`. <p style="color: blue">Important: compare must not to be `TestedModel() == ExpectedModel()`</p>  
<br/>
More about it in `docs/example.py`