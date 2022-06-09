import argparse
import random
import requests
import os


def authentication():
    headers = {
        "Content-Type": "application/json",
    }
    data = f'{{"email":"{args.username}","password":"{args.password}"}}'
    response = requests.post(
        "https://project-apollo-api.stg.gc.casetext.com/v0/auth/login",
        headers=headers,
        data=data,
    )
    return response.json()["token"]


def collection():
    headers = {
        "Authorization": f"Bearer {authentication()}",
        "Content-Type": "application/json",
    }
    data = '{ "model": "lawbert" }'
    response = requests.post(
        f"https://project-apollo-api.stg.gc.casetext.com/v0/{args.collection}/create",
        headers=headers,
        data=data,
    )
    return response.ok


def random_generator():
    dirpath = os.getcwd() + "/" + args.filedir
    filenames = random.sample(os.listdir(dirpath), args.num_files)
    headers = {
        "Authorization": f"Bearer {authentication()}",
        "Content-Type": "text/plain",
    }
    upload = 0
    for fname in filenames:
        print(fname)
        files = {
            "file": (f"{fname}", open(f"{dirpath}/{fname}", "r")),
        }
        response = requests.post(
            f"https://project-apollo-api.stg.gc.casetext.com/v0/{args.collection}",
            headers=headers,
            files=files,
        )
        if response.ok:
            print(response.text)
            upload += 1
            print(upload)
        else:
            print("Upload failed")
    return response.ok


def argument():
    parser = argparse.ArgumentParser(
        description="CaseText WeSearch Upload Tool"
    )
    parser.add_argument(
        "-u",
        "--username",
        help="Account username/email",
        required=True,
    )
    parser.add_argument(
        "-p",
        "--password",
        help="Account password",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--collection",
        help="Collection name",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--filedir",
        help="Folder to be extracted",
        nargs="?",
        default="446c8aa0-6eba-11e5-bc7f-4851b79b387c",
    )
    parser.add_argument(
        "-n",
        "--num_files",
        help="Number of random files",
        nargs="?",
        default=1000,
        type=int,
    )
    return parser.parse_args()


def main() -> None:
    collection()
    random_generator()


if __name__ == "__main__":
    args = argument()
    main()
