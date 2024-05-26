

# !pip install twelvelabs
import streamlit as st
from twelvelabs import TwelveLabs
client = TwelveLabs(api_key=st.secrets['TWELVE_API']))

!python -m pip install requests
headers = {
    "x-api-key": st.secrets['TWELVE_API'])
}
INDEXES_URL = f"{https://dashboard.twelvelabs.io/home}/indexes"

# !pip install twelvelabs
from twelvelabs import TwelveLabs
client = TwelveLabs(api_key=st.secrets['TWELVE_API']))

headers = {
    "x-api-key": st.secrets['TWELVE_API'])
}
INDEXES_URL = f"https://dashboard.twelvelabs.io/home/indexes"
response = requests.get(INDEXES_URL, headers=headers)
st.write(response.text)

# !pip install twelvelabs
from twelvelabs import TwelveLabs
client = TwelveLabs(api_key=st.secrets['TWELVE_API'])

headers = {
    "x-api-key": st.secrets['TWELVE_API']
}
INDEXES_URL = f"https://dashboard.twelvelabs.io/home/indexes"

# !python -m pip install requests
headers = {
    "x-api-key": st.secrets['TWELVE_API']
}

INDEXES_URL = f"https://dashboard.twelvelabs.io/home/indexes"

import requests



# # Install the requests module
# !pip install requests

# Import the requests module
import requests

# Define the INDEX_NAME and data variables
INDEX_NAME = "<memomind>"
data = {
    "engines": [
      {
        "engine_name": "marengo2.6",
        "engine_options":  ["visual", "conversation", "text_in_video", "logo"]
      }
    ],
    "index_name": INDEX_NAME,
}

# Set the INDEXES_URL and headers variables
INDEXES_URL = f"https://dashboard.twelvelabs.io/home/indexes"
headers = {
    "x-api-key": st.secrets['TWELVE_API'])
}

# Send the POST request to create the index
response = requests.post(INDEXES_URL, headers=headers, json=data)

# st.write the status code and response
st.write (f'Status code: {response.status_code}')
st.write (response.json())

if response.status_code == 405:
    st.write("Error: The server returned a 405 (Method Not Allowed) error.")
    st.write("Please check if you have the correct permissions to create an index.")
else:
    st.write(response.json())

import logging

logging.basicConfig(level=logging.DEBUG)

# ...

response = requests.post(INDEXES_URL, headers=headers, json=data)

from twelvelabs import TwelveLabs

client = TwelveLabs(api_key=st.secrets['TWELVE_API']))

engines = [
        {
          "name": "marengo2.6",
          "options": ["visual", "conversation", "text_in_video", "logo"]
        }
  ]

engines = [
        {
            "name": "pegasus1",
            "options": ["visual", "conversation"]
        }
    ]

engines = [
        {
            "name": "pegasus1",
            "options": ["visual", "conversation"]
        },
        {
          "name": "marengo2.6",
          "options": ["visual", "conversation", "text_in_video", "logo"]
        }
    ]

index = client.index.create(
    name="<YOUR_INDEX_NAME>",
    engines=engines,
    addons=["thumbnail"] # Optional
)
st.write(f"A new index has been created: id={index.id} name={index.name} engines={index.engines}")





from twelvelabs import TwelveLabs
from twelvelabs.models.task import Task

client = TwelveLabs(api_key=st.secrets['TWELVE_API']))

import streamlit as st
import cv2
from tempfile import NamedTemporaryFile

# Function to convert BytesIO to a temporary file
def convert_bytes_to_temp_file(file):
    with NamedTemporaryFile(delete=False, suffix=".mp4") as temp:
        temp.write(file.read())
        temp.flush()
        return temp.name

# Create a file uploader widget for video files
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mpeg"])

if uploaded_file is not None:
    
    
    task = client.task.create(
      index_id="6652c2d127f0a43b740fd8bb",
      file="/content/WhatsApp Video 2024-05-26 at 10.44.25.mp4",
    )
    st.write(f"Task id={task.id}")
    
    # Utility function to st.write the status of a video indexing task
    def on_task_update(task: Task):
          st.write(f"  Status={task.status}")
    
    task.wait_for_done(sleep_interval=5, callback=on_task_update)
    
    if task.status != "ready":
      raise RuntimeError(f"Indexing failed with status {task.status}")
    st.write(f"The unique identifer of your video is {task.video_id}.")
    
    from twelvelabs import TwelveLabs
    
    client = TwelveLabs(api_key=st.secrets['TWELVE_API']))
    
    gist = client.generate.gist(
      video_id="6652c6b4d22b3a3c97bef629",
      types=["title","topic","hashtag"]
    )
    st.write(f"Title={gist.title}\nTopic={gist.topics}\nHashtags={gist.hashtags}")
    
    from twelvelabs import TwelveLabs
    
    client = TwelveLabs(api_key=st.secrets['TWELVE_API']))
    
    res = client.generate.text(
      video_id="/content/WhatsApp Video 2024-05-26 at 10.44.25.mp4",
      prompt="I want to generate a description for my video with the following format: Title of the video, followed by a summary in 2-3 sentences, highlighting the main topics."
    )
    st.write(f"{res.data}")
    
    # python -m pip install requests
    
    import requests
    
    # Construct the URL of the `/embed` endpoint
    BASE_URL = "https://api.twelvelabs.io"
    VERSION = "v1.2"
    EMBED_URL = f"{BASE_URL}/{VERSION}/embed"
    
    # Set the headers of the request
    headers = {
        "x-api-key": st.secrets['TWELVE_API'])
    }
    
    # Specify the body of the request
    data = {
        "engine_name": "Marengo-retrieval-2.6",
        "text": "bollywood",
    }
    
    # Invoke the POST method of the `/embed` endpoint
    response = requests.post(EMBED_URL, headers=headers, data=data)
    
    # st.write the status code and the response
    st.write(f"Status Code: {response.status_code}")
    st.write("Response:")
    st.write(response.json())
    
    # python -m pip install requests
    
    import requests
    
    # Construct the URL of the `/embed` endpoint
    BASE_URL = "https://api.twelvelabs.io"
    VERSION = "v1.2"
    EMBED_URL = f"{BASE_URL}/{VERSION}/embed"
    
    # Set the headers of the request
    headers = {
        "x-api-key": st.secrets['TWELVE_API'])
    }
    
    # Specify the body of the request
    data = {
        "engine_name": "Marengo-retrieval-2.6",
        "text": "<YOUR_TEXT>",
    }
    
    # Invoke the POST method of the `/embed` endpoint
    response = requests.post(EMBED_URL, headers=headers, data=data)
    
    # st.write the status code and the response
    st.write(f"Status Code: {response.status_code}")
    st.write("Response:")
    st.write(response.json())
    
    from twelvelabs import TwelveLabs
    
    client = TwelveLabs(api_key=st.secrets['TWELVE_API']))
    
    res = client.generate.text(
      video_id="6652c6b4d22b3a3c97bef629",
      prompt="I want to generate a description for my video with the following format: Title of the video, followed by a summary in 2-3 sentences, highlighting the main topics."
    )
    st.write(f"{res.data}")
    
    # python -m pip install requests
    
    import requests
    
    # Construct the URL of the `/embed` endpoint
    BASE_URL = "https://api.twelvelabs.io"
    VERSION = "v1.2"
    EMBED_URL = f"{BASE_URL}/{VERSION}/embed"
    
    # Set the headers of the request
    headers = {
        "x-api-key": st.secrets['TWELVE_API'])
    }
    
    # Specify the body of the request
    data = {
        "engine_name": "Marengo-retrieval-2.6",
        "text": "<YOUR_TEXT>",
    }
    
    # Invoke the POST method of the `/embed` endpoint
    response = requests.post(EMBED_URL, headers=headers, data=data)
    
    # st.write the status code and the response
    st.write(f"Status Code: {response.status_code}")
    st.write("Response:")
    st.write(response.json())
