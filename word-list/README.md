This script pulls the top x most frequently used words from a Wikipedia article. It uses regular expressions and stop word removal to create a cleaned table that we can view with the results

#Installation

The necessary dependencies are in the requirements.txt file so just run this before running the actual code to get them installed

pip install -r requirements.txt

#Usage

There are three arguments. The first is the article you want to retrive words from. The second is a yes/no value that describes whether or not you want to remove stop words
and the last value is the number of words that you want to retrive, is default on 20.

python main.py "your article name here" yes x
