"""
Smart Energy Monitor System.
"""

import logging


def configure_logging():
    """Configure logging system."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def show_menu():
    """Display main menu."""
    print("\n===== SMART ENERGY MONITOR =====")
    print("1. View Devices")
    print("2. Update Energy Indices")
    print("3. Activate Overload Warning")
    print("4. Calculate Energy Cost")
    print("5. Exit")
    print("================================")


def show_devices(devices):
    """
    Display all devices.

    Args:
        devices (list): Device list.
    """
    if not devices:
        print("System is empty.")
        return

    print("\n{:<6} {:<25} {:<12} {:<12} {:<12}".format(
        "ID",
        "LOCATION",
        "OLD",
        "NEW",
        "STATUS"
    ))

    print("-" * 70)

    for device in devices:
        print(
            f"{device['id']:<6}"
            f"{device['location']:<25}"
            f"{device['old_index']:<12}"
            f"{device['new_index']:<12}"
            f"{device['status']:<12}"
        )


def find_device(devices, device_id):
    """
    Find device by id.

    Args:
        devices (list): Device list.
        device_id (str): Device id.

    Returns:
        dict | None
    """
    for device in devices:
        if device["id"] == device_id:
            return device

    return None


def get_valid_index(message):
    """
    Input valid index.

    Args:
        message (str): Input message.

    Returns:
        int
    """
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print(
                    "ERR-E03: Value must be >= 0."
                )
                continue

            return value

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a number."
            )


def update_indices(devices):
    """
    Update device indices.

    Args:
        devices (list): Device list.
    """
    device_id = input(
        "Enter device ID: "
    ).strip()

    device = find_device(
        devices,
        device_id
    )

    if device is None:
        print(
            "ERR-E01: Device not found."
        )
        return

    old_index = get_valid_index(
        "Enter old index: "
    )

    while True:
        new_index = get_valid_index(
            "Enter new index: "
        )

        if new_index < old_index:
            print(
                "ERR-E02: New index "
                "must be >= old index."
            )
            continue

        break

    device["old_index"] = old_index
    device["new_index"] = new_index

    logging.info(
        "Device %s updated successfully.",
        device_id
    )

    print(
        "Energy indices updated successfully."
    )


def activate_warning(devices):
    """
    Activate overload warning.

    Args:
        devices (list): Device list.
    """
    device_id = input(
        "Enter device ID: "
    ).strip()

    device = find_device(
        devices,
        device_id
    )

    if device is None:
        print(
            "ERR-E01: Device not found."
        )
        return

    if device["status"] == "Overload":
        print(
            "ERR-E04: Device already "
            "in overload state."
        )
        return

    consumption = (
        device["new_index"]
        - device["old_index"]
    )

    if consumption > 5000:
        device["status"] = "Overload"

        logging.warning(
            "Overload detected on %s",
            device_id
        )

        print(
            "Warning activated successfully."
        )

    else:
        print(
            "Device consumption "
            "does not exceed threshold."
        )


def calculate_energy_financials(devices):
    """
    Calculate energy financials.

    Args:
        devices (list): Device list.

    Returns:
        tuple:
        (
            total_consumption,
            discount_percent,
            final_cost
        )
    """
    total_consumption = sum(
        device["new_index"]
        - device["old_index"]
        for device in devices
    )

    total_cost = (
        total_consumption * 3000
    )

    discount_percent = 0

    if total_consumption >= 50000:
        discount_percent = 3

    final_cost = total_cost * (
        1 - discount_percent / 100
    )

    return (
        total_consumption,
        discount_percent,
        final_cost
    )


def display_financial_report(devices):
    """
    Display financial report.

    Args:
        devices (list): Device list.
    """
    (
        total_consumption,
        discount_percent,
        final_cost
    ) = calculate_energy_financials(
        devices
    )

    print("\n===== ENERGY REPORT =====")

    print(
        f"Total Consumption: "
        f"{total_consumption:,} kWh"
    )

    print(
        f"Discount Applied: "
        f"{discount_percent}%"
    )

    print(
        f"Final Cost: "
        f"{final_cost:,.0f} VND"
    )


def main():
    """Program entry point."""
    configure_logging()

    devices = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload"
        },
        {
            "id": "M03",
            "location": "Packaging Area",
            "old_index": 5000,
            "new_index": 60000,
            "status": "Normal"
        }
    ]

    while True:
        try:
            show_menu()

            choice = int(
                input("Select option: ")
            )

            if choice == 1:
                show_devices(devices)

            elif choice == 2:
                update_indices(devices)

            elif choice == 3:
                activate_warning(devices)

            elif choice == 4:
                display_financial_report(
                    devices
                )

            elif choice == 5:
                print(
                    "Thank you for using "
                    "Smart Energy Monitor."
                )
                break

            else:
                print(
                    "Invalid menu option."
                )

        except ValueError:
            print(
                "Please enter a number."
            )


if __name__ == "__main__":
    main()