# Named Entity Recognition (NER) with spaCy, nltk, and stanza

This repository demonstrates the implementation of Named Entity Recognition (NER) parsers using three popular NLP libraries: [**spaCy**](https://spacy.io/), [**nltk**](https://www.nltk.org/), and [**stanza**](https://stanfordnlp.github.io/stanza/). The project focuses on parsing and evaluating named entities from pre-parsed text data while ensuring proper token alignment.

---

## Project Overview

Named Entity Recognition is a fundamental task in Natural Language Processing (NLP) that involves identifying and classifying entities in text into predefined categories such as:

- People
- Locations
- Organizations
- Dates
- Quantities

This project includes:
1. Implementation of NER parsers using multiple models across three libraries.
2. Evaluation of model performance using metrics such as precision, recall, and F1 scores.
3. Comparison of models based on evaluation results.

---

## Features

- Prepares data for NER tasks to ensure compatibility across libraries.
- Supports evaluation of seven different NER models:
  - Four models from spaCy
  - One model from nltk
  - Two models from stanza
- Provides a streamlined framework for debugging, testing, and evaluation.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/justarandomnameduh/ner-pipeline.git
   cd ner-pipeline
   ```

2. **Set Up the Environment and Dependencies**:
   - Install [Anaconda](https://www.anaconda.com/) if not already installed.
   - Create a virtual environment:
     ```bash
     conda create -n "YOUR_ENV" python=3.8
     conda activate YOUR_ENV
     pip install jupyterhub notebook tqdm numpy spacy spacy_transformers scikit-learn nltk stanza matplotlib ipywidgets
     ```

4. **Download Models**:
   - Download models for spaCy, nltk, and stanza as needed. (_`get_all_models()` function already handle this_)
     
---

## Usage

### 1. Run Parsers on Sample Data
For initial development and testing, use the sample data files:
- **sample.txt.gz**: Input sentences
- **sample.conllu.gz**: Gold labels for evaluation

### 2. Full Dataset Parsing
After validating the parsers with the sample data, process the full dataset, which may take up to an hour on standard laptops.

### 3. Evaluate and Compare Models
Run the included evaluation functions to compute metrics and tabulate results for the seven models.

---

## File Structure

- **NER.ipynb**: Main notebook containing implementation and evaluation.
- **sample.txt.gz**: Sample input text file.
- **input.txt.gz**: Full input text file.
- **sample.conllu.gz**: Sample gold labels file.
- **input.conllu.gz**: Full gold labels file.
- **requirements.txt**: Project dependencies.
- **tag_converter.py**: Helper functions for converting tags.

---

## Key Highlights

- **Focus on Alignment**: The pre-parsed input requires "white space" tokenization to avoid misalignment during evaluation.
- **Convenience Functions**: Provided utilities streamline logging, format conversion, and output file writing.
- **Evaluation-Ready**: Automated evaluation ensures consistent and reliable metric computation.

---

## Results

| Model | F1(PER) | F1(MISC) | F1(LOC) | F1(ORG) | F1(Macro AVG) | OvA AUC |
| --- | --- | --- | --- | --- | --- | --- |
| Stanza | 0.92 | 0.76 | **0.86** | 0.73 | 0.82 | 0.89 |
| NLTK | 0.73 | 0.01 | 0.56 | 0.49 | 0.45 | 0.70 |
| spaCy-sm | 0.79 | 0.62 | 0.73 | 0.64 | 0.69 | 0.80 |
| spaCy-md | 0.86 | 0.67 | 0.79 | 0.68 | 0.75 | 0.84 |
| spaCy-lg | 0.87 | 0.69 | 0.79 | 0.70 | 0.76 | 0.85 |
| spaCy-tr | **0.96** | **0.81** | **0.86** | **0.86** | **0.87** | **0.92** |

---

## Contributions

Quang Minh Tien Nguyen @justarandomnameduh
