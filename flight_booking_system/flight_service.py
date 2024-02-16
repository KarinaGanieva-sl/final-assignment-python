from flight import Flight
import streamlit as st


def add_flight(flight_number, origin, destination, departure_time, capacity):
    if flight_number and origin and destination and departure_time and capacity:
        new_flight = Flight(flight_number, origin, destination, departure_time, capacity)
        st.session_state['flights_list'].append(new_flight)
        st.success("Success!")


def update_flight(flight_number):
    flight = next((f for f in st.session_state['flights_list'] if f.flight_number == flight_number), None)
    if flight is not None:
        with st.form(f"form_{flight_number}"):
            origin = st.text_input("Origin", value=flight.origin)
            destination = st.text_input("Destination", value=flight.destination)
            departure_time = st.text_input("Time", value=flight.departure_time)
            capacity = st.number_input("Capacity", value=flight.capacity, step=1)

            submitted = st.form_submit_button("Update flight")
            if submitted:
                flight.origin = origin
                flight.destination = destination
                flight.departure_time = departure_time
                flight.capacity = capacity
                st.success(f"Flight {flight_number} updated!")
    else:
        st.error(f"Flight {flight_number} not found.")
