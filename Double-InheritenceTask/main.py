class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def display_user_info(self):
        print(f"User ID: {self.user_id}, Username: {self.username}")


class Subscriber:
    def __init__(self, subscription_id, plan, total_payment):
        self.subscription_id = subscription_id
        self.plan = plan
        self.payment = total_payment

    def subscribe(self):
        print(f"Subscriber with ID {self.subscription_id} subscribed to the {self.plan} plan")


class PremiumSubscriber(User, Subscriber):
    def __init__(self, user_id, username, subscription_id, plan, total_payment, screen):
        User.__init__(self, user_id, username)
        Subscriber.__init__(self, subscription_id, plan, total_payment)
        self.max_screen = screen

    def set_max_screens(self, screen):
        self.max_screen = screen
        print(f"Maximum screen set to {self.max_screen} in premium plan")


# Example usage
premium_user = PremiumSubscriber("123", "john_doe", "456", "monthly", 20, 4)
premium_user.display_user_info()
premium_user.subscribe()
premium_user.set_max_screens(5)
