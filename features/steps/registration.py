from behave import *
import logging


@given(u'I have a valid registration link')
def step_impl(context):
    context.link = context.valid_link


@given(u'I have an invalid registration link')
def step_impl(context):
    context.link = context.invalid_link


@when("I visit the link")
def step_impl(context):
    logging.info('STEP: I visit the link')
    logging.info(f'Link => {context.link}')
    context.browser.get(context.link)


@then("I can see the form page")
def step_impl(context):
    print(f'context.browser.current_url = {context.browser.current_url}')
    print(f'context.portal_base_url + "/sites/12345" = {context.portal_base_url + "/sites/12345"}')
    assert context.browser.current_url == context.portal_base_url + "/sites/12345"


@step("I see the provider's stock form")
def step_impl(context):
    print(f'context.browser.title = {context.browser.title}')
    print(f'context.valid_provider_name + " | Site Form" = {context.valid_provider_name + " | Site Form"}')
    assert context.browser.title == context.valid_provider_name + " | Site FormT"


@step("I see that I am denied access")
def step_impl(context):
    assert 'You may need permission to access this service' in context.browser.page_source
