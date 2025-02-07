import time
from tabnanny import check

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:

    class TestTextBox:

        @pytest.mark.skip
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            # assert input_data == output_data

            for in_data, out_data in zip(input_data, output_data):
                assert in_data == out_data, f'{in_data} mismatches {out_data}'

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, f'{input_checkbox} mismatches {output_result}\n\nCheck checkboxes'