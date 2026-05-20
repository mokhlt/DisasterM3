# DisasterM3 Repository Analysis

## Current Repository Structure

The DisasterM3 repository is a small Python project for running benchmark experiments on the DisasterM3 dataset.

The main files and folders are:

- `models/`: contains model-related code.
- `pyscripts/`: contains scripts used to run the benchmark.
- `README.md`: explains the project and gives example commands.
- `__init__.py`: makes the folder work as a Python package.

From the README, the main workflow seems to be running a script such as `run_vllm.py` with a selected model and subset.

## Code Organization Analysis

The current repo is useful as a reference because it gives a direct way to run the DisasterM3 benchmark.

However, the structure looks more focused on running DisasterM3 itself instead of being a general framework for many disaster datasets.

The code does not clearly separate the dataset loading, model running, evaluation, and experiment tracking into independent parts.

## Is the Framework Tied to a Specific Dataset?

Yes, the current workflow seems mainly tied to the DisasterM3 dataset.

To use another dataset, such as EarthVQA or MONITRS, the code would need a clear dataset interface. Each dataset should be loaded in the same format so the rest of the framework does not need to change.

For example, every dataset loader should return samples with fields like:

- image path
- question or prompt
- ground truth answer
- task type
- metadata

This would make it easier to add more datasets later.

## Identified Limitations

Some limitations I noticed are:

- There is no common `BaseDataset` class.
- Dataset loading is not clearly separated from the benchmark workflow.
- There is no clear model runner interface.
- Switching models depends on script arguments, not a full config system.
- Evaluation logic is not clearly separated by task type.
- There is no clear experiment tracking layer such as MLflow or W&B.
- Adding another dataset would likely require changing the code instead of only adding a new adapter.

## Proposed Modular Redesign

A better structure would follow this flow:

Dataset -> Model Runner -> Evaluator -> Experiment Tracker

The proposed structure could be:

- `datasets/base.py`: contains a `BaseDataset` class.
- `datasets/disasterm3.py`: loads DisasterM3 data.
- `models/base.py`: contains a base model runner.
- `evaluation/`: contains evaluators for VQA, classification, damage assessment, and counting.
- `configs/`: stores YAML config files for dataset, model, and task settings.
- `experiments/tracker.py`: logs experiment results and metrics.

## How This Helps

This design makes the framework easier to extend.

The evaluator should not care which dataset or model is being used. The dataset loader should prepare the data in a common format, and the model runner should return predictions in a common format.

This makes it possible to switch datasets or models using a config file instead of editing the main evaluation code.