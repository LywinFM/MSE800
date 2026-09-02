from gtts import gTTS

language = 'en'
text = "If the person is unconscious, check for breathing and pulse. If there is no breathing or pulse, begin CPR immediately. If the person is breathing but not responsive, place them in the recovery position by rolling the person onto their side with head tilted back slightly and monitor their condition until help arrives."

speech = gTTS (text=text, lang=language, slow=False, tld='com')
speech.save("output5.wav")