from home_work9_refactor.model.pages.registration_page import UserRegistrationPage
from home_work9_refactor import resources
from selene.support.shared import browser
from selene import browser


def test_registration_form():
    registration_page = UserRegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Johann')
    registration_page.fill_last_name('Bach')
    registration_page.fill_user_email('Johann@Bach.com')
    registration_page.indicate_gender()
    registration_page.user_number('4931031680')
    registration_page.fill_date_of_birth('1900', 'January', '01')
    registration_page.subject_from_dropdown('art')
    registration_page.hobbies_checkbox()
    browser.element('#uploadPicture').set_value(resources.image_file_path('organ.jpeg'))
    registration_page.fill_street('Sophienstraße 41, 99817 Eisenach, Germany')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit_form()

    registration_page.should_registered_user_with('Johann Bach', 'Johann@Bach.com', 'Male', '4931031680',
                                                  '01 January,1900', 'Arts', 'Music', 'organ.jpeg',
                                                  'Sophienstraße 41, 99817 Eisenach, Germany', 'NCR Delhi')
