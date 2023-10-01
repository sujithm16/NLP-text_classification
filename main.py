from src.NLPtc import logger
from src.NLPtc.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_in = DataIngestionTrainingPipeline()
    data_in.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e