import time

from pages.elements_page import TextBoxPage, CheckBoxPage
from conftest import driver

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "Полное имя не совпадает"
            assert input_data == output_data, "Почта не совпадает"
            assert input_data == output_data, "Текущий адрес не совпадает"
            assert input_data == output_data, "Постоянный адрес не совпадает"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()