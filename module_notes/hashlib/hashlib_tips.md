[TOC]

[`Refer:Python之数据加密与解密及相关操作（hashlib、hmac、random、base64、pycrypto）`](<https://www.cnblogs.com/yyds/p/7072492.html>)

```
# Example to get the SHA1 sum, given a user's email
import hashlib
mbox = 'foo@bar.net'
mbox_sha1sum = hashlib.sha1(mbox.encode('utf-8'))
print(mbox_sha1sum.hexdigest())
print(mbox_sha1sum.digest())
>>> 62e8a8e6a893103a75c2132fa880e7f07e8fa517
>>> b'b\xe8\xa8\xe6\xa8\x93\x10:u\xc2\x13/\xa8\x80\xe7\xf0~\x8f\xa5\x17'
```

