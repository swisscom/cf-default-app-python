# CF Default App Python

The default Python app that will be pushed in the Swisscom Application Cloud if no source code is provided.

Based on [Flask](http://flask.pocoo.org/)

## Run locally

1. Install [Python](http://docs.python-guide.org/en/latest/starting/installation/)
1. Run `pip install -r requirements.txt`
1. Run `python app.py`
1. Visit [http://localhost:3000](http://localhost:3000)

## Run in the cloud

1. Install the [cf CLI](https://github.com/cloudfoundry/cli#downloads)
1. Run `cf push --random-route`
1. Visit the given URL

## Create ZIP

1. Run `zip -r python_app.zip static templates app.py Procfile requirements.txt`
