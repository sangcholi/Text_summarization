import sys
from transformers import BartTokenizer
from transformers import BartForConditionalGeneration
from transformers import BartConfig
        

class ModelHandler:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
        self.tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

    def preprocess(self, text):
        model_input = self.tokenizer([text], max_length = len(text),
                                return_tensors = 'pt')

        return model_input

    def inference(self, model_input):
        model_output = self.model.generate(model_input['input_ids'], num_beams = 3,
                                    max_length = 100, early_stopping = True)

        return model_output

    def postprocess(self, model_output):
        predicted_results = []
        for o in model_output:
            predicted_results.append(self.tokenizer.decode(o, skip_special_tokens = True,
                                                    clean_up_tokenization_spaces = False))

        return predicted_results

    def handle(self, data):
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        
        return self.postprocess(model_output)

if __name__ == "__main__":
    # text = sys.argv[0]
    text = "Welcome to Flask’s documentation. Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API section."
    model = ModelHandler()
    output = model.handle(text)
    print(output)
