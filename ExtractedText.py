# -*- coding: utf-8 -*-
import openpyxl 
from openpyxl import load_workbook
import spacy 
import SpacyNLP 
from SpacyNLP import SpacyNLP
import re

matcher = re.compile(r'[A-Za-z0-9]+')#r'\b[A-Za-z]+\b')

def replace_target(match, replacements):
    target = match.group()
    return replacements.get(target, target)

def hamming_distance(str1, str2):
  added = 0
  while len(str1) < len(str2):
    str1 += " "
  while len(str2) < len(str1):
    str2 += " "
  return sum(char1 != char2 for char1, char2 in zip(str1, str2))

class ExtractedText:
  """
  methods for extracting and interacting with text from spreadsheets
  """
  def __init__(self, spreadsheet_filename):
    self.spreadsheet = load_workbook(spreadsheet_filename, data_only=True)
    self.worksheet = self.spreadsheet.active
    self.rows = [[value for value in row if value != None] for row in self.worksheet.values if len([val for val in row if val != None]) > 1]
    self.worksheet_headers = self.rows[0]
    self.headerless_rows = self.rows[1:]
    self.chunked_text = self.chunk_text()

  def chunk_text(self):
    chunked_text = ""
    for row in self.headerless_rows:
        chunked_text += ' '.join(row)
    return chunked_text

  def redact(self):
    NLPEngine = SpacyNLP()

    redacted_text = []

    unredacted_text = NLPEngine.process_doc(self.chunked_text)
    all_named_entities = NLPEngine.get_all_named_entities(unredacted_text)

    replacements = {entity:entity_type for entity,entity_type in all_named_entities}

    #need to do some preprocessing to ensure that persons are uniquely identified but anonymized
    #need to be uniquely identified for LLM to provide summaries for each individual

    #first assign a unique identifier to each value
    id = 0
    for entity in replacements:
      if replacements[entity] == 'PERSON':
        id += 1
        replacements[entity] = 'PERSON'+str(id)

    #replace similar strings
    list_keys = list(replacements.keys())
    for i in range(len(list_keys)):
      for j in range(i+1, len(list_keys)):
        if hamming_distance(list_keys[i][:-1], list_keys[j][:-1]) <= 4:
          replacements[list_keys[j]] = replacements[list_keys[i]]

    for row in self.headerless_rows:
      for string in row:
        processed = re.sub(matcher, lambda match: replace_target(match, replacements), string)
        for entity in replacements:
          processed = processed.replace(entity, replacements[entity])
        redacted_text.append(processed)
    return redacted_text
