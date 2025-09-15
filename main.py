from textSummerizer.pipeline.stage01_data_ingestion import DataIngestionPipeline
from textSummerizer.logging import logger
from textSummerizer.pipeline.stage02_data_validation import DataValidationPipeline
from textSummerizer.pipeline.stage03_data_transformation import DataTransformationPipeline


STAGE_NAME="Data Ingestion"
try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed \n\n>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Data Validation"
try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    data_validation=DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed \n\n>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation"
try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed \n\n>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


