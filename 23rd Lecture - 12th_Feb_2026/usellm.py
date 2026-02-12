import asyncio
import os
# import google.generativeai as genai

from dotenv import load_dotenv


# class ModelGemini:
#     def __init__(self):
#         load_dotenv()
#         self.gemini_api_key = os.getenv("GEMINI_API_KEY")
#         if not self.gemini_api_key:
#             raise ValueError("API key for GEMINI is not set in the .env file.")
#         os.environ["GEMINI_API_KEY"] = self.gemini_api_key
#         genai.configure(api_key=self.gemini_api_key)

#     async def gemini_response(self, prompt):
#         model = genai.GenerativeModel("gemini-2.0-flash")
#         response = model.generate_content(prompt)
#         await asyncio.sleep(1)
#         return response.text
    
import asyncio
import requests


class ModelQwen:
    def __init__(self, base_url="http://192.168.12.1:30243"):
        self.base_url = base_url.rstrip("/")
        self.endpoint = f"{self.base_url}/v1/chat/completions"

    def _qwen_text_response(self, prompt: str) -> str:
        payload = {
            "model": "Qwen/Qwen3-4B-Instruct-2507",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt}
                    ]
                }
            ],
            "max_tokens": 500,
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                self.endpoint,
                json=payload,
                headers=headers,
                timeout=60
            )
            response.raise_for_status()
        except Exception as e:
            return f"LLM Server Error: {e}"

        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]

        return str(data)

    async def qwen_response(self, prompt: str) -> str:
        # Run blocking requests in a thread (IMPORTANT)
        return await asyncio.to_thread(self._qwen_text_response, prompt)
