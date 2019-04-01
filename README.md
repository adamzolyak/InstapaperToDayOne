# Instapaper To Day One

A script to format weekly highlights from Instapaper and add them to Day One as a new journal entry.

## Preqrequisites

- [Python 3](https://www.python.org/downloads/) in installed on OS X.
- [Day One](https://dayoneapp.com/) v2 is installed on OS X.
- The [Day One CLI v2](https://help.dayoneapp.com/tips-and-tutorials/command-line-interface-cli) is installed on OS X. [Install](https://help.dayoneapp.com/tips-and-tutorials/command-line-interface-cli) the Day One CLI v2 by running `sudo bash /Applications/Day\ One.app/Contents/Resources/install_cli.sh`.

## Running The Script

1. Create a `import.txt` file in this directory containing the Instapaper highlights to be imported. Copy and paste from the IFTTT email. See format details below. Configured to work with the format of [this IFFF recipe's email](https://ifttt.com/applets/75192374d-send-a-weekly-digest-of-my-instapaper-highlights).
1. Run `python3 import.py` to import the entries.
1. Verify the import was successful by checking the summary printed at the end of the script `Summary: Created new journal entry with 39 highlights...`.

## Format of Import File (journal.txt)

Note: Line spacing and multiple lines don't matter.

```
Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

"It is going to have an impact the size of the impact of the internet, or as Andrew Ng suggests, the impact of electricity. It is going to affect every industry, and leaders of every type of organization are going to be wishing that they had looked into it sooner."

Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

March 18, 2019 at 03:54PM

via Instapaper https://ift.tt/2W8MATH March 18, 2019 at 03:54PM
via Instapaper https://www.fast.ai/2016/11/17/not-all-the-same/

Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

"It is going to have an impact the size of the impact of the internet, or as Andrew Ng suggests, the impact of electricity. It is going to affect every industry, and leaders of every type of organization are going to be wishing that they had looked into it sooner."

Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

March 18, 2019 at 03:54PM

via Instapaper https://ift.tt/2W8MATH March 18, 2019 at 03:54PM
via Instapaper https://www.fast.ai/2016/11/17/not-all-the-same/

Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

"It is going to have an impact the size of the impact of the internet, or as Andrew Ng suggests, the impact of electricity. It is going to affect every industry, and leaders of every type of organization are going to be wishing that they had looked into it sooner."

Please Don't Say "It used to be called big data and now it's called deep learning" · fast.ai

March 18, 2019 at 03:54PM

via Instapaper https://ift.tt/2W8MATH March 18, 2019 at 03:54PM
via Instapaper https://www.fast.ai/2016/11/17/not-all-the-same/
```

Adjust the import script as needed to match different import formats.

## License

ISC © 2019 Adam Zolyak adam@tinkurlab.com (www.tinkurlab.com)
