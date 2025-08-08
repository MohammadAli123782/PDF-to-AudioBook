# 📖 PDF to Audiobook Converter

Convert your PDF files into spoken audio (MP3) using Python!  
This script extracts text from a PDF and uses **Google Text-to-Speech (gTTS)** to create a natural-sounding audiobook.  

---

## 🚀 Features
- Extracts text from any PDF file.
- Converts the text to speech in MP3 format.
- Uses **Google Text-to-Speech** for high-quality audio.
- Simple and lightweight Python script.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **[PyPDF2](https://pypi.org/project/PyPDF2/)** – For extracting text from PDF files.
- **[gTTS](https://pypi.org/project/gTTS/)** – For converting text to speech.

---

## 📂 Project Structure
```
📂 pdf-to-audiobook/
 ├── pdf_to_audio.py      # Main script
 ├── name.pdf             # Your PDF file (replace with your own)
 ├── requirements.txt     # List of dependencies
 └── README.md            # Documentation
```

---

## 📦 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/pdf-to-audiobook.git
cd pdf-to-audiobook
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` does not exist, create one with:)*  
```
PyPDF2
gTTS
```

### 3️⃣ Add your PDF
Place your PDF file in the project folder and rename it in the script:
```python
pdf_path = "name.pdf"  # Replace with your PDF file name
```

### 4️⃣ Run the script
```bash
python pdf_to_audio.py
```

### 5️⃣ Output
- An MP3 file named `Audio.mp3` will be saved in the same folder.

---

## 📸 Example Output
```
Extracted text preview:
 Once upon a time, in a quiet village, there lived...
✅ Audio file saved as 'Audio.mp3'.
```

---

## ⚠️ Notes
- Requires internet connection for `gTTS` to work.
- If your PDF contains scanned images instead of text, you will need OCR tools like **pytesseract** to extract the text.

---

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.

---

