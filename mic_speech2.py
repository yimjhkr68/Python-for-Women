#!/usr/bin/env python3 "mic_speech2.py"

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said [" + r.recognize_google(audio) + "]")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "speech-to-text-160208",
  "private_key_id": "e254f600dab65bcf30093a9480f741d54402ac08",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDFKoDqAxno/y/+\nlxsFK34G/K2zsv5Ikmkj5PUtkDk9edHfmSOJA9kUHiFw9Ldg+iI7/Zr0H2iVD0vr\n4B5UaImkDoB6BqR2Ow057d+deAYuRhfLaqGvoqvYy0TGnFUo4e1dBX1TmBRiLyd+\nJBiuHaqTwSDaWjSouLKrIdd31B6xcgg1A125XSzvwcB84shcaNn95L4PKCZPkQgA\nRIS5mhx1/3yEfDndQ8lVpxfmI5ZW9SmEjA05ILFFfQqpey05/Wr59ZICv4B929Vu\nmAYmE+pmFDTcG/pSf8e7NAISgex22d2oJKJUujLFsh+D6oGbymNPFruTGOrHqpZL\nPy3TGtKxAgMBAAECggEAPfHCmsLqqwcxnvz+Yjtt1ugf8qsztL07Bynx1aTQNv5E\n78j/Hxb0ZpuoygI4cuFjTBG7UyNjCiHKKos5PC+zvrVHrA7WMMcQurh/XsvMtVEU\nPLZ9od6ruurx6qxHHRcOKgGFhHPtQ4OpFrpkfp+XbeBpX/CjRrbwe0+gkGc2VWz+\nrvrA0FdOGtWZILlajbvON7HgZ3lTVjIjnHGG0bGCBHk6AVfrz6kjENTXXUrWMz/E\n9+iSwfPbWrzGUo4QogfB8uJ5UFfNZOYUWCPfdVVE1hue9XvkVz9t7YeKZ4M6UHRk\nnX6bxy3KRnQwSSiAK6vgEoakgdfz/r4jHSYASTO4IQKBgQDvXTFibdw3V3tUnOo7\nCB2R5ag7bWn58OK07178MfnN6IDrRtUoPBozYuWoHxuhRS1TL3drjhNBUK9oNMJ0\nP3DxoNRBLiGlceEi4wMxeeA0qg671ph9C+CcEWIpZyT8cxki4pdQ7jYghrc3X0Ji\nkM2IjyhT0ki9W4hqSC5Bf/SW9QKBgQDS3oQtVmTOFI+tquAEk0BdqPuVMLQRRXkQ\nHkkVNX0ABlRwCXvWLdhQLGWtUft0rtZho12n7ZAFBe9EBYOX1J9fbenJWRdU29gq\n2KolcuA0z0mE2B8uKVtYXH3fi1byZ+GW9yU2EytBUK3i4S8t4tPtcb4G94nbbdj9\n5MPRwKLfTQKBgQC3+AZ2wj0ZA9G0bI3SJSCk+7/bPPLQuQVlTvzQFJEMYwCC1AQM\nUnVIvWAJYS9ZOdPmNXsxXRcLgjnue25g7kmeTKAWIKCXifkhWR0hL6zUjUeZswus\nQC63hNzPOYlBxiyxlTn7Z7qOMTwsALkDDIwLwwuZsOtbLjighy2WBgQ06QKBgH3M\n1lod4oG3bogTGxZfqtS1jXHR3ns3USQ2jS8j+/DZ1eIJJmH+c8BQ3E/sSvGvpKIX\nTjZy2arFgZq5F2qrJHFQJ1tB1VOA3JOjMs6om+2lhJzGOsPVVHOAqm+Et1hidQkV\nZJPAF9wdf7+MzBK58ekEJHQPlaTdAclmgxRNsl05AoGBAMR/bMfdqEVau9+KqiDU\nudcbYzpkDfwV+rE58iS8aW0IkRcgMZL79OI+f/ZxC6qLPmahYxsFUKcKqIimWBvM\narRY0qvn5Pv04HKWg5uUQpbHcfBuc3WA7mvD6jkaYL9mBZWJxBM7IbzJsdjqYpcG\nkZdTZp7DnSh396Y3qC2v4Y7M\n-----END PRIVATE KEY-----\n",
  "client_email": "844043050975-compute@developer.gserviceaccount.com",
  "client_id": "111198725381511708389",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/844043050975-compute%40developer.gserviceaccount.com"
}"""
try:
    print("Google Cloud Speech thinks you said [" + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)+ "]")
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

