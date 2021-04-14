# The GRAD-GPAD framework 🗿 [![version](https://img.shields.io/github/release/acostapazo/gradgpad/all.svg)](https://github.com/acostapazo/gradgpad/releases) [![ci](https://github.com/acostapazo/gradgpad/workflows/ci/badge.svg)](https://github.com/acostapazo/gradgpad/actions) [![pypi](https://img.shields.io/pypi/dm/gradgpad)](https://pypi.org/project/gradgpad/)


👉 The GRAD-GPAD framework is a comprehensive and modular framework to evaluate the performance of face-PAD (face Presentation Attack Detection) approaches in realistic settings, enabling accountability and fair comparison of most face-PAD approaches in the literature.

🙋 GRAD-GPAD stand for Generalization Representation over Aggregated Datasets for Generalized Presentation Attack Detection


## 💻 Installation

```console
pip install gradgpad
```

## 🚀 Getting Started

The best way to learn how to use the GRAD-GPAD framework is through the Notebook 📔 examples available in [gradgpad-notebooks](https://github.com/acostapazo/gradgpad-notebooks).

An example video using the framework will be available soon.

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

## 🤔 Contributing

There is a lot of work ahead (adding new categorizations, datasets, improving documentation...), feel free to add and propose any improvements you can think of! If you need help getting started, don't hesitate to contact us :)

* 🛠️ Environment

```console
>> conda create -n grad-gpad python=3.6
>> conda activate grad-gpad
(grad-gpad) >> pip install lume
(grad-gpad) >> lume -install
```

* ✅ Testing

```console
(grad-gpad) >> lume -test
```

