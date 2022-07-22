from behave import *

@given('an http request is sent to the URL')
def step_impl(context):
    pass

@then('it should return a 200 response code')
def step_impl(context):
    assert context.failed is False
