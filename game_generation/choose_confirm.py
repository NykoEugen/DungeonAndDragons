class ChooseConfirm:
    @staticmethod
    def choose_confirm(ex=None):
        if ex:
            return True
        else:
            choose = input("Confirm? (Y / N): ").lower()
            if choose == "y":
                return False
            if choose == "n":
                return True
