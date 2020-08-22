from robot.libraries.BuiltIn import BuiltIn


class Base:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.sl = BuiltIn().get_library_instance('SeleniumLibrary')

    @staticmethod
    def _log(msg, level):
        BuiltIn().log(msg, level=level, html=True)

    def info(self, msg):
        self._log(msg, 'INFO')

    def warn(self, msg):
        self._log(msg, 'WARN')
