#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 30, 2022
# This program calculates and displays the surface area and volume
# of a pentagonal prism using the user input of the base edge and height
# This program also asks for the unit of measurement


import math


def main():
    # Initialize Variable (that is later used to see if the user wants to run the program again)
    keep_running = True
    while keep_running:

        # Error Checking
        try:

            # Gets the user's input for the base edge, height and the unit of measurement for the pentagonal prism
            unit_of_measurement = input(
                "Enter Metric Unit of Measurement (ex. mm, cm, dm, m, hm, km): "
            )
            base_edge = float(input("Enter the measurement of the a base edge: "))
            height = float(input("Enter the height: "))

            # Calculates the Volume and Surface Area
            volume = round(
                1
                / 4
                * (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))))
                * base_edge**2
                * height,
                2,
            )
            surface_area = round(
                5 * base_edge * height
                + 1 / 2 * (math.sqrt(5 * (5 + 2 * (math.sqrt(5))))) * base_edge**2,
                2,
            )

            # Displays the Volume and Surface Area back to user
            print(
                f"\nThe Volume of the Pentagonal Prism: {volume}{unit_of_measurement}^3"
            )
            print(
                f"The Surface Area of the Pentagonal Prism: {surface_area}{unit_of_measurement}^2"
            )

            # Asks if the user wants to run the program again
            calculate_again = input(
                "Do you want to use the calculator again (enter 'y' to run again or anything else to end): "
            )
            if calculate_again != "y":
                keep_running = False

        # In the event that the user entered a letter instead of a number
        except ValueError:
            print("Please Enter a valid number!")


if __name__ == "__main__":
    main()
