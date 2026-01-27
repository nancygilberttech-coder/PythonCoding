class device:
    def __init__(self, name: str):
        self.name = name

    def get_status(self):
        return "Offline"


class radio(device):
    def __init__(self, name: str):
        super().__init__(name)

    def get_status(self):
        return "Online"


my_radio = radio("Motorola-XPR")
print(my_radio.name)  # Motorola-XPR (inherited from Device)
print(my_radio.get_status())  # Online (overridden in Radio)
