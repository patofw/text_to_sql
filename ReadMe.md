# Text-to-SQL App
Welcome to the Text-to-SQL mock app. 

## Installation

`git clone` this repo. 

create a Python virtual environment (recommended)

run `python setup.py` to install dependencies.


To make it work simply: 
 
1. Make sure you get your API Token set in https://huggingface.co/. Explore your prefered model to use.
LLAMA2 is recommended (requires additional permission from META for usage).
However, the configuration is set up by default for the `"mrm8488/t5-base-finetuned-wikiSQL"` model. 
1. Once a model is selected, add your API key in the .env file. (It is recommended to use a secret manager for this)
2. Set up the right configurations for your model if necessary in the ```config.yaml``` file.
3. You can either run the app using streamlit by:
    ````streamlit run app.py ````
4. or, follow the [#Text-to-SQL-step-by-step.ipynb] for a quick tutorial (configurations are loaded directly in the Notebook).

This code is intended to have an easy to deploy quick demo app to showcase text-to-sql capabilities.

The quality of the the response depends heavily in the model chosen. 