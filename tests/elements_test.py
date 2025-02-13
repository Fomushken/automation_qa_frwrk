import random
import time

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:

    class TestTextBox:

        @pytest.mark.skip
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            for in_data, out_data in zip(input_data, output_data):
                assert in_data == out_data, f'{in_data} mismatches {out_data}'

    class TestCheckBox:
        @pytest.mark.skip
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, f'{input_checkbox} mismatches {output_result}\n\nCheck checkboxes'

    class TestRadioButton:

        @pytest.mark.skip
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', "'Yes' hasn't been selected"
            assert output_impressive == 'Impressive', "'Impressive' hasn't been selected"
            assert output_no == 'No', "'No' hasn't been selected"

        @pytest.mark.skip
        def test_random_radio_buttons(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            results = radio_button_page.click_random_radio_buttons(30)
            for result in results:
                assert result[1] == result[0], f'clicked {result[0]} received {result[1]}'

    class TestWebTable:
        @pytest.mark.skip
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            added_persons = list(web_table_page.add_new_person(random.randint(10, 40)))
            time.sleep(1)
            web_table_page.expand_maximum_rows()
            person_list_result = web_table_page.get_person_data_list()
            for added_person in added_persons:
                assert added_person in person_list_result, f'person {added_person} not in result'

        @pytest.mark.skip
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            added_person = next(web_table_page.add_new_person(1))
            search_key = added_person["first_name"]
            web_table_page.search_person(search_key)
            search_result = web_table_page.check_searched_person()
            assert len(search_result) == 1 and search_result[0] == added_person
