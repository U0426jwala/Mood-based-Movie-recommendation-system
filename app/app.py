import os
import uuid
import logging
from flask import Flask, flash, redirect, render_template, request, jsonify, session, url_for
from flask.templating import TemplateNotFound 
from flask_cors import CORS
from modules import Module
import pymongo

model = Module()
app = Flask(__name__)
CORS(app)

app.secret_key = "Testing"

emotion_categories = {
  "admiration": "soothieanduplift",
  "amusement": "soothieanduplift",
  "anger": "distractandchange",
  "annoyance": "distractandchange",
  "approval": "soothieanduplift",
  "caring": "soothieanduplift",
  "confusion": "engageandexplore",
  "curiosity": "engageandexplore",
  "desire": "engageandexplore",
  "disappointment": "reflectiveandunderstand",
  "disapproval": "distractandchange",
  "disgust": "distractandchange",
  "embarrassment": "distractandchange",
  "excitement": "energeticandmotivate",
  "fear": "distractandchange",
  "gratitude": "soothieanduplift",
  "grief": "reflectiveandunderstand",
  "joy": "energeticandmotivate",
  "love": "soothieanduplift",
  "nervousness": "distractandchange",
  "optimism": "energeticandmotivate",
  "pride": "energeticandmotivate",
  "realization": "engageandexplore",
  "relief": "soothieanduplift",
  "remorse": "reflectiveandunderstand",
  "sadness": "reflectiveandunderstand",
  "surprise": "engageandexplore",
  "neutral": "soothieanduplift"
}

@app.route('/')
def Home():
    return render_template('auth.html')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
  return render_template('audio_to_text.html')

@app.route('/audio', methods=['POST', 'GET'])
def audio():
    if request.method == 'POST':
        try:
            output_file = f"./tmp/{uuid.uuid4()}.wav"
            open(output_file, 'wb').write(request.data)
            text, emotion = model.predict(audio_path=output_file)
            os.remove(output_file)
            
            predicted_category = emotion_categories.get(emotion, "defaultcategory")
            return jsonify({
                "url": url_for(predicted_category, text=text, emotion=emotion)
            })
            print("Predicted Category:", predicted_category)  # Print predicted category
            print("Text:", text)  # Print predicted text
            print("Emotion:", emotion)  # Print predicted emotion
            logging.info("Predicted Category: %s", predicted_category)
            logging.info("Text: %s", text)
            logging.info("Emotion: %s", emotion)
            return jsonify({"url": url_for(predicted_category)})
            
        except (FileNotFoundError, TemplateNotFound) as e:
            logging.error(e)
            return jsonify({"error": "Template file not found."}), 404

        except Exception as e:
            logging.error(e)
            return jsonify({"error": "An error occurred"}), 500
            
    elif request.method == 'GET':
        return jsonify({"message": "This route only accepts POST requests."}), 405


@app.route('/reflectiveandunderstand', methods=['GET']) 
def reflectiveandunderstand():
    text = request.args.get('text', '')  # Get predicted text
    emotion = request.args.get('emotion', '')  # Get predicted emotion
    return render_template('reflectiveandunderstand.html', text=text, emotion=emotion) 

@app.route('/distractandchange', methods=['GET']) 
def distractandchange():
    text = request.args.get('text', '')  # Get predicted text
    emotion = request.args.get('emotion', '')  # Get predicted emotion
    return render_template('distractandchange.html', text=text, emotion=emotion)

@app.route('/energeticandmotivate', methods=['GET']) 
def energeticandmotivate():
    text = request.args.get('text', '')  # Get predicted text
    emotion = request.args.get('emotion', '')  # Get predicted emotion
    return render_template('energeticandmotivate.html', text=text, emotion=emotion) 

@app.route('/engageandexplore', methods=['GET']) 
def engageandexplore():
    text = request.args.get('text', '')  # Get predicted text
    emotion = request.args.get('emotion', '')  # Get predicted emotion
    return render_template('engageandexplore.html', text=text, emotion=emotion)

# Add more routes as needed, mirroring your category names
@app.route('/soothieanduplift', methods=['GET']) 
def soothieanduplift():
    text = request.args.get('text', '')  # Get predicted text
    emotion = request.args.get('emotion', '')  # Get predicted emotion
    return render_template('soothieanduplift.html', text=text, emotion=emotion) 


# Add more routes as needed, mirroring your category names


con=pymongo.MongoClient("mongodb://127.0.0.1:27017/")

db=con["moviedb"]

ucoll=db["users"]


@app.route("/",methods=["GET","POST"])
def userAuth():
    if request.method=='POST':
        btnstate=request.form.get("state")
        if btnstate=="REGISTER":
            print("redirecting to ---------> Registed")
            username=request.form.get("username")
            email=request.form.get("email")
            pwd=request.form.get("password")
            phno=request.form.get("phno")
            data={"username":username,"email":email,"password":pwd,"phno":phno}
            user = ucoll.find_one({"email": email})
            if user!=None:
                flash("User already exist !")
                print("user already exist !")
            else:
                ucoll.insert_one(data)
                print("User created sucessfully")
                return redirect(url_for('userAuth'))
        

        if btnstate=="LOGIN":
            print("redirecting to ---------> Logined")
            email=request.form.get("email")
            pwd=request.form.get("password")
            user = ucoll.find_one({"email": email})
            if user==None:
                flash("User does not exit")
                print("User does not exit ")
                
            if user and user["password"] == pwd:
                session['username']=user["email"]
                return redirect(url_for('index'))
            else:
                flash("you have entered incorrect password")
                print("you have entered incorrect password")
        print(btnstate)
    return render_template("auth.html")



if __name__ == "__main__":
  # Configure logging for Hugging Face environment
  logging.basicConfig(level=logging.DEBUG)

  app.run(debug=True, port=7860, host='0.0.0.0')