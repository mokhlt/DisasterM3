# VLM Evaluation Methodology

Vision-Language Models are models that work with both images and text. They can look at an image and answer a question, describe what is happening, or choose a label.

In disaster analysis, the image can be a satellite image, drone image, or any image from an affected area. The text part can be a question or prompt.

For example:

What disaster is shown in the image?

Are there damaged buildings?

Is the area flooded?

How many buildings are affected?

The model gives an answer, then this answer is compared with the correct answer in the dataset.

## Type of Data

A VLM evaluation dataset usually includes images and text questions. It also includes the correct answers or labels.

In some tasks, the answer is a class, like flood, wildfire, earthquake damage, or no damage.

In other tasks, the answer can be yes or no, a short text answer, or a number.

## Evaluation Metrics

The metric depends on the task.

For classification, accuracy can be used to check how many answers were correct.

For yes or no questions, accuracy can also be used.

For VQA tasks, the predicted answer can be compared with the ground truth answer. This can be done using exact match or answer similarity.

For counting tasks, the predicted number can be compared with the correct number.

For damage assessment, the model can be checked based on whether it predicted the correct damage level.

## Why This Matters

Evaluation is important because it shows if the model is actually useful. A model might work well on normal images but perform worse on satellite images or disaster images.

Using the same evaluation method makes it easier to compare different models fairly.