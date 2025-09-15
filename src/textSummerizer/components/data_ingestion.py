import os
import urllib.request as request
import zipfile
from src.textSummerizer.logging import logger
from textSummerizer.utils.common import get_size
from textSummerizer.entity.config_entity import DataIngestionConfig
from pathlib import Path



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded ! with following info {headers}")
        else:
            logger.info(f"file alredy exists of size: {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)