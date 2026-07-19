from gtts import gTTS

language = 'en'
text = "Hello, this is a test of the text-to-speech functionality by Lywin."

speech = gTTS (text=text, lang=language, slow=False, tld='com')
speech.save("output1.mp3")