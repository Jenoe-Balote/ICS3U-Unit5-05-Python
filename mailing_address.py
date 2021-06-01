#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: May 2021
# This program formats a proper mailing address for the user


def address_format(name, street_number, street_name, city, province,
                   postal_code, apartment_number=None):
    # This function formats the address

    address = name + "\n"
    if apartment_number is not None:
        address = address + apartment_number + "-"
    address = address + street_number + " " + street_name + "\n" \
        + city + " " + province + "  " + postal_code

    return address


def main():
    # This function gets the address information
    apartment_number_input = None

    # Input
    print("Let's format your mailing address!")
    print("")
    full_name = input("Enter your full name: ")
    apartment_question = input("Do you live in an apartment "
                               "(yes/no)?: ")
    if apartment_question == "yes":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type: ")
    city = input("Enter your city: ")
    province = input("Enter the abbreviation of your province: ")
    postal_code = input("Enter your postal code: ")

    # Call functions
    if apartment_number_input is not None:
        m_address = address_format(full_name,
                                   street_number,
                                   street_name,
                                   city,
                                   province,
                                   postal_code,
                                   apartment_number)
    else:
        m_address = address_format(full_name,
                                   street_number,
                                   street_name,
                                   city,
                                   province,
                                   postal_code)

    # Output
    print("")
    print("Your mailing address is:")
    print("")
    print(m_address.upper())
    print("\nDone.")


if __name__ == "__main__":
    main()
