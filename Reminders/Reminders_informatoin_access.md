# Dazzla - Reminders and Information Access part

This Python script is a voice-activated assistant program that performs various tasks based on voice commands. It provides convenience and assistance by performing tasks such as searching Wikipedia, retrieving weather updates, telling the current time, and setting up water drinking reminders through voice commands.

## Components

### Imported Libraries


- `datetime`: For handling date and time.
- `wikipedia`: Provides access to Wikipedia's content.
- `requests`: Used for making HTTP requests.
- `BeautifulSoup`: For parsing HTML content.


### Main Execution

- The program starts by wishing the user.
- It continuously listens to the user's voice commands in a loop.
- It performs various actions based on the recognized commands:
  - Searches Wikipedia for information if the command contains "Wikipedia".
  - Retrieves weather updates for a specified city if the command contains "weather".
  - Tells the current time if the command contains "current time".
  - Sets up reminders to drink water every 2 hours if the command contains "I drink water".
  - Stops the water drinking reminders if the command contains "stop".

