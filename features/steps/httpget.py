from behave import *
import requests
from nose.tools import *
import os

@given('an http request is sent to the URL')
def step_impl(context):
    r = requests.get(os.environ['SERVER_HOST'])
    context.response = r.status_code
    pass

@then('it should return a 200 response code')
def step_impl(context):
    eq_(context.response, 200)
