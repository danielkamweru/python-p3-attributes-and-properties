#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Guido", job="Sales"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self.name = None

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
            self.job = None


    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self.name = new_name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, new_job):
        if new_job in APPROVED_JOBS:
            self.job = new_job
        else:
            print("Job must be in list of approved jobs.")