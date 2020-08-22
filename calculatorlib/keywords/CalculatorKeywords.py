from calculatorlib.keywords.Base import Base
from robot.api.deco import keyword
from robot.utils import asserts


class CalculatorKeywords(Base):

    seven_locator = '//span[@dcg-command="7"]'

    command_locator = '//*[@dcg-command="{command}"]'

    expression_value_locator = '//div[@class="dcg-basic-expression-value"]//span[@class="dcg-mq-root-block"]'
    number_class = 'dcg-mq-digit'

    @keyword
    def clear_all(self):
        self.sl.click_element(self.command_locator.format(command='clearall'))

    @keyword
    def results_should_exist(self):
        asserts.assert_true(self.sl.find_elements(self.expression_value_locator))

    @keyword
    def results_should_be_cleared(self):
        asserts.assert_equal(0, len(self.sl.find_elements(self.expression_value_locator)))

    @keyword
    def click_seven(self):
        self.sl.click_element(self.seven_locator)

    @keyword
    def click_command(self, cmd):
        self.sl.click_element(self.command_locator.format(command=cmd))

    @keyword
    def enter_expression(self, *expressions):
        for expression in expressions:
            if expression in ['enter', 'ans']:
                self.sl.click_element(self.command_locator.format(command=expression))
            else:
                for e in expression:
                    self.sl.click_element(self.command_locator.format(command=e))

    @keyword
    def latest_result_should_be(self, expected):
        latest_result_container = self.sl.find_elements(self.expression_value_locator)[-1]
        numbers = latest_result_container.find_elements_by_tag_name('span')

        numbers = ''.join([n.text for n in numbers]).lstrip('=')

        asserts.assert_equal(expected, numbers)
