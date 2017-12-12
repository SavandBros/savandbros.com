## Savand Bros main website

[![CircleCI](https://circleci.com/gh/SavandBros/savandbros.svg?style=svg)](https://circleci.com/gh/SavandBros/savandbros)
[![codecov](https://codecov.io/gh/SavandBros/savandbros/branch/master/graph/badge.svg)](https://codecov.io/gh/SavandBros/savandbros)


This code repository holds the source code of Savand Bros Kloud51 main website, reachable at https://kloud51.com
The code base is tiny but it has been created to be minimal as possible, therefore there's not much of code pipeline, review, 
testing etc is involved.

### Setup

Make sure you have the following requirements:

* Python 3.5+
* Git
* Virtualenv (optional)

Clone the repo:

```
git clone git@github.com:SavandBros/kloud51.git && cd kloud51
```

Install dependencies:

```
pip install -r requirements/dev.txt
```

That's all needed to get it installed and configured.

To run local web-server:

```
python manage.py runserver
```


### Deployment

Code deployment to production and staging servers is done via Continuous Integration and Delivery servers, any new commit to master branch branch will be deployed to the production server, so be sure that your latest code works and won't break the production.

You may deploy your code to production server from your local development machine, however you'd need certain envrionment variables required available on your machine.

To deploy from your local machine:

```
fab deploy
```

The command above will deploy the latest code to remote server and you should be able to see the latest code available very soon.


### License

This source code has been distributed under GPLv3 licesne. 
