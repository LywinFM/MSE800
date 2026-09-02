from gtts import gTTS # This for checking the Airway, Breathing, and Circulation (ABC) of a person in an emergency situation.

language = 'en'
text = "If the person is unconscious, check for breathing and pulse. If there is no breathing or pulse, begin CPR immediately or wait for help. If the person is breathing but not responsive, place them in the recovery position and monitor their condition until help arrives."

speech = gTTS (text=text, lang=language, slow=False, tld='com')
speech.save("output2.mp3")