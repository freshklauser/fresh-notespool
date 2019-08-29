### 1. 编解码json数据

 - `json.loads() `解码`json`数据，将字符串类型json数据转化为字典dict类型

- `json.dumps()` 编码`json`数据，将dict类型转化为 str 类型的 json 数据

  ```
  # json <---> dictionary
  # note: dictionary中的value不能使用numpy的数据格式如ndarray/np.integer/np.floating, 会报错可以是list，tuple,int，float这些内置的数据类型
  	dict --> json:
  		json_cont = json.dumps(dict_cont)
  	json --> dict:
  		dict_cont = json.loads(json_cont)
  	eg:
  	def write_to_txt(self):
          receiver_dict = {}
          receiver_dict['freq'] = self.frequency
          receiver_dict['ampt'] = self.amplitude
          # convert to json for writing into txt file
          receiver_json = json.dumps(receiver_dict)     # type:str
          # write json to local txt file
          open(self.txt_name, 'w') as f:
          	f.write(receiver_json)
          ''' json --> dict '''
          self.recerver_dict = json.loads(self.receiver_json)
  ```

### 2. 解决numpy数据格式造成的typeError错误
​	自定义序列化方法 继承`json.JSONEncoder`，再使用`json`方法时加入参数
​	代码如下：

```
class NpEncoder(json.JSONEncoder):
		def default(self, obj):
			if isinstance(obj, np.integer):
				return int(obj)
			elif isinstance(obj, np.floating):
				return float(obj)
			elif isinstance(obj, np.ndarray):
				return obj.tolist()
			else:
				return super(NpEncoder, self).default(obj)
				
data_json = json.dumps(data_dict, cls=NpEncoder)			# cls=NpEncoder
```

### 3. json.dumps序列化数据并输入中文编码数据

​	`json.dumps(change, ensure_ascii=False) `

### 4. requests中post/get方法的属性

```
r.status_code #响应状态码
	r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
	r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
	r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
	r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
	#*特殊方法*#
	r.json() #Requests中内置的JSON解码器
	r.raise_for_status() #失败请求(非200响应)抛出异常
```

### 5. post提交数据参数 data/json

- `payload`为字典时，使用json可以自动解析为`json`格式
- `payload`为`json`时，使用`data`参数

```
payload = {'adminID': "12",'beginYear': "2019"}
# 使用json参数自动解析payload为json格式数据上传
response = requests.post(url = url,json = payload,headers = headers)
print(response.text)

# 使用data参数上次json.dumps解析过的数据
response = requests.post(url = url,data = json.dumps(payload),headers = headers)
print(response.text)
```

- `res.text`和`res.content`的区别

  `resp.text`返回的是`Unicode`型的数据， 类型是 `<str>`

  `resp.content`返回的是`bytes`型也就是二进制的数据,，类型是`<bytes>`

  `resp.json()`返回的是`json`格式数据

  - 如果你想取文本，可以通过`r.text`

  - 如果想取图片，文件，则可以通过`r.content`

    

### 2. 读写json文件：

- json.load() 读取json文件的 json数据
- json.dump() 把json数据写出为 json文件