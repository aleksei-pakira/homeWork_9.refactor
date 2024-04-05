from selene import browser, be, command, have


class UserRegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def indicate_gender(self):
        browser.element('#gender-radio-1').perform(command.js.click).should(be.selected)
        return self

    def user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def subject_from_dropdown(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('[id="react-select-2-option-0"]').click()   # choose element from dropdown
        return self

    def hobbies_checkbox(self):
        browser.element('#hobbies-checkbox-3').perform(command.js.click).should(be.selected)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_street(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit_form(self):
        browser.element('button#submit').click()
        return self

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                                    address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_and_city,
            )
        )
        return self
