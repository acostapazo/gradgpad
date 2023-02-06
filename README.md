# gradgpad 🗿 [![version](https://img.shields.io/github/release/acostapazo/gradgpad/all.svg)](https://github.com/acostapazo/gradgpad/releases) [![ci](https://github.com/acostapazo/gradgpad/workflows/ci/badge.svg)](https://github.com/acostapazo/gradgpad/actions) [![pypi](https://img.shields.io/pypi/dm/gradgpad)](https://pypi.org/project/gradgpad/) [![codecov](https://codecov.io/gh/acostapazo/gradgpad/branch/main/graph/badge.svg?token=HXTGF8ZBJ7)](https://codecov.io/gh/acostapazo/gradgpad)



👉  The GRAD-GPAD framework is a comprehensive and modular framework to evaluate the performance of face-PAD (face Presentation Attack Detection) approaches in realistic settings, enabling accountability and fair comparison of most face-PAD approaches in the literature.

🙋  GRAD-GPAD stand for Generalization Representation over Aggregated Datasets for Generalized Presentation Attack Detection.

## 🤔 Abstract 

Face recognition technology is now mature enough to reach commercial products, such as smart phones or tablets. However, it still needs to increase robustness against imposter attacks. In this regard, face Presentation Attack Detection (face-PAD) is a key component in providing trustable facial access to digital devices. Despite the success of several face-PAD works in publicly available datasets, most of them fail to reach the market, revealing the lack of evaluation frameworks that represent realistic settings. Here, an extensive analysis of the generalisation problem in face-PAD is provided, jointly with an evaluation strategy based on the aggregation of most publicly available datasets and a set of novel protocols to cover the most realistic settings, including a novel demographic bias analysis. Besides, a new fine-grained categorisation of presentation attacks and instruments is provided, enabling higher flexibility in assessing the generalisation of different algorithms under a common framework. As a result, GRAD-GPAD v2, a comprehensive and modular framework is presented to evaluate the performance of face-PAD approaches in realistic settings, enabling accountability and fair comparison of most face-PAD approaches in the literature.


## 🙏 Acknowledgements

If you use this framework, please cite the following publication:

```
@article{https://doi.org/10.1049/bme2.12049,
author = {Costa-Pazo, Artur and Pérez-Cabo, Daniel and Jiménez-Cabello, David and Alba-Castro, José Luis and Vazquez-Fernandez, Esteban},
title = {Face presentation attack detection. A comprehensive evaluation of the generalisation problem},
journal = {IET Biometrics},
volume = {10},
number = {4},
pages = {408-429},
doi = {https://doi.org/10.1049/bme2.12049},
url = {https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/bme2.12049},
eprint = {https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/bme2.12049},
abstract = {Abstract Face recognition technology is now mature enough to reach commercial products, such as smart phones or tablets. However, it still needs to increase robustness against imposter attacks. In this regard, face Presentation Attack Detection (face-PAD) is a key component in providing trustable facial access to digital devices. Despite the success of several face-PAD works in publicly available datasets, most of them fail to reach the market, revealing the lack of evaluation frameworks that represent realistic settings. Here, an extensive analysis of the generalisation problem in face-PAD is provided, jointly with an evaluation strategy based on the aggregation of most publicly available datasets and a set of novel protocols to cover the most realistic settings, including a novel demographic bias analysis. Besides, a new fine-grained categorisation of presentation attacks and instruments is provided, enabling higher flexibility in assessing the generalisation of different algorithms under a common framework. As a result, GRAD-GPAD v2, a comprehensive and modular framework is presented to evaluate the performance of face-PAD approaches in realistic settings, enabling accountability and fair comparison of most face-PAD approaches in the literature.},
year = {2021}
}
```


This publication has been financed by the "Agencia Estatal de Investigación. Gobierno de España"  ref. `DIN2019-010735 / AEI / 10.13039/501100011033`


## 💻 Installation

```console
pip install gradgpad
```

## 🚀 Getting Started

The best way to learn how to use the GRAD-GPAD framework is through the Notebook examples available in:

*  [gradgpad-notebooks](https://github.com/acostapazo/gradgpad-notebooks) 📔 

## 📺 Video Tutorial

[![Tutorial](https://img.youtube.com/vi/y5lQox0hmGU/0.jpg)](https://www.youtube.com/watch?v=y5lQox0hmGU)


## 👍 Annotations

Labels and annotations are available through the Python package. 

Example:

```python
from gradgpad import annotations
print(f"Total GRAD-GPAD Annotations: {annotations.num_annotations}")
print(annotations.annotated_samples[0])
annotations.print_semantic(annotation_index=0)
```

These annotations are also publicly available in [json file](https://github.com/acostapazo/gradgpad/blob/master/gradgpad/data/gradgpad_annotations.json).

## 📰 Reproducible Research

```console
$ gradgpad --reproducible-research -o <output-folder> 
```

Use `gradgpad --help` to check available parameter

```
$ gradgpad --help                         
usage: gradgpad [-h] [--reproducible-research] [--zip]
                [--output-path OUTPUT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --reproducible-research, -rr
                        Create a folder with reproducible research results
  --zip, -z             Zip result folder
  --output-path OUTPUT_PATH, -o OUTPUT_PATH
                        Output path
```

## ❓ FAQ

#### Is it necessary to have all data sets to test framework?

No, it is not necessary, although the more datasets you add to the test, the greater the statistical significance of 
your evaluation set. 

From the paper:

> "The unified categorisation added in GRAD-GPAD v2 brings the opportunity both to create novel protocols and to visualise the results from different perspectives. Also, the extended GRAD-GPAD v2 dataset allows a better statistical significance of the results of previous protocols, leveraging their added-value for assessing face-PAD generalisation on current and future algorithms."

> **Note**
> Even if you only have access to a few datasets, you can take advantage of annotations and perform tests on your datasets.
> ```python
> from gradgpad import annotations
> 
> my_datasets = ["replay-mobile", "replay-attack"]
> 
> 
> selected_annotations = annotations.get_annotations_filtered_by_datasets(my_datasets)
> ```


#### I want to evaluate my own algorithms in the GRAD-GPAD framework? How should I start?

We strongly recommend using the python client for easy access to the annotations (available in a json file [here](https://github.com/acostapazo/gradgpad/blob/main/gradgpad/data/gradgpad_annotations.json)). 
Integrate your algorithm and define a score file format compatible with GRAD-GPAD (examples in [scores](https://github.com/acostapazo/gradgpad/tree/main/gradgpad/data/scores)), so you can use the available evaluation tools.

```mermaid
flowchart LR
    subgraph GRAD-GPAD Dataset Annotations
    gradgpad_annotations.json
    python(Python client)
	end

    Algorithm

    subgraph Evaluation
    scores_format(Scores Format)
    tools(GRAD-GPAD Evaluation tools)
    end

    gradgpad_annotations.json --> python
    python --> Algorithm
    Algorithm --> scores_format
    scores_format --> tools
```

> **Note**
> The following code could help you to integrate your algorithm:
>
>```python
>from gradgpad import annotations
>
>my_datasets = {
>    "replay-mobile": "/Users/username/datasets/replay-mobile",  # set path to your dataset
>    "replay-attack": "/Users/username/datasets/replay-attack",  # set path to your dataset
>}
>selected_annotations = annotations.get_annotations_filtered_by_datasets([*my_datasets])
>
>for annotation in selected_annotations:
>    filename = f"{my_datasets.get(annotation.dataset.value)}/{annotation.media}"
>    print(f"{filename=}")
>
>    # load the media file
>
>    # perform your algorithm
>
>    # save to a file like this {annotation.media: score}
>    # like in https://github.com/acostapazo/gradgpad/tree/main/gradgpad/data/scores/auxiliary
>    # once you have the score files, you can use the evaluation tools
>    # check notebooks in https://github.com/acostapazo/gradgpad-notebooks
>```


## 🤔 Contributing

There is a lot of work ahead (adding new categorizations, datasets, improving documentation...), feel free to add and propose any improvements you can think of! If you need help getting started, don't hesitate to contact us ✌️

* 🛠️ Environment

```console
>> python -m venv venv
>> source venv/bin/activate
(venv) >> pip install lume
(venv) >> lume -install
```

* ✅ Testing

```console
(venv) >> lume -test
```

