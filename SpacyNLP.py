import spacy

class SpacyNLP:
  """
  wrapper over SpaCy's NLP engine
  """
  def __init__(self):
    self.nlp = spacy.load(r'C:\\Users\\thoma\AppData\\Local\\Programs\\Python\\Python310\\Lib\site-packages\\en_core_web_sm\\en_core_web_sm-3.7.1')

  def process_doc(self, doc):
    return self.nlp(doc)

  def get_all_named_entities(self, processed_doc):
    return [(ent.text, ent.label_) for ent in processed_doc.ents]

  def get_person_entities(self, all_named):
    return [pair for pair in all_named if pair[1] == 'PERSON']

  def get_loc_entities(self, all_named):
    return [pair for pair in all_named if pair[1] == 'LOCATION']

  def get_org_entities(self, all_named):
    return [pair for pair in all_named if pair[1] == 'ORGANIZATION']

  def get_card_entities(self, all_named):
    return [pair for pair in all_named if pair[1] == 'CARDINAL']
