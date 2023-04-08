from behave import given, when, then

@given('Skip onboarding')
def wiki_skip_onboarding(context):
    context.app.onboarding_page.click_skip()

@when('Click on search icon')
def wiki_click_search(context):
    context.app.main_page.click_search()

@when('Search for Python (programming language)')
def wiki_search_subject(context):
    context.app.main_page.input_search_phrase()

@then('Verify search result shown for Python (programming language)')
def wiki_verify_result(context):
    context.app.search_result_page.verify_search_result()