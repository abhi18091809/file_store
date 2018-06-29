from flask import Response
from main.services.authorisationService import *
from main.services.uploadService import *


def upload_file(auth, file, option):
    user = authorise(auth)

    if user is not None:
        if file.lower().endswith(('.doc', '.pdf', '.txt')):
            implement = upload_file_for_storage(file, option)
            if implement:
                res = Response(response="File stored", status=201)
            else:
                res = Response(response="Error in uploading file", status=500)
        else:
            res = Response(response="File not allowed", status=403)
    else:
        res = Response(response="Unauthorised Usage", status=401)

    return res

def rename_file(auth, new_name, old_name):
    return True

def delete_file(auth, file):
    return True
