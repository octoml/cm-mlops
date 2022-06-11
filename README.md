# CM repository with automations to bridge MLOps and DevOps

[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/cm)


It is becoming very challenging to co-design, optimize and deploy efficient AI Systems in the real world:
["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess).

However, [our experience](https://doi.org/10.5281/zenodo.6475385) 
suggests that it is possible to [apply DevOps principles to MLOps](https://www.datanami.com/2022/03/30/birds-arent-real-and-neither-is-mlops/)
if we organize all AI, ML and Systems artifacts including models, data sets, frameworks, libraries, tools and scripts as
a database of unified components with a common API and extensible meta description that describe 
dependencies on other artifacts, operating systems and hardware.

We are prototyping [CM-based](https://github.com/mlcommons/ck/tree/master/cm) 
automations to convert native user scripts and artifacts into portable CM scripts
that can help to modularize AI, ML and other complex applications and automatically
adapt them to diverse and rapidly evolving software and hardware stacks.

For example, we use CM scripts to enable collaborative, deterministic and reproducible benchmarking, co-design, optimization and deployment 
of AI and ML Systems. across continuously changing software, hardware, models and data sets.



# How to use

## Install CM toolkit and dependencies

Install the CM toolkit as described [here](https://github.com/mlcommons/ck/blob/master/cm/docs/installation.md).

## Install this CM repository

Use CM to install this repository on your system:

```bash
$ cm pull repo octoml@cm-mlops
```

You can now list available CM scripts as follows:
```bash
$ cm list script
```

You can run any CM script as follows:
```bash
$ cm run script {CM script alias or UID}
```


## Check tutorials

Follow the [CM scripts tutorial](https://cknowledge.org/docs/cm/tutorial-scripts.html) to understand CM concepts.



# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
