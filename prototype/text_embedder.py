from transformers import BertTokenizer, BertModel

class TextEmbedder():
    def __init__(self, model='bert'):
        if model == 'bert':
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            self.model = BertModel.from_pretrained("bert-base-uncased")

    def to_embedding(self, text, max_length=512):
        text = text[:max_length]
        # text = '[CLS] ' + text # TODO: Do I need this step?
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        output = output.pooler_output.detach().numpy()
        return output[0]