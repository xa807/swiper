import uuid

import oss2


def get_bucket():

    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。
    # 强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIRiQGIywYBeYN', 'ZOHiNBYPr72dCFog2fLU5Pu9RvVAIf')

    # Endpoint以北京为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'xa1807-swiper')

    return bucket


def upload_file(filename):

    key = uuid.uuid4().hex

    try:
        bucket = get_bucket()
        # <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
        result = bucket.put_object_from_file(key, filename)
        print(result)

    except Exception as e:
        print('上传文件失败',  e)

    return key


def download_file(key, filename):
    # 下载key的文件到本地filename文件中
    try:
        bucket = get_bucket()
        # <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
        bucket.get_object_to_file(key, filename)
    except Exception as e:
        print('上传文件失败',  e)


def delete_file(key):
    try:
        bucket = get_bucket()
        bucket.delete_object(key)
    except Exception as e:
        return False

    return True


def get_url(key):
    style = 'image/auto-orient,1/resize,p_50/quality,q_90/watermark,text_U3dpcGVyLVhB,' \
            'type_d3F5LW1pY3JvaGVp,color_b5a6a6,size_30,x_10,y_10'

    url = get_bucket().sign_url('GET', key, 10 * 60, params={'x-oss-process': style})
    return url


def get_small_url(key):
    style = 'image/auto-orient,1/resize,p_20/quality,q_90/watermark,' \
            'text_U3dpcGVyLVhB,color_ada8a8,size_40,g_se,x_10,y_10'

    url = get_bucket().sign_url('GET', key, 10 * 60, params={'x-oss-process': style})
    return url
