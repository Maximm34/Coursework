from minio import Minio
# this piece of code is responsible fo downloading files from the cloud storage
def downloadingmaths1():
     client = Minio(
         "http://127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
      )


     for item in client.list_objects("maths1",recursive=True):
         client.fget_object("maths1",item.object_name,item.object_name)


def downloadingmaths2():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths2", recursive=True):
        client.fget_object("maths2", item.object_name, item.object_name)


def downloadingmaths3():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths3", recursive=True):
        client.fget_object("maths3", item.object_name, item.object_name)


def downloadingmaths4():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths4", recursive=True):
        client.fget_object("maths4", item.object_name, item.object_name)


def downloadingmaths5():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths5", recursive=True):
        client.fget_object("maths5", item.object_name, item.object_name)


def downloadingmaths6():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths6", recursive=True):
        client.fget_object("maths6", item.object_name, item.object_name)


def downloadingmaths7():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths7", recursive=True):
        client.fget_object("maths7", item.object_name, item.object_name)


def downloadingmaths8():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths8", recursive=True):
        client.fget_object("maths8", item.object_name, item.object_name)


def downloadingmaths9():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("maths9", recursive=True):
        client.fget_object("maths9", item.object_name, item.object_name)

def downloadingtests():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("tests", recursive=True):
        client.fget_object("test", item.object_name, item.object_name)


def downloadingpractice():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("practices", recursive=True):
        client.fget_object("practices", item.object_name, item.object_name)

def downloadinganswersfortests():
    client = Minio(
        "http://127.0.0.1:9000",
        access_key="minio",
        secret_key="minio12345",
    )

    for item in client.list_objects("answersfortests", recursive=True):
        client.fget_object("answersfortests", item.object_name, item.object_name)