import logging

import pandas as pd
from metaflow import S3, FlowSpec, Parameter, step

from . import __version__

logger = logging.getLogger("{{ cookiecutter.repo_name }}.inference_flow")


class InferenceFlow(FlowSpec):

    model_name = Parameter("model_name", type=str, required=True, default="expert_transaction_matching")
    model_stage = Parameter("model_stage", type=str, required=True, default='Production')
    version = Parameter("version", type=str, default=__version__)
    s3_bucket = Parameter("bucket", type=str, required=True)
    s3_candidates_path = Parameter("s3_in_key", type=str, required=True)
    s3_out = Parameter("s3_out_key", type=str, required=True)

    @step
    def start(self):
        logger.info(f"Startomg inference at {pd.Timestamp.now():%Y-%m-%d %H:%M:%S}")
        self.next(self.pull_candidates)

    @step
    def pull_candidates(self):
        print("the data artifact is: %s" % self.my_var)

        with S3() as s3:
            tmp_data_path = s3.get(self.s3_candidates_path)
            local_path = tmp_data_path.path
            self.candidates = pd.read_parquet(local_path)

        logger.info(f"Pull candidates from s3: {len(self.candidates):,d}")

        self.next(self.pull_model)

    @step
    def pull_model(self):
        from zgny_aip_mlflow import get_model

        loaded_model = get_model(
            model_name=self.model_name, model_stage=self.model_stage
        )

        self.model = loaded_model._model_impl.sklearn_model
        logger.info(f"Pull model from Mlflow: {self.model_name=} {self.model_stage=}")

        self.next(self.inference)

    @step
    def inference(self):
        self.candidates["probability"] = self.model.predict_proba(self.candidates)[:, 1]
        self.candidates["model"] = self.model.name
        self.candidates["scored_at"] = pd.Timestamp.now()

        logger.info(
            f"Ran Inference on {len(self.candidates):,d} candidates, of those {(self.candidates['probability'] > 0.81).sum():,d} are likely matches"
        )
        logger.info(f"outputting to s3: {self.s3_out}")

        with S3() as s3:
            s3.put(self.s3_out, self.candidates, overwrite=True)

        self.next(self.end)

    @step
    def end(self):
        logger.info(f"Done with inference at {pd.Timestamp.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    InferenceFlow()
