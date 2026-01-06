""""Q6. Design a class Vehicle that:
•	Keeps a record of service charge rate common to all vehicles.
•	Each vehicle has a model, kilometers_run, and service history.
•	Has a function to calculate service charge based on km and rate.
•	Provides a method to update the service rate for all vehicles.
•	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
1.	Creating vehicles with different km and models.
2.	Updating the service rate.
3.	Showing charges and eligibility checks.
"""
class Vehicle:
    service_charge_rate=13
    def __init__(self,model,kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history
    def service_charge(self):



