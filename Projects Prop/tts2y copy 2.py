from gtts import gTTS

language = 'en'
text = "Welcome to FAR111 a mobile application for first aid instruction, please choose a scenario to continue."

speech = gTTS (text=text, lang=language, slow=False, tld='com')
speech.save("output4.mp3")