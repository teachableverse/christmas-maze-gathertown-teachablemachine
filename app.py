from flask import Flask, render_template, request, make_response, jsonify
import pyautogui as pag 

# please import pydirectinput instead of pyautogui for windows user
# import pydirectinput as pag

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')

@app.route("/action", methods=["GET"])
def action():
    index = request.args.get('index')
    print("index : " + index)

    if index == '1':
        pag.press('up')
    elif index == '2':
        pag.press('down')
    elif index == '3':
        pag.press('right')
    elif index == '4':
        pag.press('left')
    
    return make_response(jsonify({"status number": 200}), 200)
  
if __name__ == "__main__":
  app.run(port=5001)