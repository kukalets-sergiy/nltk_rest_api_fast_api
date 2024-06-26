import nltk


def tokenize_text(text: str):
    return nltk.word_tokenize(text)


def pos_tag_text(text: str):
    tokens = tokenize_text(text)
    return nltk.pos_tag(tokens)


def ner_text(text: str):
    pos_tags = pos_tag_text(text)
    ne_tree = nltk.ne_chunk(pos_tags)
    entities = []
    for subtree in ne_tree:
        if isinstance(subtree, nltk.Tree):
            entity = " ".join([word for word, tag in subtree.leaves()])
            entity_type = subtree.label()
            entities.append({"entity": entity, "type": entity_type})
    return entities
