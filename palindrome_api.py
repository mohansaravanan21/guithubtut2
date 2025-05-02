from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

def is_palindrome_recursive(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.

    :param s: Input string
    :return: True if the string is a palindrome, False otherwise
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

class PalindromeInput(BaseModel):
    text: str

@app.post("/check-palindrome/")
def check_palindrome(input: PalindromeInput):
    result = is_palindrome_recursive(input.text)
    return {"text": input.text, "is_palindrome": result}

if __name__ == "__main__":
    # Run the server with nohup to keep it running in the background
    os.system("nohup uvicorn palindrome_api:app --host 127.0.0.1 --port 8008 --reload &")