import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as data
import torchvision.transforms as transforms
import torchvision.models as models
import logging
import os
import hydra
from omegaconf import DictConfig
from torch.utils.data import DataLoader
from poutyne.framework import Experiment, EarlyStopping
from poutyne.framework.metrics import F1
from poutyne.utils import set_seeds
from src.models.MLflow_logger import MlFlowWriter


log = logging.getLogger(__name__)


@hydra.main(config_path="../../conf/config.yaml")
def main(cfg: DictConfig) -> None:
    log.info("Init of the training")
    seed = cfg.setting.seed
    set_seeds(seed)
    experiment_name = "DeepTagger-exp"
    writer_callback = MlFlowWriter(experiment_name=experiment_name, config_params=cfg,
                                   root_path=hydra.utils.get_original_cwd())

    log.info("Loading of the dataset and embedding model")
    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    train = DataLoader(data.CIFAR10(root="..\..\data", train=True, download=True, transform=transform), batch_size=cfg.trainer.batch_size)
    val = DataLoader(data.CIFAR10(root="..\..\data", train=False, download=True, transform=transform), batch_size=cfg.trainer.batch_size)


    network = models.resnet18()

    optimizer = optim.Adam(network.parameters(), lr=cfg.trainer.learning_rate)
    loss = nn.CrossEntropyLoss()

    saving_directory = os.path.join(hydra.utils.get_original_cwd(), cfg.poutyne.root_logging_directory,
                                    writer_callback.experiment_id,
                                    writer_callback.run_id)

    monitored_metric = "val_acc"
    monitor_mode = "max"


    experiment = Experiment(directory=saving_directory, network=network, device=cfg.device, optimizer=optimizer,
                            loss_function=loss, batch_metrics=["acc"], epoch_metrics=[F1()],
                            logging=cfg.poutyne.logging, monitor_metric=monitored_metric, monitor_mode=monitor_mode)

    log.info("Start of the training")
    experiment.train(train_generator=train, valid_generator=val, epochs=cfg.trainer.num_epochs,
                     seed=seed, callbacks=[writer_callback])

    log.info("Start of the testing of the trained model")
    test_result = experiment.test(test_generator=val, seed=seed)

    writer_callback.on_test_end(test_result)


if __name__ == '__main__':
    main()