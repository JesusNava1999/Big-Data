import requests, json
import matplotlib.pyplot as plt

url = 'https://jsonplaceholder.typicode.com/comments'
resp = requests.get(url)
data = resp.text
print(type(data))
data_json = data.rstrip()
data_json = json.loads(data_json)
print(data_json[0])

plt.title("Comentarios por publicación")
comments=[]
post=[]
for elem in data_json:
    #print(elem["postId"])
    post.append(elem["postId"])
    comments.append(elem["id"])
plt.plot(post,comments)
plt.show()

