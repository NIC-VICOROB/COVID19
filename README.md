# COVID19

Resources for COVID-19 detection using medical imaging and deep
learning.

## Background

*Background extracted from
[here](https://github.com/ieee8023/covid-chestxray-dataset)*

The 2019 novel coronavirus (COVID-19) presents several unique features. While the diagnosis is confirmed using polymerase chain reaction (PCR), infected patients with pneumonia may present on chest X-ray and computed tomography (CT) images with a pattern that is only moderately characteristic for the human eye [Ng, 2020](https://pubs.rsna.org/doi/10.1148/ryct.2020200034). COVID-19’s rate of transmission depends on our capacity to reliably identify infected patients with a low rate of false negatives. In addition, a low rate of false positives is required to avoid further increasing the burden on the healthcare system by unnecessarily exposing patients to quarantine if that is not required. Along with proper infection control, it is evident that timely detection of the disease would enable the implementation of all the supportive care required by patients affected by COVID-19.

## Motivation

*Background extracted from
[here](https://github.com/ieee8023/covid-chestxray-dataset)*

While PCR tests offer many advantages they are physical things that require shipping the test or the sample. X-ray machines can be plugged in to screen patients as long as they have electricity.

Imagine a future where we run out of tests and then the majority of radiologists get sick. AI tools can help general practitioners to triage and treat patients.

## What is the goal?

Different goals are envisioned for this particular project:

* Being able to differentiate the COVID-19 disease from both bacterial
  and viral pneumonia.

* Being able to predict the worsening of the patient in time using
  longitudinal studies.

* __Being able to provide suitable tools to the medical
    community__.


##  Dataset resources

So far, these are the available datasets related to COVID-19 related
to X-ray and CT images.

* [Open source github dataset](https://github.com/ieee8023/covid-chestxray-dataset)
* [Kaggle RSNA pneumonia dataset](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge)
* [Kaggle COMS COVID-19 competition (private?)](https://www.kaggle.com/c/4771-sp20-covid/overview)


## Related literature

Please find the related literature [here](./literature.md),
covering scientific related literature and interesting blog posts.

## Available models

Please find the related existing models and implementations [here](./models.md).


## Best practices
* Fork this repository to add your contributions and add a pull
  request to update it.
* Develop your methods in Jupyter Notebooks if possible.
* Please provide a way to download your data in order to replicate the
  results as much as possible.
* All models should be placed inside the `models` folder.
* Create a new folder with your model, adding a `requeriments.txt` if
  necessary.
* Document your findings.
* Use graphical figures and explanatory analysis when possible.
* Use [issues](https://github.com/NIC-VICOROB/COVID19/issues)
    extensively.
* Sync the tasks between the members of the group with [this project template](https://github.com/NIC-VICOROB/COVID19/projects/1?add_cards_query=is%3Aopen).



## Contact
Contact: [Sergi Valverde, Postodoctoral researcher, University of
Girona, Spain](https://github.com/sergivalverde).
