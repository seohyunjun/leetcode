import json
import openai
import time

def get_key():
    with open('./key/OpenAPI_APIKEY.json') as json_file:
        json_data = json.load(json_file)
    return json_data

prompt = 'Design Circular Deque' 
def getInfo(prompt):
    OpenAIKEY = get_key()
    openai.api_key = OpenAIKEY['Key']['Authorization']    
    
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{prompt}에 대해 markdown형식으로 설명해줘"}])
    content = completion.choices[0].message.content
    return content