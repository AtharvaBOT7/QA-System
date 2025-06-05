from llama_index.core.readers import SimpleDirectoryReader
import sys
import os
from exception import customexception
from logger import logging

def load_data(data):
    try:
        logging.info("Data Loading Started...")
        loader = SimpleDirectoryReader("Data")
        documents = loader.load_data()
        logging.info("Data Loading Completed...")
        return documents
    
    except Exception as e:
        logging.info("Exception in loading the data...")
        raise customexception(e, sys)
    
    