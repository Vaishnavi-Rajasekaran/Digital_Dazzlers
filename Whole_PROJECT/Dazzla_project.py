# -*- coding: utf-8 -*-



from ast import main
from multiprocessing.spawn import _main
from msilib import MSIMODIFY_VALIDATE_NEW
from tkinter.tix import MAIN
from tkinter import tix as tk
import requests
import pyautogui
from bs4 import BeautifulSoup
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os,subprocess
import random
import time
import keyboard as kk
import pywhatkit as kit
from twilio.rest import Client
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak ("Good evening")
    speak("Hello i am  your Dazzla, what can i do for you")
    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        print("Say that again please...")
        return"None"
    return query

def check_whatsapp(con_name):
    whatsapp_num={
        "vaish":"9385385381","Meena":"9342764784"
    }
    if con_name in whatsapp_num:
        return (whatsapp_num[con_name])
    return "Not Found"

def send_whatsapp_message(contact_name, message):
    contact_number = check_whatsapp(contact_name)
    if contact_number != "Not Found":
        kit.sendwhatmsg_instantly(f"+91{contact_number}", message)
        time.sleep(5)
        pyautogui.press('enter')
    else:
        print("Contact not found")

def send_whatsapp_message_with_number(contact_num, message):
    kit.sendwhatmsg_instantly(f"+91{contact_num}", message)
    time.sleep(5)
    pyautogui.press('enter') 

def remind_exercise():
    speak("It's time to do some exercise. Remember to take care of your health!")

def provide_fitness_tips(health_condition):
    if health_condition == "normal":
        tips = ["Remember to stay hydrated throughout the day.", "Include a variety of fruits and vegetables in your diet.",
                "Try to get at least 30 minutes of exercise every day.", "Make sure to get enough sleep for optimal health."]
        print(tips)
        speak(tips)

    elif health_condition == "diabetic":
        tips = ["Monitor your blood sugar levels regularly.", "Follow a balanced diet with controlled carbohydrate intake.",
                "Engage in regular physical activity to help manage your blood sugar levels.",
                "Consult with your healthcare provider for personalized advice."]
        print(tips)
        speak(tips)
    elif health_condition == "hypertensive":
        tips = ["Limit your sodium intake to help control your blood pressure.", "Engage in regular aerobic exercise such as walking, swimming, or cycling.",
                "Monitor your blood pressure regularly and take medications as prescribed by your doctor.",
                "Practice stress-reduction techniques such as deep breathing or meditation."]
        print(tips)
        speak(tips)
    
    elif health_condition == "Anxiety":
        tips = ["Deep breathing can help calm the nervous system and reduce anxiety symptoms.", "Activities such as progressive muscle relaxation, visualization, or mindfulness meditation can help alleviate anxiety"]
        print(tips)
        speak(tips)

    elif health_condition == "Asthma":
        tips = ["Identify and avoid triggers such as smoke, pollen, dust mites, or pet dander that can worsen asthma symptoms",
                "Use inhalers and other medications as directed by your healthcare provider to manage asthma symptoms effectively"]
        print(tips)
        speak(tips)

    elif health_condition == "Headache":
        tips = ["Dehydration can contribute to headaches, so drink plenty of water throughout the day.",
                "Stress and tension can trigger headaches, so try techniques like deep breathing, meditation, or gentle stretching to relax."]
        print(tips)
        speak(tips)
    else:
        tips = ["Consult with a healthcare professional for personalized health advice.", "Stay informed about your health condition and follow recommended guidelines.",
                "Make healthy lifestyle choices such as eating a balanced diet and staying physically active.",
                "Listen to your body and seek medical attention if you experience any concerning symptoms."]
        print(tips)
        speak(tips)

    #tip = random.choice(tips)
    #speak("Here's a fitness tip for you: " + tip)
import urllib.request
urllib.request.urlretrieve(
    url='https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/main/notebooks/utils/notebook_utils.py',
    filename='notebook_utils.py'
)
import collections
import tarfile
import time
from pathlib import Path

import cv2
import numpy as np
from IPython import display
import openvino as ov
from openvino.tools.mo.front import tf as ov_tf_front
from openvino.tools import mo

import notebook_utils as utils
import pyttsx3

def speakk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# A directory where the model will be downloaded.
base_model_dir = Path("model")

# The name of the model from Open Model Zoo
model_name = "ssdlite_mobilenet_v2"

archive_name = Path(f"{model_name}_coco_2018_05_09.tar.gz")
model_url = f"https://storage.openvinotoolkit.org/repositories/open_model_zoo/public/2022.1/{model_name}/{archive_name}"

# Download the archive
downloaded_model_path = base_model_dir / archive_name
if not downloaded_model_path.exists():
    utils.download_file(model_url, downloaded_model_path.name, downloaded_model_path.parent)

# Unpack the model
tf_model_path = base_model_dir / archive_name.with_suffix("").stem / "frozen_inference_graph.pb"
if not tf_model_path.exists():
    with tarfile.open(downloaded_model_path) as file:
        file.extractall(base_model_dir)
        
        
precision = "FP16"
# The output path for the conversion.
converted_model_path = Path("model") / f"{model_name}_{precision.lower()}.xml"

# Convert it to IR if not previously converted
trans_config_path = Path(ov_tf_front.__file__).parent / "ssd_v2_support.json"
if not converted_model_path.exists():
    ov_model = mo.convert_model(
        tf_model_path, 
        compress_to_fp16=(precision == 'FP16'), 
        transformations_config=trans_config_path,
        tensorflow_object_detection_api_pipeline_config=tf_model_path.parent / "pipeline.config", 
        reverse_input_channels=True
    )
    ov.save_model(ov_model, converted_model_path)
    del ov_model
    
import ipywidgets as widgets

core = ov.Core()

device = widgets.Dropdown(
    options=core.available_devices + ["AUTO"],
    value='AUTO',
    description='Device:',
    disabled=False,
)

device

# Read the network and corresponding weights from a file.
model = core.read_model(model=converted_model_path)
# Compile the model for CPU (you can choose manually CPU, GPU etc.)
# or let the engine choose the best available device (AUTO).
compiled_model = core.compile_model(model=model, device_name=device.value)

# Get the input and output nodes.
input_layer = compiled_model.input(0)
output_layer = compiled_model.output(0)

# Get the input size.
height, width = list(input_layer.shape)[1:3]

# https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/
classes = [
    "background", "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train",
    "truck", "boat", "traffic light", "fire hydrant", "street sign", "stop sign",
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant",
    "bear", "zebra", "giraffe", "hat", "backpack", "umbrella", "shoe", "eye glasses",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
    "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
    "plate", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "couch", "potted plant", "bed", "mirror", "dining table", "window", "desk", "toilet",
    "door", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven",
    "toaster", "sink", "refrigerator", "blender", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush", "hair brush"
]

# Colors for the classes above (Rainbow Color Map).
colors = cv2.applyColorMap(
    src=np.arange(0, 255, 255 / len(classes), dtype=np.float32).astype(np.uint8),
    colormap=cv2.COLORMAP_RAINBOW,
).squeeze()

def process_results(frame, results, thresh=0.6):
    # The size of the original frame.
    h, w = frame.shape[:2]
    # The 'results' variable is a [1, 1, 100, 7] tensor.
    results = results.squeeze()
    boxes = []
    labels = []
    scores = []
    for _, label, score, xmin, ymin, xmax, ymax in results:
        # Create a box with pixels coordinates from the box with normalized coordinates [0,1].
        boxes.append(
            tuple(map(int, (xmin * w, ymin * h, (xmax - xmin) * w, (ymax - ymin) * h)))
        )
        labels.append(int(label))
        scores.append(float(score))

    # Apply non-maximum suppression to get rid of many overlapping entities.
    # See https://paperswithcode.com/method/non-maximum-suppression
    # This algorithm returns indices of objects to keep.
    indices = cv2.dnn.NMSBoxes(
        bboxes=boxes, scores=scores, score_threshold=thresh, nms_threshold=0.6
    )

    # If there are no boxes.
    if len(indices) == 0:
        return []

    # Filter detected objects.
    return [(labels[idx], scores[idx], boxes[idx]) for idx in indices.flatten()]

def draw_boxes(frame, boxes):
    for label, score, box in boxes:
        # Choose color for the label.
        color = tuple(map(int, colors[label]))
        # Draw a box.
        x2 = box[0] + box[2]
        y2 = box[1] + box[3]
        cv2.rectangle(img=frame, pt1=box[:2], pt2=(x2, y2), color=color, thickness=3)

        # Draw a label name inside the box.
        cv2.putText(
            img=frame,
            text=f"{classes[label]} {score:.2f}",
            org=(box[0] + 10, box[1] + 30),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=frame.shape[1] / 1000,
            color=color,
            thickness=1,
            lineType=cv2.LINE_AA,
        )

    return frame
account_sid = 'AC7b5e61ad2b4c0d1edf99e544a7413862'
auth_token = '217e5d24c2c317a14403881095a9128a'
client = Client(account_sid, auth_token)

def make_phone_call(to_number, from_number, message):
    client.calls.create(
        twiml=f'<Response><Say>{message}</Say></Response>',
        to=to_number,
        from_=from_number
    )
    


# Main processing function to run object detection.
def run_object_detection(source=0, flip=True, use_popup=False, skip_first_frames=0):
    player = None
    try:
        print("Starting run_object_detection function...")
        # Create a video player to play with target fps.
        player = utils.VideoPlayer(
            source=source, flip=flip, fps=30, skip_first_frames=skip_first_frames
        )
        print("Video player created.")
        # Start capturing.
        player.start()
        print("Video player started.")
        if use_popup:
            title = "Press ESC to Exit"
            cv2.namedWindow(
                winname=title, flags=cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_AUTOSIZE
            )

        processing_times = collections.deque()
        while True:
            # Grab the frame.
            frame = player.next()
            if frame is None:
                print("Source ended")
                break
            # If the frame is larger than full HD, reduce size to improve the performance.
            scale = 1280 / max(frame.shape)
            if scale < 1:
                frame = cv2.resize(
                    src=frame,
                    dsize=None,
                    fx=scale,
                    fy=scale,
                    interpolation=cv2.INTER_AREA,
                )

            # Resize the image and change dims to fit neural network input.
            input_img = cv2.resize(
                src=frame, dsize=(width, height), interpolation=cv2.INTER_AREA
            )
            # Create a batch of images (size = 1).
            input_img = input_img[np.newaxis, ...]

            # Measure processing time.

            start_time = time.time()
            # Get the results.
            results = compiled_model([input_img])[output_layer]
            stop_time = time.time()
            # Get poses from network results.
            boxes = process_results(frame=frame, results=results)

            # Draw boxes on a frame.
            frame = draw_boxes(frame=frame, boxes=boxes)
            
            # Convert detected objects to text
            detected_objects = [classes[label] for label, _, _ in boxes]
            detected_objects_text = ", ".join(detected_objects)
            print(detected_objects)

            processing_times.append(stop_time - start_time)
            # Use processing times from last 200 frames.
            if len(processing_times) > 200:
                processing_times.popleft()

            _, f_width = frame.shape[:2]
            # Mean processing time [ms].
            processing_time = np.mean(processing_times) * 1000
            fps = 1000 / processing_time
            cv2.putText(
                img=frame,
                text=f"Inference time: {processing_time:.1f}ms ({fps:.1f} FPS)",
                org=(20, 40),
                fontFace=cv2.FONT_HERSHEY_COMPLEX,
                fontScale=f_width / 1000,
                color=(0, 0, 255),
                thickness=1,
                lineType=cv2.LINE_AA,
            )
            # Speak detected objects
            speakk(detected_objects_text+"detected")

            # Use this workaround if there is flickering.
            if use_popup:
                cv2.imshow(winname=title, mat=frame)
                key = cv2.waitKey(1)
                # escape = 27
                if key == 27:
                    break
            else:
                # Encode numpy array to jpg.
                _, encoded_img = cv2.imencode(
                    ext=".jpg", img=frame, params=[cv2.IMWRITE_JPEG_QUALITY, 100]
                )
                # Create an IPython image.
                i = display.Image(data=encoded_img)
                # Display the image in this notebook.
                display.clear_output(wait=True)
                display.display(i)
    # ctrl-c
    except KeyboardInterrupt:
        print("Interrupted")
    # any different error
    except RuntimeError as e:
        print(e)
    finally:
        if player is not None:
            # Stop capturing.
            player.stop()
        if use_popup:
            cv2.destroyAllWindows()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "weather" in query:
          speak("Sir, which city's weather report you want")
          cty=takeCommand().lower()
          search=f"Weather in {cty}"
          url=f"https://www.google.com/search?&q={search}"
          r=requests.get(url)
          s=BeautifulSoup(r.text,"html.parser")
          update=s.find('div',class_="BNeawe").text
          print(update)
          speak(update)
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir = 'C:\Audio'
            songs = os.listdir(music_dir)
            rd = random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))
        elif 'exit' in query or 'close' in query:
                speak("Good bye see you soon")
                exit()
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'send' and 'whatsapp' in query:
            nm=query.replace("send","")
            nm=nm.replace("whatsapp","")
            nm=nm.replace("message","")
            nm=nm.replace("to","")
            nm=nm.replace("on","")
            nm=nm.replace(" ",'')
            whatsappNumber=check_whatsapp(nm)
            if whatsappNumber=="Not Found":
                print("This name is not registered on my system. Can you please tell me their number")
                speak("This name is not registered on my system. Can you please tell me their number")
                whatsappNumber=takeCommand()
                print("What do you want me to send?")
                speak("What do you want me to send?")
                message=takeCommand()
                send_whatsapp_message_with_number(whatsappNumber,message)
                speak(f"I have sent the message to {whatsappNumber}!")
                k=True
            else:
                print("What do you want me to send?")
                speak("What do you want me to send?")
                message=takeCommand()
                send_whatsapp_message(whatsappNumber,message)
                speak(f"I have sent the message to {nm}")
        elif "i drink water" in query:
            speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
            while True:
                speak("It's time to drink water. Stay hydrated!")
                time.sleep(7)  #after 7 seconds
                speak("Would you like to stop reminders or continue?")
                inputt = takeCommand().lower()
                if "stop" in inputt:
                    speak("Okay, I'll stop reminding you to drink water.")
                    break
                else:
                    speak("Great! I'll remind you to drink water an hour later. Get hydrated yourself!")
                    time.sleep(7200)
        elif "exercise" in query:
            remind_exercise()
        elif "fitness tips" in query:
            speak("What is your current health condition?")
            health_condition = takeCommand().lower()
            provide_fitness_tips(health_condition)
        elif "emotional wellness" in query:
            speak("Practice mindfulness or meditation to reduce stress and promote mental clarity.",
                "Stay connected with friends and family members for emotional support and social connection.",
                "Seek professional help if you're struggling with your mental health. Therapy and counseling can be beneficial.",
                "Practice self-care activities such as journaling, taking a bath, or going for a walk to recharge emotionally.")
        elif "physical wellness" in query:
            speak("Stay physically active by engaging in regular exercise or physical activity for at least 30 minutes a day.",
                "Eat a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.",
                "Get enough sleep each night, aiming for 7-9 hours for adults.",
                "Stay hydrated by drinking plenty of water throughout the day.")
        elif "detect obstacle" in query:
            run_object_detection()
        elif "phone call" in query:
            make_phone_call('+918072442952','+919500236467', 'Hello, Good Morning I am dazzla I am here to inform to call the user ')
            

            
