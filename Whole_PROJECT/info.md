# Dazzla - Voice Assistant for the Visually Impaired

Dazzla is a voice assistant designed to assist visually impaired individuals by providing them with assistance and information through voice commands. Leveraging Intel's OpenVINO toolkit, Dazzla can also detect obstacles in the environment, enhancing safety and independence for users.

## Overview

Dazzla is a comprehensive voice assistant tailored specifically for the visually impaired community. It offers a range of features to facilitate daily tasks and promote accessibility.

## Key Features

- **Voice Interaction**: Users can interact with Dazzla hands-free using voice commands.
- **Weather Updates**: Real-time weather updates for a specified city help users plan their activities.
- **Wikipedia Search**: Retrieve summarized information from Wikipedia on various topics.
- **Music Playback**: Play music from a predefined directory for entertainment.
- **WhatsApp Messaging**: Send instant messages via WhatsApp to predefined contacts or numbers.
- **Health Tips**: Personalized fitness tips based on the user's health condition.
- **Obstacle Detection**: Real-time detection of obstacles in the user's environment for enhanced safety.
- **Phone Call Assistance**: Assist users in making phone calls through voice commands.

## Intel OpenVINO Integration

Dazzla leverages Intel's OpenVINO toolkit for efficient object detection, enabling it to identify obstacles and objects in the user's surroundings in real-time.

- **Object Detection**: Utilizes OpenVINO for accurate detection of obstacles.
- **Model Conversion**: Pre-trained object detection models are converted to the Intermediate Representation (IR) format using OpenVINO Model Optimizer.
- **Real-time Inference**: Performs real-time object detection using the compiled OpenVINO model, providing timely feedback to the user about detected obstacles.

## Usage

1. **Initialization**: Upon activation, Dazzla greets the user and awaits voice commands.
2. **Voice Commands**: Users can issue voice commands to perform various tasks such as retrieving information, sending messages, and detecting obstacles.
3. **Obstacle Detection**: By invoking the "detect obstacle" command, Dazzla performs real-time object detection to identify obstacles in the user's environment.
4. **Phone Call Assistance**: Users can request Dazzla to assist in making phone calls by issuing voice commands containing the phrase "phone call".

## Accessibility Features

- **Voice Feedback**: Provides auditory feedback to users, enabling interaction without the need for visual cues.
- **Hands-free Operation**: The voice-based interface allows users to operate Dazzla without manual input, enhancing accessibility for visually impaired individuals.

## Dependencies

- Python 3.x
- SpeechRecognition
- Pyttsx3
- Wikipedia API
- PyAutoGUI
- Beautiful Soup
- Requests
- OpenVINO Toolkit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dazzla-voice-assistant.git
