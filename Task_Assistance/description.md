# Dazzla - Task Assistance Part

Dazzla is a voice assistant designed to assist users with making phone calls and sending WhatsApp messages using voice commands. This README provides an overview of the script and instructions for usage.

## Overview

The provided Python script is a part of Dazzla, enabling users to interact with their phone and WhatsApp contacts through voice commands. It utilizes speech recognition and text-to-speech capabilities for seamless communication.

## Key Functions

- **make_phone_call(to_number, from_number, message)**: Initiates a phone call using Twilio's API, specifying recipient's and sender's numbers along with an optional message.
- **check_whatsapp(con_name)**: Checks if a contact name is registered and returns their WhatsApp number if found.
- **send_whatsapp_message(contact_name, message)**: Sends a WhatsApp message to a contact identified by name.
- **send_whatsapp_message_with_number(contact_num, message)**: Sends a WhatsApp message to a contact identified by number.

## Usage

1. **Initialization**: Execute the script, and Dazzla will greet the user and await voice commands.

2. **Making Phone Calls**: Say "phone call" followed by the recipient's name to initiate a phone call.

3. **Sending WhatsApp Messages by Name**: Say "send WhatsApp message to [contact name]" and provide the message content when prompted.

4. **Sending WhatsApp Messages by Number**: If the contact's name is not recognized, provide the contact's number, and the assistant will send the message to that number.

## Dependencies

- Python
- pyttsx3
- speech_recognition
- twilio
- pywhatkit
- pyautogui
