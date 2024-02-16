from booking import Booking
import streamlit as st


def book_flight(flight_number, passenger_name):
    flight = next((f for f in st.session_state['flights_list'] if f.flight_number == flight_number), None)
    if flight and flight.available_seats() > 0:
        flight.bookings += 1
        new_booking = Booking(flight.bookings, flight_number, passenger_name)
        st.session_state['bookings_list'].append(new_booking)
        st.success(f"Flight {flight_number} successfully booked for {passenger_name}")
        return new_booking
    else:
        st.error(f"Error while booking")
        return None


def cancel_booking(booking_id):
    pass
