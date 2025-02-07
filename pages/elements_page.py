import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    """ Testing of textbox form and result that received. They must match """
    locators = TextBoxPageLocators()

    # Method uses generator to create a person, then fills the form and returns data of the person
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        button_element = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(button_element)
        button_element.click()
        return full_name, email, current_address, permanent_address

    # This method collects and returns person's data that appears after submitting the form
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    """ Testing of checkbox form and result that received. They must match """

    locators = CheckBoxPageLocators()

    # This method clicks "expand" button to show full list of checkboxes
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    # This method clicks random checkboxes 21 times
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, len(item_list)-1)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    # Collect all actually checked checkboxes using CSS selectors.
    # returns list of checkboxes as formatted string
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            item_title = box.find_element(By.XPATH, self.locators.ITEM_TITLE)
            data.append(item_title.text.lower())
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    # Collects output from the page after clicking checkboxes.
    # Returns list as formatted string
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()

class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_BUTTON,
            'impressive': self.locators.IMPRESSIVE_BUTTON,
            'no': self.locators.NO_BUTTON,
        }

        radio = self.element_is_visible(choices[choice])
        radio.click()

    def get_output_result(self):
        return self.element_is_present(self.locators.RESULT_TEXT).text

    def get_buttons_list(self):
        return self.elements_are_present(self.locators.RADIO_BUTTONS)

    def click_random_radio_button(self, buttons_list):
        random_button = buttons_list[random.randint(0, len(buttons_list)-1)]
        random_button.click()
        return random_button.text

    def click_random_radio_buttons(self, times):
        buttons_list = self.get_buttons_list()
        res = []
        for _ in range(times):
            res.append((self.click_random_radio_button(buttons_list), self.get_output_result()))
        return res

class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def click_add_button(self) -> None:
        self.element_is_visible(self.locators.ADD_BUTTON).click()

    def get_person(self) -> dict[str, str | int]:
        person_info = next(generated_person())
        first_name = person_info.first_name
        lastname = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        return {
            'first_name': first_name,
            'last_name': lastname,
            'email': email,
            'age': age,
            'salary': salary,
            'department': department,
        }

    def fill_all_fields(self, person_data) -> None:
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person_data['first_name'])
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person_data['last_name'])
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_data['email'])
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_data['age'])
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person_data['salary'])
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person_data['department'])

    def click_submit(self) -> None:
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def add_new_person(self):
        # count = random.randint(1, 40)
        count = 1
        while count != 0:
            self.click_add_button()
            person = self.get_person()
            self.fill_all_fields(person)
            self.click_submit()
            count -= 1
