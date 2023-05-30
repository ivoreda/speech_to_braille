import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak into the mic...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text_from_mic = text.lower()
    except speech_recognition.UnknownValueError:
        print("Sorry i didnt understanc you...")


braille_alphabet = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',
}

def translate_to_braille(text):
    braille_text = ''
    for char in text:
        if char.lower() in braille_alphabet:
            braille_text += braille_alphabet[char.lower()]
        else:
            braille_text += char
    return braille_text

# Example usage
english_text = "IVOR IS THE BEST"
braille_text = translate_to_braille(text_from_mic)
print("Synthesised speech to braille")
print(braille_text)


"""
START
    using speech recognition library
    gain access to users microphone
    listen to spoken audio
    synthesise audio to text
    run text through braille_translator function
    check each character in text
    if the character is in the braille dictionary
    get the value of that character in braille
    add to a new string called "braille_text"
    print out braille text to console
END
"""