# WeSearch
An easy to use tool to upload files for WeSearch

## Requirements
- Locally clone this repo and run with python3. This has been tested with v3.10.4
- You have an account with casetext. If not, create an account from [here](https://casetext.com/trial)
- Install needed packages `python3 -m pip install -r requirements.txt`

## Usage
```
export password=XXXXX
python3 main.py -u youremail@address.com -p $password -c collection_name
```
Default Setup:
- The file directory is the [current project path]/446c8aa0-6eba-11e5-bc7f-4851b79b387c/[files]. If you would like to specify a different folder, pass in `-f or --filedir new-dir-name`. This assumes your new project path would be in the format of [current project path]/[new directory name]/[files]
- The number of files is set to 1000 by default. If you would like to upload a different number of files, you can bypass the default by passing in `-n or --num_files integer`.

Example: We want to upload 5 files from a directory called `upload` and create a collection called `resources`
`python3 main.py -u youremail@address.com -p $password -c resources -f upload -n 5`
