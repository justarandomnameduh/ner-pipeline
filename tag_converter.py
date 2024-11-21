import gzip

# Convert Ontonotes 5 formatted labels to conll03 format.
# @nlptimer
def convert_ontonotes_to_conll(input_file, output_file):
  # Mapping from OntoNotes 5 labels to CoNLL-2003 BIO labels
  ontonotes_to_conll = {
    "B-PERSON": "B-PER",
    "B-GPE": "B-LOC",
    "B-LOC": "B-LOC",
    "B-ORG": "B-ORG",
    "B-NORP": "B-MISC",
    "B-FAC": "B-MISC",
    "B-PRODUCT": "B-MISC",
    "B-EVENT": "B-MISC",
    "B-WORK_OF_ART": "B-MISC",
    "B-LAW": "B-MISC",
    "B-LANGUAGE": "B-MISC",
    "I-PERSON": "I-PER",
    "I-GPE": "I-LOC",
    "I-LOC": "I-LOC",
    "I-ORG": "I-ORG",
    "I-NORP": "I-MISC",
    "I-FAC": "I-MISC",
    "I-PRODUCT": "I-MISC",
    "I-EVENT": "I-MISC",
    "I-WORK_OF_ART": "I-MISC",
    "I-LAW": "I-MISC",
    "I-LANGUAGE": "I-MISC",
    # The following labels do not exist in CoNLL-2003 and are thus ignored
    "B-DATE": "O",
    "B-TIME": "O",
    "B-PERCENT": "O",
    "B-MONEY": "O",
    "B-QUANTITY": "O",
    "B-ORDINAL": "O",
    "B-CARDINAL": "O",
    "I-DATE": "O",
    "I-TIME": "O",
    "I-PERCENT": "O",
    "I-MONEY": "O",
    "I-QUANTITY": "O",
    "I-ORDINAL": "O",
    "I-CARDINAL": "O",
    "O" : "O"
  }

  with gzip.open(input_file, 'rt') as infile, gzip.open(output_file, 'wt') as outfile:
    for line in infile:
      if line.strip() == '':
        outfile.write('\n')
        continue
      pos, token, ontonotes_label = line.strip().split('\t')
      if ontonotes_label not in ontonotes_to_conll:
        print("[ERROR]: `{}' is not a valid ontonotes_label.".format(ontonotes_label))
        return False
      conll_label = ontonotes_to_conll.get(ontonotes_label, None)
      if conll_label:
        outfile.write(f"{pos}\t{token}\t{conll_label}\n")
      else:
        # If the label does not map to a CoNLL-2003 label, write the token with 'O'
        outfile.write(f"{pos}\t{token}\tO\n")
  return True


# Convert NLTK formated labels to Conll03.
#@nlptimer
def convert_nltk_to_conll(input_file, output_file):
  # Mapping from OntoNotes 5 labels to CoNLL-2003 BIO labels
  nltk_to_conll = {
    "B-FACILITY": "B-MISC",
    "I-FACILITY": "I-MISC",
    "B-GPE": "B-LOC",
    "I-GPE": "I-LOC",
    "B-GSP": "B-LOC",
    "I-GSP": "I-LOC",
    "B-LOCATION": "B-LOC",
    "I-LOCATION": "I-LOC",
    "B-ORGANIZATION": "B-ORG",
    "I-ORGANIZATION": "I-ORG",
    "B-PERSON": "B-PER",
    "I-PERSON": "I-PER",
    "I-FACILITY": "I-MISC",
    "B-FACILITY": "B-MISC",
    "O": "O"
  }
  with gzip.open(input_file, 'rt') as infile, gzip.open(output_file, 'wt') as outfile:
    for line in infile:
      if line.strip() == '':
        outfile.write('\n')
        continue
      pos, token, nltk_label = line.strip().split('\t')
      if nltk_label not in nltk_to_conll:
        print("[ERROR]: `{}' is not a valid nltk_label.".format(nltk_label))
        return False
      conll_label = nltk_to_conll.get(nltk_label, None)
      if conll_label:
        outfile.write(f"{pos}\t{token}\t{conll_label}\n")
      else:
        # If the label does not map to a CoNLL-2003 label, write the token with 'O'
        outfile.write(f"{pos}\t{token}\tO\n")
  return True


# Convert Spacy OntoNotes labels to Conll03
#print('\nConvert NLTK output format to conll03.\n')
#logger.info('\nConvert NLTK output format to conll03.\n')
#rv = convert_nltk_to_conll('nltk.gz', 'nltk.conllu.gz')
#if rv == False:
#  logger.error('[ERROR]: Convert Failed. Please fix the labels and retry.')
#  print('[ERROR]: Convert Failed. Please fix the labels and retry.')
#else:
#  print('\nEvaluate the NLTK model tags\n')
#  logger.info('\nEvaluate the NLTK model tags\n')
#  score_conllu_file('nltk.conllu.gz', 'input.conllu.gz')


# Convert Spacy OntoNotes labels to Conll03.
#print('\nConvert Spacy output format to conll03.\n')
#logger.info('\nConvert Spacy output format to conll03.\n')
#rv = convert_ontonotes_to_conll('spacy-websm.gz', 'spacy-websm.conllu.gz')
#if rv == False:
#  logger.error('[ERROR]: Convert Failed. Please fix the labels and retry.')
##  print('[ERROR]: Convert Failed. Please fix the labels and retry.')
#else:
#  print('Evaluate Spacy en_core_web_sm model tags\n')
#  logger.info('Evaluate Spacy en_core_web_sm model tags\n')
#  score_conllu_file('spacy-websm.conllu.gz', 'input.conllu.gz')


# Convert Spacy OntoNotes labels to Conll03
#print('\nConvert Spacy output format to conll03.\n')
#logger.info('\nConvert Spacy output format to conll03.\n')
#rv = convert_ontonotes_to_conll('spacy-webmd.gz', 'spacy-webmd.conllu.gz')
#if rv == False:
#  logger.error('[ERROR]: Convert Failed. Please fix the labels and retry.')
#  print('[ERROR]: Convert Failed. Please fix the labels and retry.')
#else:
#  print('\nEvaluate Spacy en_core_web_md model tags\n')
#  logger.info('\nEvaluate Spacy en_core_web_md model tags\n')
#  score_conllu_file('spacy-webmd.conllu.gz', 'input.conllu.gz')


# Convert Spacy OntoNotes labels to Conll03
#print('\nConvert Spacy output format to conll03.\n')
#logger.info('\nConvert Spacy output format to conll03.\n')
#rv = convert_ontonotes_to_conll('spacy-weblg.gz', 'spacy-weblg.conllu.gz')
#if rv == False:
#  logger.error('[ERROR]: Convert Failed. Please fix the labels and retry.')
#  print('[ERROR]: Convert Failed. Please fix the labels and retry.')
#else:
#  print('\nEvaluate Spacy en_core_web_lg model tags\n')
#  logger.info('\nEvaluate Spacy en_core_web_lg model tags\n')
#  score_conllu_file('spacy-weblg.conllu.gz', 'input.conllu.gz')


# Convert Spacy OntoNotes labels to Conll03
#print('\nConvert Spacy output format to conll03.\n')
#logger.info('\nConvert Spacy output format to conll03.\n')
#rv = convert_ontonotes_to_conll('spacy-webtrf.gz', 'spacy-webtrf.conllu.gz')
#if rv == False:
#  logger.error('[ERROR]: Convert Failed. Please fix the labels and retry.')
#  print('[ERROR]: Convert Failed. Please fix the labels and retry.')
#else:
#  print('\nEvaluate Spacy en_core_web_trf model tags\n')
#  logger.info('\nEvaluate Spacy en_core_web_trf model tags\n')
#  score_conllu_file('spacy-webtrf.conllu.gz', 'input.conllu.gz')
