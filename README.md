# slack-exporter
Export data from Slack as a non-admin user. This script uses Slack's API to
export history from each channel chunk by chunk.

Note that the format of channel logs is JSON, not NDJSON. We should probably
make it possible to output NDJSON using a command line option. There are many
things that would be nice to have so feel free to contribute and submit pull
requests.

## Usage
Generate a test Slack API token [here](https://api.slack.com/web) and put it in
a file called `./env` like this: 
```
export SLACK_TOKEN=xoxp-123456...
```
Then every time you start your shell just `cd` into this directory, do `source
./env` and  run the exporter with your desired options.

```sh
./slack-exporter --min-members 17 --date-start 2016-06-01
```

Find more options in `./slack-exporter -h`.

## Development setup
```sh
pyenv virtualenv 3.5.0 slack-exporter
pyenv local slack-exporter
```
