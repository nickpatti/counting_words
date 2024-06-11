from typing import Optional
import re
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Query, HTTPException
import subprocess

from process_file import format_word_counts

app = FastAPI()


@app.post("/word_count/")
async def process_document(file: UploadFile = File(...), num_of_entries: Optional[int] = Query(None)):
    """
    An async function that takes a file and number of entries and returns a string with new lines in order from the most
    frequent to the least frequent word. 
    :param file: Local file path
    :param num_of_entries: The amount of words and counts you want to output
    :return: num_of_entries amount of words and counts in a string with a newline after each
    """
    try:
        # attempt to upload the file
        file_path = Path(f"/tmp/{file.filename}")
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return format_word_counts(file_path, num_of_entries)


@app.post("/run-tests/")
async def run_tests():
    try:
        # Attempt to run tests
        result = subprocess.run(["pytest", "-v", "-s", "tests.py"], capture_output=True, text=True)
        output = result.stdout

        if "FAILED" in output:
            # Detect if one of the tests failed then count the amount of full stops using regex.
            failed_tests = re.findall(r"=+ (.+?) =+", output)
            raise HTTPException(status_code=500, detail=f"Tests failed: {failed_tests}")
        else:
            return {"message": "All tests passed"}

    except subprocess.CalledProcessError as e:
        # Raise error if the tests fail to run
        raise HTTPException(status_code=500, detail=f"Failed to execute tests: {e}")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

