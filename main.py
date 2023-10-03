from src.NLPtc import logger
from src.NLPtc.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.NLPtc.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from src.NLPtc.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_in = DataIngestionTrainingPipeline()
    data_in.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_val = DataValidationTrainingPipeline()
    data_val.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e