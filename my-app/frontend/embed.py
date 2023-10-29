import tensorflow_hub as hub
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def get_embed(sentence):
  return embed([sentence])

if __name__ == "__main__":
  print(get_embed("hiiifjia sjdfiaosd fasdf asd"))
