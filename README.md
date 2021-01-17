# Bookify HackNITP 3.0
Bookify project made for HackNITP 3.0
### Concept
You may have used Spotify to listen to songs. But, what about books or lengthy PDFs? Well, you might say that audiobooks serve that purpose. But, using this web application, users can upload PDF document and get the summary of that PDF file in the language of their choice as audio output (mp3). Hence, listening to the summaries of these PDF documents in your native language can save your time and effort.
### Dependencies
1. Python
2. Django 
3. Pdfplumber
4. NLTK
5. Textblob
6. Gtts
7. HTML
8. CSS
9. BootStrap
### Deployed Webapp Link
https://bookify-hack-nitp.herokuapp.com/
### In Case It Doesn't Work...Instructions For Setting Up The Project Locally
* Download or clone the repository into your local machine.
* Run `pip install -r requirements.txt` to install required modules.
* Run `python manage.py runserver` to run in test server in `http://127.0.0.1:8000/`.
* Run `python manage.py collectstatic` to set up static files.
* Run `python manage.py migrate` to set up database.
* Run `python manage.py createsuperuser`to create an admin user. You can visit the admin dashboard in `http://127.0.0.1:8000/admin/`.
* In the terminal run `python` to open python shell. 
* Run `import nltk` and `nltk.download('punkt')`, `nltk.download('stopwords')` to get the required nltk libraries installed.
* Boom! you are ready to go.
### Youtube Link
https://youtu.be/qC93WRwFmY0
### Presentation Link
https://drive.google.com/file/d/1CsLhVtdtFpnGqAXZkIpXL6BnutCUyOB7/view?usp=sharing
