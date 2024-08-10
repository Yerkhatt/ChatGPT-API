from fastapi import FastAPI
import schemas
from ChatGPT import ChatGPT
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Initialize ChatGPTClient
model = ChatGPT(api_key="your_api_key")

prompt = 'You are essay evaluation expert. Evaluate given essays'   # change it

@app.post('/post_request', tags=['API'])
def user_request(request: schemas.Text):
	
	response = model.generate_response(prompt=prompt, user_text = request.text)

	return {"response": response}