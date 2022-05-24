# CM repository to bridge MLOps and DevOps

[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/cm)


It is becoming very challenging to co-design, optimize and deploy efficient AI Systems in the real world:
["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess).

However, [our experience](https://doi.org/10.5281/zenodo.6475385) 
suggests that it is possible to [apply DevOps principles to MLOps](https://www.datanami.com/2022/03/30/birds-arent-real-and-neither-is-mlops/)
if we treat all AI, ML and Systems artifacts including models, data sets, frameworks, libraries and scripts as "code" meta packages 
with dependencies on other artifacts, operating systems and hardware.

We are prototyping [CM-based](https://github.com/mlcommons/ck/tree/master/cm) 
automations to convert ad-hoc scripts and artifacts into "intelligent components"
that can modularize AI, ML and other complex applications and automatically
adapt them to diverse and rapidly evolving software and hardware stacks.

For example, we use IC to enable collaborative, deterministic and reproducible benchmarking, co-design, optimization and deployment 
of AI and ML Systems. across continuously changing software, hardware, models and data sets.



# How to use

## Install CM toolkit and dependencies

Install the CM toolkit as described [here](https://github.com/mlcommons/ck/blob/master/cm/docs/installation.md).

## Install this CM repository

Use CM to install this repository on your system:

```bash
$ cm pull repo octoml@cm-mlops
```

You can now list available intelligent components (IC) as follows:
```bash
$ cm list ic
```

You can run any IC as follows:
```bash
$ cm run ic {IC name or UID}
```


## Check tutorials

Follow the [IC tutorial](https://cknowledge.org/docs/cm/tutorial-ic.html) to understand IC concepts.



# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)


