# Reuse Analysis: EarthVQA

## Dataset Chosen

I chose EarthVQA for this task.

EarthVQA is a remote sensing visual question answering dataset. It uses satellite images with questions and answers. This makes it similar to the type of work needed for disaster image analysis.

## Reusable Design Pattern

One useful pattern is the image, question, and answer format.

Each sample can have:

- image path
- question
- answer
- task type

This format is simple and easy to reuse.

## How It Fits the Framework

This pattern fits the dataset interface I proposed.

If DisasterM3 and EarthVQA both return data in a similar format, then the evaluator does not need to change for every dataset.

The dataset loader prepares the sample. The model runner uses the image and question. Then the evaluator compares the model answer with the correct answer.

## Why This Is Useful

This makes the framework easier to extend.

Instead of changing the whole code when adding a new dataset, we can only add a new dataset loader.

This also makes model comparison easier because different datasets can follow the same general evaluation flow.