def validate_flight_number(flight_number):
    if len(flight_number) != 5 or not flight_number.startswith("FN"):
        raise ValueError("Invalid flight number format.")
