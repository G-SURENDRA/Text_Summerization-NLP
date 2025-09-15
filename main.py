from textSummerizer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from textSummerizer.logging import logger


STAGE_NAME="Data Ingestion"
try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed \n\n>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


