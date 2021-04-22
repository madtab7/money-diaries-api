# Money Diaries API

A Django app for money diaries

## Stack

- Python 3
- Django 3.1

## Getting Started

First install Python:

```sh
brew install python
```

This app runs on Python 3 so make sure you that is installed by running:

```sh
$ python -V
Python 3.7.3
```

### Create Virtual Environment

Once you have Python installed you'll need to start a virtual environment.

In the root folder run:

```sh
virtualenv venv
```

This will create a `./venv` folder in the root directory. Then activate it:

```sh
source venv/bin/activate
```

To deactivate the virtual environment, run:

```sh
deactivate
```

### Install Dependencies

Install required dependencies with:

```sh
pip install -r requirements.txt
```

### Initial Migrations

Before starting the app for the first time you'll need to run some initial migrations for the admin panel to function. In the root directory run:

```
python manage.py migrate
```

After that succeeds, create a default user so that you can login to the admin panel:

```
python manage.py createsuperuser
```

### Start Server

```
python manage.py runserver
```

This will spin up the app at `localhost:8000`.

## Admin panel

To login to the admin panel, go to to `localhost:8000/admin` and login with the credentials you specified above.

## API

This app uses [django-rest-framework](https://www.django-rest-framework.org/) and [drf-spectacular](https://drf-spectacular.readthedocs.io/) to maintain and generate the API schema and documentation.

To view API documentation, go to `localhost:8000/`.

To update the API schema definition:

```
manage.py spectacular --file schema.yml
```

## Deploying

This application is hosted on [AWS ElasticBeanstalk](https://console.aws.amazon.com/elasticbeanstalk). To interact with ElasticBeanstalk locally you can install the [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html).

The local configuration for deployment lives in the `.elasticbeanstalk` directory. If you don't have this directory you can create one and associate it with the existing ElasticBeanstalk app environment:

```sh
eb init --profile {your-aws-profile}
```

This will prompt you to select the region (us-east-1) and the application environment (you can choose "no" when it asks about CodeCommit).

On success it should create a `.elasticbeanstalk` directory in the root folder with a `.config.yml` file.

When you're ready to deploy run:

```
eb deploy --profile {your-aws-profile}
```

More EB deploy commands available [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-deploy.html)

## Scraping/Seeding Data

To seed the database with Refinery29's Money Diary entries, this app uses Google Sheets / Google Drive to extract data. Once data has been scraped into a Google Sheet, the GoogleScript can be executed to return formatted json data.
