# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-12-04 09:07:25
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-12-04 09:07:48

def encode_to_UTF8(data):
    try:
        return data.encode('UTF-8')
    except UnicodeEncodeError as e:
        logger.error("Could not encode data to UTF-8 -- %s" % e)
        return False
    except Exception as e:
        raise(e)
        return False


def try_decode_UTF8(data):
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return False
    except Exception as e:
        raise(e)