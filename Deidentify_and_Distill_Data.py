#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deidentifying sensitive data and using Gemini to summarize and analyze student evaluations
"""
import sys
import os
import pkgutil
import openpyxl
from openpyxl import Workbook
import re
import google.generativeai as genai

import ExtractedText
from ExtractedText import ExtractedText
import SpacyNLP

import google.generativeai as genai
genai.configure(api_key="AIzaSyBTAu05pQbGou5vt2Vww5Otkhy-AjjW5js")

import argparse
from argparse import ArgumentParser

import gooey 
from gooey import GooeyParser, Gooey, local_resource_path

#spreadsheet_filename = 'UNREDACTED.xlsx'

path_to_images = r'C:\\Users\\thoma\\Downloads\\TextSummarizing\\images'

current_model = 'Gemini 1.5'

def generate_redacted(spreadsheet_filename):
  unredacted_text = ExtractedText(spreadsheet_filename)
  redacted_text = unredacted_text.redact()
  return redacted_text

#redacted_text = generate_redacted(spreadsheet_filename)
#model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content(f'The following text contains evaluations of medical preceptors. It was completed anonymously by students. First, please summarize the feedback received for each preceptor. Draw out themes and highlights. At the end, provide a precise sentiment analysis of the feedback. {redacted_text}.')
#print(response.text)

#nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
#sys.stdout = nonbuffered_stdout

__DESCR__ = ('This program deidentifies and then analyzes preceptor evaluations using AI.')

@Gooey(default_size=(700, 400), navigation='TABBED', advanced=True, image_dir=local_resource_path(path_to_images), menu=[{
        'name': 'File',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'Instructions',
                'name': 'Instructions',
                'description': '1. Upload a spreadsheet containing the data you want analyzed. 2. The program will output a spreadsheet of redacted text. Check that all sensitive information was successfully anonymized. 3. Prompt the AI using the anonymized text.'
                ,
                'developer': 'Thomas Evans',
                'license': 'MIT'
            }, {
                'type': 'MessageDialog',
                'menuTitle': 'Example Prompt',
                'message': 'The following text contains evaluations of medical preceptors. It was completed anonymously by students. First, please summarize the feedback received for each preceptor. Draw out themes and highlights. At the end, provide a precise sentiment analysis of the feedback.'
            }]
        },{
        'name': 'Help',
        'items': [{
            'type': 'Link',
            'menuTitle': 'Documentation',
            'url': 'https://www.readthedocs.com/foo'
        }]
    }])
def main():
  parser = GooeyParser(prog='Deidentify and Distill Data', description=__DESCR__)
  parser.add_argument('Upload_Spreadsheet', widget='FileChooser',
                        help='Name of the spreadsheet containing the evaluations you want deidentified.')
  parser.add_argument('Prompt', help=f'Enter a prompt for {current_model}.')
  
  #parser.add_argument('')
  args = parser.parse_args()
  spreadsheet_filename = args.Upload_Spreadsheet

  redacted_text = generate_redacted(spreadsheet_filename)

  #for text in redacted_text:
  #  print(text)
#   event, values = sg.Window('Please review the data to make sure deidentification was successful. AI makes mistakes: you may need to manually fix them and then rerun the program. Sorry!', [[sg.Text('Select one->'), sg.Listbox(['No errors. Please proceed'], size=(20, 3), key='LB')],
#     [sg.Button('Proceed'), sg.Button('Cancel')]]).read(close=True)

# if event == 'Proceed':
# sg.popup_cancel('User aborted'
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(f'{args.Prompt} {redacted_text}')#f'The following text contains evaluations of medical preceptors. It was completed anonymously by students. First, please summarize the feedback received for each preceptor. Draw out themes and highlights. At the end, provide a precise sentiment analysis of the feedback. {redacted_text}.')
  print(response.text)

if __name__=="__main__":
  main() 