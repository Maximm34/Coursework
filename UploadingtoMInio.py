
from minio import Minio
from minio.error import ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists
#Uploading answers to minio
def UploadingAnswersPractice():
    MINIO_PORT = 9000
    HOST_URI = "http://127.0.0.1:9000"
    Bucketname = "uploadeddocks"
    login = "minio"
    password = "minio12345"
    doc_to_upload = "OutputP.doc"

    minioClient = Minio('%s:%s' % (HOST_URI, MINIO_PORT),
                        access_key=login,
                        secret_key=password,
                        secure=False)

    try:
        minioClient.make_bucket(Bucketname)
    except BucketAlreadyOwnedByYou as er:
        pass
    except BucketAlreadyExists as er:
        pass
    except ResponseError as er:
        raise

    try:
        objct = minioClient.fput_object(
            bucket_name=Bucketname, object_name=doc_to_upload, file_path="./%s" % doc_to_upload
        )
        print("done")
        print(objct)
    except ResponseError as er:
        print(er)
#Uploading answers to minio
def UploadingAnswersTest():
    MINIO_PORT = 9000
    HOST_URI = "http://127.0.0.1:9000"
    Bucketname = "uploadeddocks"
    login = "minio"
    password = "minio12345"
    doc_to_upload = "OutputT.doc"

    minioClient = Minio('%s:%s' % (HOST_URI, MINIO_PORT),
                        access_key=login,
                        secret_key=password,
                        secure=False)

    try:
        minioClient.make_bucket(Bucketname)
    except BucketAlreadyOwnedByYou as er:
        pass
    except BucketAlreadyExists as er:
        pass
    except ResponseError as er:
        raise

    try:
        objct = minioClient.fput_object(
            bucket_name=Bucketname, object_name=doc_to_upload, file_path="./%s" % doc_to_upload
        )
        print("done")
        print(objct)
    except ResponseError as err:
        print(err)


#Uploading answers to minio
def UploadingAccountDetail():
    MINIO_PORT = 9000
    HOST_URI = "http://127.0.0.1:9000"
    Bucketname = "uploadeddocks"
    login = "minio"
    password = "minio12345"
    doc_to_upload = "OutputT.doc"

    minioClient = Minio('%s:%s' % (HOST_URI, MINIO_PORT),
                        access_key=login,
                        secret_key=password,
                        secure=False)

    try:
        minioClient.make_bucket(Bucketname)
    except BucketAlreadyOwnedByYou as er:
        pass
    except BucketAlreadyExists as er:
        pass
    except ResponseError as er:
        raise

    try:
        objct = minioClient.fput_object(
            bucket_name=Bucketname, object_name=doc_to_upload, file_path="./%s" % doc_to_upload
        )
        print("done")
        print(objct)
    except ResponseError as err:
        print(err)