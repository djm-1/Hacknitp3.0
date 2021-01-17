# importing libraries
from django.shortcuts import render,HttpResponse
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import pdfplumber
import re
import os
import goslate
from textblob import TextBlob
from gtts import gTTS
from .models import Bookify
def index(request):
    if request.method == 'POST':
        uploaded_file=request.FILES['myfile']
        #print(uploaded_file.name)
        file_extension=uploaded_file.name.split('.')[-1]
        if file_extension =='pdf':
            new_audio_book = Bookify.objects.create(input_file=uploaded_file)
            #pdf = pdfplumber.open(uploaded_file)
            pdf = pdfplumber.open(new_audio_book.input_file)
            text=''
            for i in range(len(pdf.pages)):
                page = pdf.pages[i]
                text += page.extract_text()
            article_text = re.sub(r'\[[0-9]*\]', ' ', text)
            article_text = re.sub(r'\s+', ' ', article_text)
            # Removing special characters and digits
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
            sentence_list = nltk.sent_tokenize(article_text)
            stopwords = nltk.corpus.stopwords.words('english')

            word_frequencies = {}
            for word in nltk.word_tokenize(formatted_article_text):
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
                maximum_frequncy = max(word_frequencies.values())
            for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
                sentence_scores = {}
            for sent in sentence_list:
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]
            import heapq
            summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

            summary = ' '.join(summary_sentences)
            print(summary)
            summary = TextBlob(summary)
            lang=request.POST.get('lang')
            #print(lang)
            if lang!='en':
                summary= summary.translate(from_lang='en',to=lang)
            #print(summary)
            tts=gTTS(str(summary),lang=lang)

            
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            #tts.save(uploaded_file.name.split('.')[0]+'.mp3')
            tts.save("%s.mp3" % os.path.join(BASE_DIR+'/media/audio/',uploaded_file.name.split('.')[0]))
            Bookify.objects.filter(id=new_audio_book.id).update(output_file='audio/'+uploaded_file.name.split('.')[0]+'.mp3')
            
            
            pdf.close()
            return render(request,'index.html',{'model':Bookify.objects.get(id=new_audio_book.id)})
            #return 
        else:
            return HttpResponse('file format should be pdf only !')
    else:
        return render(request,'index.html')



