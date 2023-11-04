import logging

import streamlit as st
from langchain import PromptTemplate,  LLMChain

from src.sql_model import TextToSQLModel

logger = logging.getLogger(__name__)


def _load_model():
    """Loads LLM model using LangChain
    """
    try:
        text_sql_pipe = TextToSQLModel()
        return text_sql_pipe
    except Exception as e:
        logger.error(f"Can not load model due to: {e}")
        raise e


def _build_query(model, text_input: str):
    """
    Args:
        model: LLM model loaded using LangChain
        text_input: input text given by the user.
    Return:
        res: SQL generated script from the text input

    """

    template = """
    Translate English to SQL from the prompt below:
    ```{text}```
    """

    prompt = PromptTemplate(
        template=template, input_variables=["text"]
    )

    llm_chain = LLMChain(prompt=prompt, llm=model)
    res = llm_chain.run(text_input)
    return res


def main():
    text_to_sql = _load_model()
    model = text_to_sql.build_model()
    st.title('SQL Script Writing Tool')

    # Sidebar to capture the OpenAi API key
    st.sidebar.title(f"Using {text_to_sql._MODEL_NAME} as model")

    # Captures User Inputs
    prompt = st.text_input(
        'Please describe what you want', key="prompt"
    )  # The box for the text prompt

    submit = st.button("Generate SQL Script for me")

    if submit:
        sql_query = _build_query(
            model=model,
            text_input=prompt
        )
        st.text("Here is your query:")
        st.text(sql_query)


if __name__ == "__main__":
    main()  # Run main Streamlit app.
