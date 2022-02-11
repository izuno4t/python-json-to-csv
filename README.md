# python-json-to-csv

JSON ファイルを CSV に変換する

## requirement

### pip install

```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.pypip
```

### install modules

```sh
pip install -r requirements.txt
```

## jq でもできるんだよ

```sh
cat sample1.json | jq -r '.[] | [.key1, .key2, .key3] | @csv'
```

ファイルサイズが大きい場合は`--stream`で

```sh
jq -cn --stream 'fromstream(1|truncate_stream(inputs)) | [.key1, .key2, .key3] | @csv' test.json
curl sample1.json | jq -n --stream 'fromstream(1|truncate_stream(inputs)) | .[] | [.key1, .key2, .key3] | @csv'
```

## refs

- [JSON を CSV に簡単に変換する方法](https://qiita.com/yukiyoshimura/items/4c8d535ac79843d0fb0e)
