from pprint import pprint
import requests

def addCard(front: str, back: str):
    print(front, back)
    r = requests.post('http://127.0.0.1:8765', json={
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Computer Science::PSI::Data representation::Units of infomation",
                "modelName": "Basic",
                "fields": {
                    "Front": f"{front}",
                    "Back": f"{back}"
                },
            }
        }
    })

while True:
    prefix = input('Enter prefix: ')
    prefixSymbol = input('Enter prefix symbol: ')
    base = '10'
    exponent = input('Enter exponent: ')
    value = input('Enter value: ')

    addCard(f'How many bytes in a {prefix}byte ({prefixSymbol})?', f"\\[\n{base}^{'{'+ exponent + '}'}={value}\n\\]")


