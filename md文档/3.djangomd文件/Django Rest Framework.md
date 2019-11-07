# Day10 Django Rest Framework

## RESTful���

### һ. WebӦ��ģʽ

##### �ڿ���WebӦ���У�������Ӧ��ģʽ��

```
ǰ��˲����룺��Ⱦ
ǰ��˷���
```

#### 1 ǰ��˲�����

```
��ǰ��˲������Ӧ��ģʽ�У�ǰ��ҳ�濴����Ч�������ɺ�˿��ƣ��ɺ����Ⱦҳ����ض���Ҳ���Ǻ����Ҫ����ǰ�˵�չʾ��ǰ�����˵���϶Ⱥܸߡ�

����Ӧ��ģʽ�Ƚ��ʺϴ���ҳӦ�ã����ǵ���˶Խ�Appʱ��App���ܲ�����Ҫ��˷���һ��HTML��ҳ�������������ݱ������Ժ��ԭ��������ҳ�Ľӿڲ���������ǰ��AppӦ�ã�Ϊ�˶Խ�App��˻����ٿ���һ�׽ӿڡ�

```

#### 2 ǰ��˷���

```
��ǰ��˷����Ӧ��ģʽ�У���˽�����ǰ����������ݣ�������ȾHTMLҳ�棬���ٿ���ǰ�˵�Ч��������ǰ���û�����ʲôЧ�����Ӻ�������������μ��ص�ǰ���У�����ǰ���Լ���������ҳ����ҳ�Ĵ���ʽ��App��App�Ĵ���ʽ������������ǰ�ˣ���������ݻ�����ͬ����˽��迪��һ���߼������ṩ���ݼ��ɡ�

��ǰ��˷����Ӧ��ģʽ�� ��ǰ�����˵���϶���Խϵ͡�

��ǰ��˷����Ӧ��ģʽ�У�����ͨ������˿�����ÿ����ͼ����Ϊһ���ӿڣ�����API��ǰ��ͨ�����ʽӿ��������ݽ�����ɾ�Ĳ顣
```

### ��. ��ʶRESTful

```
��Representational State Transfer����д��ά���ٿƳ���Ϊ������״̬���䡱�����ڴ󲿷������Ϊ�����ֲ�״̬ת������

RESTful��һ�ֿ������ά���ٿ�˵��REST����Ʒ������Ǳ�׼�� REST����������������client��server��һ�ֽ�����ʽ��REST����ʵ�ã�ʵ�õ��������� RESTful API��REST��������ӿڣ�,һ����ά������ܹ����

�����������忴��RESTful����url,������Ҫ��ѯ��Ʒ��Ϣ����ô
��REST��url��http://.../queryGoods?id=1001&type=t01
REST��url: http://.../t01/goods/1001

���Կ���REST�ص㣺url��࣬������ͨ��url����������������ͳ��url�Ƚφ��£�������ʵ���������ַ����ƴ��һ���ַ���������Ƕ������ɡ����ǲ���REST�ķ��ͻ�úܶ࣬���ںܶ����վ�Ѿ��������ַ���ˣ���Ҳ�ǳ������򣬵��͵ľ���url�Ķ̻�ת����
```

#### ����ʲô��RESTful�ܹ���

```
ÿһ��URL����һ����Դ��
�ͻ��˺ͷ�����֮�䣬����������Դ��ĳ�ֱ��ֲ㣻
�ͻ���ͨ���ĸ�HTTP���ʣ�GET,POST,PUT,DELETE�����Է���������Դ���в�����ʵ��"���ֲ�״̬ת��"��
```

### ��. RESTful API���

###### Э��

�ӿ�API���û���ͨ��Э�飬ͨ��ʹ��HTTP\(S\)Э�顣  TCP ,  UDP 

###### ����  Ӧ�þ�����API������ר������֮�¡�

```
http://api.hello.com 
```

���ȷ��API�ܼ򵥣������д��ģ���䣬���Կ��Ƿ���������֮�¡�

```
http://www.hello.com/api/
```

###### �汾

Ӧ�ý�API�İ汾�ŷ���URL��

```
http://api.rock.com/v1/
```

Ҳ�������ǽ��汾�ŷ���HTTP��ͷ��Ϣ�У����������URL�з����ֱ�ۡ�GITHUB����ô��ġ�

###### ·����Endpoint��

·���ֳơ��յ㡰��endpoint������ʾAPI�ľ�����ַ��

��RESTful�ܹ��У�ÿ����ַ����һ����Դ��Resource����������ַ�в����ж��ʣ�ֻ�������ʣ��������õ��������������ݿ�ı������Ӧ��һ����˵�����ݿ��еı���ͬ�ּ�¼�ġ����ϡ���collection��������API�е�����ҲӦ��ʹ�ø�����

###### HTTP����

������Դ�ľ���������ͣ���HTTP���ʱ�ʾ��

HTTP���ö���

- GET��SELECT�����ӷ�����ȡ����Դ
- POST��CREATE or UPDATE�����ڷ�����������Դ�������Դ
- PUT��UPDATE�����ڷ�����������Դ���ͻ����ṩ�ı���������Դ��
- PATCH��UPDATE�����ڷ�����������Դ���ͻ����ṩ�ı�����ԣ�
- DELETE��DELETE�����ӷ�����ɾ����Դ
- HEAD����ȡ��Դ��Ԫ����
- OPTIONS����ȡ��Ϣ��������Դ����Щ�����ǿͻ��˿��Ըı�ġ�

ʾ��

- GET  /students����ȡ����ѧ��
- POST /students���½�ѧ��
- GET  /students/id����ȡĳһ��ѧ��
- PUT /students/id ������ĳ��ѧ������Ϣ����Ҫ�ṩѧ����ȫ����Ϣ��
- PATCH /students/id������ĳ��ѧ������Ϣ����Ҫ�ṩѧ�����������Ϣ��
- DELETE /students/id��ɾ��ĳ��ѧ��

###### ������Ϣ��Filtering��

�����¼�������࣬�����������ܽ����Ƿ��ظ��û���APIӦ���ṩ���������˷��ؽ����

- ?limit=10
- ?offset=10
- ?page=2&per\_page=20
- ?sortby=name&order=desc
- ?student\_id=id

�������������������࣬������API·����URL����ż�����ظ������� GET /students/id �� ��student\_id=id

###### ״̬��

���������û����ص�״̬�����ʾ��Ϣ��������������һЩ�ط�

- 200 OK - \[GET\]���������ɹ������û����������
- 201 CREATED -\[POST/PUT/PATCH\]���û��½����޸����ݳɹ�
- 202 Accepted - \[\*\] ����ʾһ�������Ѿ������̨�Ŷӣ��첽����
- 204 NO CONTENT - \[DELETE\]����ʾ����ɾ���ɹ�
- 400 INVALID REQUEST - \[POST/PUT/PATCH\]���û������������д���
- 401 Unauthorized - \[\*\] ����ʾ�û�û��Ȩ�ޣ����ƣ��û������������
- 403 Forbidden - \[\*\]����ʾ�û��õ���Ȩ�����Ƿ����Ǳ���ֹ��
- 404 NOT FOUND - \[\*\]���û�������������Ե��ǲ����ڵļ�¼
- 406 Not Acceptable - \[\*\]���û������ʽ���ɵ�
- 410 Gone - \[GET\] ���û��������Դ�������Ƴ����Ҳ����ٵõ���
- 422 Unprocesable entity -\[POST/PUT/PATCH\]��������һ������ʱ������һ����֤����
- 500 INTERNAL SERVER EROR - \[\*\] ���������ڲ���������

###### ������

���״̬����4xx����Ӧ�����û����س�����Ϣ��һ����˵�����ص���Ϣ�н�error��Ϊ����

###### ���ؽ��

��Բ�ͬ���������������û����صĽ��Ӧ�÷������¹淶

- GET /sutdents��������Դ������б����飬���ϣ�
- GET /collection/id�����ص�����Դ����
- POST /collection�����������ɵ���Դ����
- PUT /collection/id��������������Դ����
- PATCH /collection/id��������������Դ����
- DELETE /collection/id������һ�����ĵ�

###### ʹ�����ӹ�����Դ

RESTful API����������ý�壬�����ؽ�����ṩ���ӣ���������API������ʹ���û������ĵ���Ҳ֪����һ��Ӧ����ʲô��

```
{
    "link": {
        "rel":   "collection https://www.hello.com/zoostudents",
        "href":  "https://api.hello.com/students",
        "title": "List of students",
        "type":  "application/vnd.yourformat+json"
      }
}
```

- rel����ʾ���API�뵱ǰ��ַ�Ĺ�ϵ
- href����ʾAPI��·��
- title����ʾAPI�ı���
- type����ʾ���ص�����

###### ����

- ���������ص����ݸ�ʽ��Ӧ�þ���ʹ��JSON
- API�������֤Ӧ��ʹ��OAuth2.0���



### APIView

- ����
  - generics����
  - GenericAPIView
    - ���ӵ�ģ�͵Ļ�ȡ����
    - get_queryset
    - get_object
      - lookup_field Ĭ��pk
    - get_serializer
    - get_serializer_class
    - get_serializer_context
    - filter_queryset
    - paginator
    - paginate_queryset
    - get_paginated_response
  - CreateAPIView
    - ����������ͼ
    - �̳���GenericAPIView
    - �̳���CreateModelMixin
    - ʵ����post���д���
  - ListAPIView
    - �б������ͼ
    - �̳���GenericAPIView
    - �̳���ListModelMixin
    - ʵ����get
  - RetrieveAPIView
    - ��ѯ�������ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���RetrieveModelMixin
    - ʵ����get  
  - DestroyAPIView
    - �������ݵ�����ͼ��ɾ�����ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���DestroyModelMixin
    - ʵ����delete
  - UpdateAPIView
    - �������ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���UpdateModelMixin
    - ʵ���� put,patch
  - ListCreateAPIView
    - ��ȡ�б����ݣ��������ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���ListModelMixin
    - �̳���CreateModelMixin
    - ʵ����  get,post
  - RetrieveUpdateAPIView
    - ��ȡ�������ݣ����µ������ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���RetrieveModelMixin
    - �̳���UpdateModelMixin
    - ʵ���� get, put, patch
  - RetrieveDestroyAPIView
    - ��ȡ�������ݣ�ɾ����������
    - �̳���GenericAPIView
    - �̳���RetrieveModelMixin
    - �̳���DestroyModelMixin
    - ʵ����  get, delete
  - RetrieveUpdateDestroyAPIView
    - ��ȡ�������ݣ����µ������ݣ�ɾ���������ݵ�����ͼ
    - �̳���GenericAPIView
    - �̳���RetrieveModelMixin
    - �̳���UpdateModelMixin
    - �̳���DestroyModelMixin
    - ʵ���� get, put, patch, delete
- mixins
  - CreateModelMixin
    - create
    - perform_create
    - get_success_headers
  - ListModelMixin
    - list
      - ��ѯ���������ӷ�ҳ���������л�
  - RetrieveModelMixin
    - retrieve
      - ��ȡ�������󲢽������л�
  - DestroyModelMixin
    - destroy
      - ��ȡ��������
      - ����ִ��ɾ��
      - ����Respon  ״̬��204
    - perform_destroy
      - Ĭ����ģ�͵�delete
      - ���˵���ݵ��߼�ɾ��
        - ��д���б���
  - UpdateModelMixin
    - update
      - ��ȡ���󣬺Ϸ���֤
      - ִ�и���
    - perform_update
    - partial_update
      - �������£���Ӧ�ľ���patch
- viewsets
  - ViewSetMixin
    - ��дas_view
  - GenericViewSet
    - �̳���GenericAPIView
    - �̳���ViewSetMixin
  - ViewSet
    - �̳���APIView
    - �̳���ViewSetMixin
    - Ĭ��ɶ����֧�֣���Ҫ�Լ��ֶ�ʵ��
  - ReadOnlyModelViewSet
    - ֻ����ģ�͵���ͼ����
    - �̳���RetrieveModelMixin
    - �̳���ListModelMixin
    - �̳���GenericViewSet
  - ModelViewSet
    - ֱ�ӷ�װ��������в���
    - �̳���GenericViewSet
    - �̳���CreateModelMixin
    - �̳���RetrieveModelMixin
    - �̳���UpdateModelMixin
    - �̳���DestroyModelMixin
    - �̳���ListModelMixin

