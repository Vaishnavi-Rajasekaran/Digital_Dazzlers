# Dazzla - Health and Wellness Part

The provided Python script is part of Dazzla, a voice assistant tailored to assist users, particularly focusing on health and wellness-related tasks. It allows users to receive fitness tips and reminders for exercise through voice commands.

## Key Functions

- **speak(text)**: Utilizes the pyttsx3 library to convert text into speech, enabling the voice assistant to communicate audibly with the user.
- **get_audio()**: Captures audio input from the user via a microphone using the SpeechRecognition library, recognizing spoken words and returning them as text.
- **remind_exercise()**: Prompts the user to perform exercise, emphasizing the importance of physical activity for overall health.
- **provide_fitness_tips(health_condition)**: Provides fitness tips tailored to the user's health condition, offering advice on hydration, diet, exercise, and sleep.
- **main()**: Initiates the voice assistant's operation loop, continuously listening for user commands and responding with exercise reminders or fitness tips based on user requests.

## Functionality

- **Exercise Reminder**: If the user mentions "exercise," the assistant reminds them to engage in physical activity, promoting a healthy lifestyle.
- **Fitness Tips**: When prompted, the assistant asks for the user's current health condition and provides personalized advice based on predefined categories such as normal, diabetic, or hypertensive.
- **Health and Wellness Tips**: Offers general health and wellness tips upon user request, providing guidance on both emotional and physical wellness aspects.


