How It Works:
Tkinter GUI: The program uses tkinter for the graphical user interface and tkcalendar to show the calendar. Users can interact with the calendar to add, view, or delete events.
Local Event Storage: Events are stored in a JSON file (events.json). Every time an event is created, updated, or deleted, the JSON file is updated, and the calendar refreshes.
User Interaction: When a user selects a date, they can either create a new event, view existing events, or delete them.


Required Dependencies:

You'll need to install tkcalendar :
run this in terminal

-- pip install tkcalendar


Explanation of Key Functions:
load_events(): Loads events from events.json when the app starts.

save_events(events): Saves the current state of events to events.json after any modifications.

add_event(date): Prompts the user for event details and saves them.

delete_event(date): Deletes an event for a specific date.

show_event(date): Displays details of an event on a specific date.

refresh_calendar(): Marks the days that have events in the calendar.

This approach gives you a full-featured dynamic calendar using just Python and local storage, all in a standalone desktop application. Let me know if you have any questions or need further adjustments
