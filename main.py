import uvicorn
from art import tprint


if __name__ == '__main__':
    tprint('Deploy - data Mining')
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
