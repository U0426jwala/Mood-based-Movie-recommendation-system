# 🎬 Mood-Based Movie Recommendation System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/AI-Emotion%20Detection-orange.svg" alt="AI Emotion Detection">
  <img src="https://img.shields.io/badge/Audio-Speech%20Recognition-purple.svg" alt="Audio Processing">
</p>

<p align="center">
  <strong>An intelligent movie recommendation system that analyzes your voice emotions to suggest the perfect movies for your current mood! 🎭</strong>
</p>

---

## 🌟 Features

✨ **Voice Emotion Detection**: Advanced AI-powered emotion recognition from audio input  
🎯 **Smart Categorization**: Automatically categorizes emotions into 5 distinct mood categories  
🎬 **Personalized Recommendations**: Tailored movie suggestions based on detected emotions  
🔊 **Real-time Processing**: Instant audio-to-text transcription and emotion analysis  
🌐 **Web Interface**: Clean, responsive web application for seamless user experience  
🔥 **Multi-Emotion Support**: Recognizes 27+ different emotions with high accuracy  

---

## 🧠 How It Works

1. **🎤 Voice Input**: User records their voice through the web interface
2. **📝 Speech-to-Text**: Audio is transcribed using Whisper AI model
3. **😊 Emotion Detection**: Text is analyzed using DistilBERT for emotion classification
4. **🎯 Mood Categorization**: Emotions are mapped to one of 5 mood categories:
   - **Reflective & Understand** - For contemplative moods
   - **Distract & Change** - For negative emotions needing redirection
   - **Energetic & Motivate** - For high-energy, positive vibes
   - **Engage & Explore** - For curious and explorative moods
   - **Soothe & Uplift** - For calming and uplifting experiences

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python) |
| **AI Models** | Whisper (Speech Recognition), DistilBERT (Emotion Detection) |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | Firebase Realtime Database |
| **ML Libraries** | PyTorch, Transformers, Whisper |
| **Audio Processing** | OpenAI Whisper |

---

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- CUDA-compatible GPU (optional, for faster processing)
- Microphone access for audio recording

### Python Dependencies

```txt
flask>=2.0.0
flask-cors>=3.0.0
torch>=1.9.0
transformers>=4.15.0
whisper>=1.0.0
firebase-admin>=6.0.0
pyaudio>=0.2.11
numpy>=1.21.0
requests>=2.25.0
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mood-movie-recommendation.git
cd mood-movie-recommendation
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Whisper Model
```bash
pip install openai-whisper
```

### 5. Firebase Configuration
- Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
- Enable Realtime Database
- Update the configuration in `test.py` with your Firebase credentials:

```python
config = {
  "apiKey": "your-api-key",
  "authDomain": "your-project.firebaseapp.com",
  "projectId": "your-project-id",
  # ... other config
}
```

### 6. Create Required Directories
```bash
mkdir tmp templates static
```

---

## 🏃‍♂️ Running the Application

### Development Mode
```bash
python app.py
```

### Production Mode (using WSGI)
```bash
python wsgi.py
```

The application will be available at `http://localhost:7860`

---

## 📁 Project Structure

```
mood-movie-recommendation/
├── app.py                 # Main Flask application
├── wsgi.py               # WSGI entry point
├── test.py               # Firebase configuration
├── requirements.txt      # Python dependencies
├── modules/
│   ├── __init__.py      # Main module class
│   ├── emotion.py       # Emotion detection logic
│   ├── transcription.py # Speech-to-text processing
│   └── utils.py         # Utility functions
├── templates/           # HTML templates
│   ├── index.html
│   ├── audio_to_text.html
│   ├── reflectiveandunderstand.html
│   ├── distractandchange.html
│   ├── energeticandmotivate.html
│   ├── engageandexplore.html
│   └── soothieanduplift.html
├── static/             # CSS, JS, images
└── tmp/               # Temporary audio files
```

---

## 🎭 Supported Emotions

The system recognizes and categorizes the following emotions:

| Category | Emotions |
|----------|----------|
| **Soothe & Uplift** | Admiration, Amusement, Approval, Caring, Gratitude, Joy, Love, Relief, Neutral |
| **Distract & Change** | Anger, Annoyance, Disapproval, Disgust, Embarrassment, Fear, Nervousness |
| **Energetic & Motivate** | Excitement, Joy, Optimism, Pride |
| **Engage & Explore** | Confusion, Curiosity, Desire, Realization, Surprise |
| **Reflective & Understand** | Disappointment, Grief, Remorse, Sadness |

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application interface |
| `/audio_to_text/` | GET | Audio recording interface |
| `/audio` | POST | Process audio and detect emotion |
| `/reflectiveandunderstand` | GET | Reflective mood recommendations |
| `/distractandchange` | GET | Distraction-based recommendations |
| `/energeticandmotivate` | GET | Energetic mood recommendations |
| `/engageandexplore` | GET | Exploratory recommendations |
| `/soothieanduplift` | GET | Soothing recommendations |

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🐛 Troubleshooting

### Common Issues

**Audio not recording:**
- Ensure microphone permissions are granted
- Check browser compatibility (Chrome/Firefox recommended)

**Model loading errors:**
- Verify CUDA installation for GPU acceleration
- Ensure sufficient RAM (4GB+ recommended)

**Firebase connection issues:**
- Verify Firebase configuration
- Check internet connectivity

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI Whisper** for speech recognition
- **Hugging Face** for emotion detection models
- **Flask** for the web framework
- **Firebase** for database services

---

## 📞 Support

If you encounter any issues or have questions:

- 📧 Email: [ujwalakusma26@gmail.com]
- 🐛 Issues: [GitHub Issues](https://github.com/U0426jwala/Mood-based-Movie-recommendation-system.git)
- 💬 Discussions: [GitHub Discussions](https://github.com/U0426jwala/mood-movie-recommendation/discussion)

---

<p align="center">
  Made with ❤️ for movie lovers everywhere!<br>
  <strong>Turn your mood into your next favorite movie! 🎬✨</strong>
</p>



