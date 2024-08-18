import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar
import json
import os

# File to store events locally
EVENTS_FILE = "events.json"

# Function to load events from a JSON file
def load_events():
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, "r") as f:
            return json.load(f)
    return {}

# Function to save events to a JSON file
def save_events(events):
    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f, indent=4)

# Initialize events dictionary
events = load_events()

# Function to handle event creation/updating
def add_event(date):
    event_title = simpledialog.askstring("Event Title", "Enter the event title:")
    event_desc = simpledialog.askstring("Event Description", "Enter the event description:")

    if event_title:
        events[date] = {"title": event_title, "description": event_desc}
        save_events(events)
        refresh_calendar()
        messagebox.showinfo("Event Added", f"Event '{event_title}' added on {date}.")

# Function to delete an event
def delete_event(date):
    if date in events:
        del events[date]
        save_events(events)
        refresh_calendar()
        messagebox.showinfo("Event Deleted", f"Event on {date} has been deleted.")

# Function to display events on a selected date
def show_event(date):
    if date in events:
        event = events[date]
        messagebox.showinfo("Event Details", f"Title: {event['title']}\nDescription: {event['description']}")
    else:
        messagebox.showinfo("No Event", f"No events found on {date}.")

# Function to refresh the calendar display (mark days with events)
def refresh_calendar():
    for date in events:
        calendar.calevent_create(date, events[date]['title'], 'event')

# Function to handle date click in the calendar
def on_date_click(event):
    selected_date = calendar.selection_get().strftime("%Y-%m-%d")
    if selected_date in events:
        if messagebox.askyesno("Event Exists", f"Do you want to delete the event on {selected_date}?"):
            delete_event(selected_date)
        else:
            show_event(selected_date)
    else:
        add_event(selected_date)

# Set up the main window
root = tk.Tk()
root.title("Dynamic Calendar")

# Create and pack the calendar
calendar = Calendar(root, selectmode="day", date_pattern="y-mm-dd")
calendar.pack(pady=20)

# Bind date selection to the click event
calendar.bind("<<CalendarSelected>>", on_date_click)

# Refresh the calendar to display events
refresh_calendar()

# Start the Tkinter event loop
root.mainloop()
