import streamlit as st

from booking_service import book_flight, cancel_booking
from flight_service import add_flight, update_flight


def show_all_flights():
    st.title("All flights:")
    for flight in st.session_state['flights_list']:
        st.write(
            f"Flight {flight.flight_number}: {flight.origin} -> {flight.destination}, time: {flight.departure_time}, "
            f"available seats: {flight.available_seats()}")


def show_all_bookings():
    st.title("All bookings:")
    for booking in st.session_state['bookings_list']:
        st.write(
            f"ID: {booking.booking_id}, Flight: {booking.flight_number}, Passenger: {booking.passenger_name}")


def form_to_add_flight():
    st.title("Add flight:")
    with st.form("new_flight_form"):
        st.write("Enter the info:")
        flight_number = st.text_input("Number")
        origin = st.text_input("Origin")
        destination = st.text_input("Destination")
        departure_time = st.text_input("time")
        capacity = st.number_input("Capasity", min_value=0, value=100, step=1)

        submitted = st.form_submit_button("Add flight")
        if submitted:
            add_flight(flight_number, origin, destination, departure_time, capacity)
        show_all_flights()


def form_to_make_booking():
    st.title("Book a flight:")
    with st.form("booking_form"):
        st.write("Enter the info:")
        flight_number = st.text_input("Flight number")
        passenger_name = st.text_input("Full name")

        submit_booking = st.form_submit_button("Book")
        if submit_booking:
            book_flight(flight_number, passenger_name)
            show_all_bookings()


def form_cancel_booking():
    st.title("Cancel booking:")
    with st.form("cancel_booking_form"):
        st.write("Enter booking id:")
        booking_id_to_cancel = st.text_input("id")

        submit_cancellation = st.form_submit_button("Cancel")
        if submit_cancellation:
            cancel_booking(booking_id_to_cancel)


def main():
    st.title("Flight Booking System")

    if 'flights_list' not in st.session_state:
        st.session_state['flights_list'] = []

    if 'bookings_list' not in st.session_state:
        st.session_state['bookings_list'] = []

    form_to_add_flight()

    flight_number_to_update = st.selectbox("Choose flight for updating:",
                                           options=[f.flight_number for f in st.session_state['flights_list']])

    if flight_number_to_update:
        update_flight(flight_number_to_update)

    form_to_make_booking()
    form_cancel_booking()


if __name__ == "__main__":
    main()
