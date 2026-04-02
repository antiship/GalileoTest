from src.base.constants import AUTO_ERROR


class AutomationError(BaseException):
    
    def __init__(self, *args, **kwargs):
        super(BaseException, self).__init__(*args, **kwargs)
        AutomationError.__init__(self, *args, **kwargs)

    def __str__(self):
        return AUTO_ERROR.format(self.args)

    def __repr__(self):
        return AUTO_ERROR.format(self.__str__())
