import tensorflow_hub as hub
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def get_embed(sentence):
  return embed([sentence]).numpy()[0].tolist()

def get_embeds(list_of_sentences):
  return [get_embed(sentence) for sentence in list_of_sentences]

if __name__ == "__main__":
  print(get_embed("hiiifjia sjdfiaosd fasdf asd"))
