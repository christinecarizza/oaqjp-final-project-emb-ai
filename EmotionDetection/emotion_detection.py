import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers, timeout=10)

    # Error handling
    if response.status_code == 400:
        modified_emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Convert response to json
        response_dict = json.loads(response.text)

        # Extract the required set of emotions
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        # Get the emotion with the highest score
        emotion_max_score = max(emotions, key=emotions.get)
        
        modified_emotions = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': emotion_max_score
        }
    
    return modified_emotions