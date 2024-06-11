### Running on Heroku ###
- Run the below command in your terminal, replacing <num_of_entries> with the amount of words you want in the string, and <path_to_file> with a path to the local txt file.
`curl -s -X POST "https://count-words-20ffa665a447.herokuapp.com/word_count/?num_of_entries=<number_of_entries>" -F "file=@<path_to_file>" | sed 's/\\n/\n/g'`


- To test, run `curl -s -X POST "https://count-words-20ffa665a447.herokuapp.com/run-tests/`


### Running Locally ###
Install requirements:
`pip install -r requirements.txt`

To count words:
- Run python main.py to run the server locally
- Run the below command to post a local file to the endpoint:

`curl -s -X POST "http://0.0.0.0:8000/word_count/?num_of_entries=<number_of_entries>" -F "file=@<path_to_file>" | sed 's/\\n/\n/g'`

Replace <number_of_entries> to the amount of words and their counts you would like to see.

Replace <path_to_file> with the path to the local txt file to be posted.

To run tests:  `pytest tests.py`  OR `curl -X POST "http://0.0.0.0:8000/run-tests/"`
