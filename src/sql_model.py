import logging
import os
from dotenv import load_dotenv


from huggingface_hub import login
from langchain import HuggingFacePipeline
from transformers import AutoTokenizer
import transformers

from .utils import get_config_params


logger = logging.getLogger(__name__)
load_dotenv()  # load env variables from .env
api_token = os.environ.get("HUGGING_FACE_API_TOKEN")
# Log in to Hugginb face using your token.

login(api_token)  # Hugging face token
logger.info("Logged in Hugging Face")

config = get_config_params()  # Load config


class TextToSQLModel:

    def __init__(
            self,
            save_model: bool = False,
            saving_dir: str = None

    ):
        """Initialize the class

        Args:
            save_model (bool, optional): If true, it saves the model in
            the given saving_dir. Defaults to False.
            saving_dir (str, optional): path to save the model.
            Ignored in save_model is false. Defaults to None.
        """
        self.save_model = save_model
        self.saving_dir = saving_dir
        self._MODEL_NAME = config["pipeline_params"]["model"]
        logger.info(f"Using {self._MODEL_NAME} model")
        self.tokenizer = self._get_tokenizer_from_model
        # Model params from config
        self.model_params = config["pipeline_params"]
        self.model_kwargs = config.get("model_kwargs")

    @property
    def _get_tokenizer_from_model(self):
        return AutoTokenizer.from_pretrained(
            self._MODEL_NAME
        )

    def _build_model_pipeline(self):
        print(self.model_params)
        pipeline = transformers.pipeline(

          **self.model_params
        )
        if self.save_model:
            self._save_pipeline(pipeline)
        return pipeline

    def build_model(self):
        """Build the Hugging Face pipeline

        Returns:
            Llm Pipeline
        """
        llm = HuggingFacePipeline(
            pipeline=self._build_model_pipeline(),
            model_kwargs={
                **self.model_kwargs
            }
        )
        return llm

    def _save_pipeline(self, pipeline):
        pipeline.save_pretrained(self.saving_dir)
        logger.info(f"Model saved at {self.saving_dir}")
