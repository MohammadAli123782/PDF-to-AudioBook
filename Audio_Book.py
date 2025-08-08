from gtts import gTTS
from PyPDF2 import PdfReader

pdf_path = "name.pdf"   #Add your pdf path here

try:
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text_list = []


        for page in pdf_reader.pages:
            text  = page.extract_text()
            if text:
                text_list.append(text.strip())

    text_string = " ".join(text_list)

    if not text_string.strip():
        raise ValueError("No text could be extracted from the PDF.")


    print("Extracted text preview:\n", text_string[:500], "...\n")


    language = "en"
    audio = gTTS(text=text_string , lang=language,slow=False)


    audio.save("Audio.mp3")
    print("✅ Audio file saved as 'Audio.mp3'. ")

except FileNotFoundError:
    print(f"❌ Error: The file '{pdf_path}' was not found. ")

except Exception as e:
    print(f"❌ An error occured: {e}")    
