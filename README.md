# Deidentify and Distill Data 
Desktop application removes personally identifying information from text data and then uses AI to extract insights from the deidentified data. 
Essentially a wrapper over spaCy's NER models and Google's Gemini API.  

# Windows (10 and later) - Build Instructions 
1. Clone this repo.
2. Create a config file, secrets.py, in the cloned repo. Add your Google Gemini API key and the full path to your images folder.
3. Follow the instructions in spaCy's docs to download to your site packages folder the specific model(s) that you want to use.
4. Add the full path to each model to your secrets.py config file. The path should look like this: {r'C:\\Users\\YOUR_NAME\AppData\\Local\\Programs\\Python\\Python310\\Lib\site-packages\\YOUR_SPACY_MODEL\\YOUR_SPACY_MODEL-VERSION}
5. From within the main folder of the cloned repo, run {pyinstaller FULL_PATH_TO_YOUR_PROGRAM}.
   
# Linux Build Steps 
_Untested_
1. Clone this repo. 
2. Ensure #!/usr/bin/env python3 is included at the top of your 'Deidentify_and_Distill_Data.py' file.
3. Run chmod + x Deidentify_and_Distill_Data.py
4. Double-clicking the file from within this directory should launch the program in executable-fashion.

# MacOS Build Steps 
#TODO 

# Example Use
1. When you click the executable, and after the program loads, you should see this screen (modulo your custom images): 
<img width="960" alt="image" src="https://github.com/user-attachments/assets/dcbe0cb4-5461-474f-bbd8-0533682cd929">
2. Click "Browse", then upload the .xlsx file containing the deidentified data that you want processed.
 <img width="960" alt="image" src="https://github.com/user-attachments/assets/9614fc00-912a-4926-bd4d-81b1d1c24e6c">
4. Enter a prompt, and then click start. Once the program finishes running, Gemini's output will be displayed, like this:
 <img width="960" alt="image" src="https://github.com/user-attachments/assets/812080d0-559d-4ba0-bf87-61c721907d27">

# Important Notes 
The ExtractedText class includes a utility function to export the deidentified data to a spreadsheet. 

# TODO  
Add model class to allow users to supply models. 
Add diff tool to allow users to compare output across models. 
Add an automated validation step (i.e. doublecheck that the data was successfully deidentified) before prompting Gemini. 
Add an optional manual validation step, which prompts the user to manually doublecheck that the data was successfully deidentified. 
