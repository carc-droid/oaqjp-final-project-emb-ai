import requests  # Import the requests library to handle HTTP requests
import json

 # Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse): 
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
    # Create a dictionary with the text to be analyzed 
    myobj = { "raw_document": { "text": text_to_analyse } }  

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)  

    # Check if the request was successful
    if response.status_code != 200:
        return {"error": "Failed to retrieve emotions"}

    # Convert the response to a dictionary
    response_dict = json.loads(response.text)
    
    # Extract the emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Format the output
    formatted_output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    

    # Return the response text from the API
    #return response.text  

    return formatted_output
    
# Testing the function
# print(emotion_detector("I am so happy I am doing this"))
