class InvalidInput(Exception):
    def __init__(self,user_input,message="Invalid Input"):
        self.user_input=user_input
        self.message=message

    def __str__(self):
        return f'{self.user_input}->{self.message}'


