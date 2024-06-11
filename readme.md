### Running on PythonAnywhere ###


### Running Locally ###
To count words:
- Run python main.py to run the server locally
- Run the below command to post a local file to the endpoint:

`curl -s -X POST "http://0.0.0.0:8000/word_count/?num_of_entries=<number_of_entries>" -F "file=@<path_to_file>" | sed 's/\\n/\n/g'`

Replace <number_of_entries> to the amount of words and their counts you would like to see.
Replace <path_to_file> with the path to the local txt file to be posted.

To run tests:
pytest tests.py