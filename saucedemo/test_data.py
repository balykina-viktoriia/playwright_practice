class Users:
    DEFAULT_PASSWORD = "secret_sauce"
    STANDARD = {"username": "standard_user", "password": DEFAULT_PASSWORD}
    LOCKED_OUT = {"username": "locked_out_user", "password": DEFAULT_PASSWORD}
    PROBLEM = {"username": "problem_user", "password": DEFAULT_PASSWORD}

class CustomerData:
    VALID = {"first_name": "John", "last_name": "Doe", "zip_code": "12345"}

class InventoryItems:
    BACKPACK = 0
    BIKE_LIGHT = 1
    BOLT_T_SHIRT = 2
    FLEECE_JACKET = 3
    ONESIE = 4
    RED_T_SHIRT = 5


class ErrorMessages:
    LAST_NAME_REQUIRED = "Error: Last Name is required"
    LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."

class SuccessMessages:
    CHECKOUT_COMPLETE = "Thank you for your order!"