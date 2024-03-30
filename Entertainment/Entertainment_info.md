## Dazzla - Entertainment part

## Description:

The Python script presented here is a part of Dazzla, a voice assistant designed to assist visually impaired individuals by providing them with various functionalities through voice commands. The script includes features for playing music and audiobooks.

- **Wish Functionality**: Upon execution, the assistant greets the user based on the time of the day and introduces itself.
  
- **Voice Recognition**: Utilizes the SpeechRecognition library to recognize voice commands spoken by the user.

- **Music Playback**: Responds to voice commands to play music stored in the specified directory. It randomly selects a music file and plays it using the default media player.

- **Audiobook Playback**: Similar to the music playback functionality, this feature allows the user to play audiobooks stored in a specific directory. It selects a random audiobook file and starts playing it.

- **Speech Synthesis**: Employs the pyttsx3 library to provide audible responses and feedback to the user's commands.

## Functionality:

1. **Greeting**: Upon running the script, the voice assistant wishes the user based on the time of the day (Good Morning/Good Afternoon/Good Evening) and introduces itself as Dazzla.

2. **Listening for Commands**: The assistant listens for voice commands from the user, utilizing the microphone as the input source.

3. **Music Playback**: If the user says "play music", the assistant randomly selects a music file from the specified directory and starts playing it using the default media player.

4. **Audiobook Playback**: If the user says "play books", the assistant randomly selects an audiobook file from the specified directory and begins playing it.

## Dependencies:

- Python 3.x
- SpeechRecognition
- pyttsx3

