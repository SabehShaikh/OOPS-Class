## single inheritence:

class subscription:
    def __init__(self, subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.payment = total_payment

    def subscribe(self):
        print(f" subscriber with {self.id} subscribed to the {self.plan} plan" )

    def unsubscribe(self):
        print(f" subscriber with {self.id} unsubscribed to the {self.plan} plan" )

    #example

# class premiumsubscription(subscription):
#     def __init__(self,subscription_id, plan, total_payment, screen):
#         self.id = subscription_id
#         self.plan = plan
#         self.payment = total_payment
#         self.max_screen = screen
#
#     def subscribe(self):
#         print(f" subscriber with {self.id} subscribed to the {self.plan} plan")
#
#     def unsubscribe(self):
#         print(f" subscriber with {self.id} unsubscribed to the {self.plan} plan")
#
#     def set_max_screens(self, screen):
#         self.max_screen = screen
#         print(f"maximum screen set to {self.max_screen} in premium plan" )
#
# netflix = premiumsubscription("122121" , "monthly" , 1,1500)
# netflix.subscribe()


## this can also be written with super() keyword:

class premiumsubscription(subscription):
    def __init__(self, subscription_id, plan, total_payment, screen):
        super().__init__(subscription_id, plan, total_payment)
        self.max_screen = screen

    def set_max_screens(self, screen):
        self.max_screen = screen
        print(f"maximum screen set to {self.max_screen} in premium plan")

netflix = premiumsubscription("122121", "monthly", 1, 1500)
netflix.subscribe()
