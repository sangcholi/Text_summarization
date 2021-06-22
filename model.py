import sys
from transformers import BartTokenizer
from transformers import BartForConditionalGeneration
from transformers import BartConfig
import torch
device='cuda' if torch.cuda.is_available() else 'cpu' 

class ModelHandler:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
        self.tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

    def preprocess(self, text):
        model_input = self.tokenizer([text], max_length = len(text),
                                return_tensors = 'pt')

        return model_input

    def process(self, model_input):
        input_ids = model_input['input_ids'].to(device)
        model_output = self.model.generate(input_ids, num_beams = 3,
                                    max_length = 100, early_stopping = True)

        return model_output

    def postprocess(self, model_output):
        predicted_results = []
        for o in model_output:
            predicted_results.append(self.tokenizer.decode(o, skip_special_tokens = True,
                                                    clean_up_tokenization_spaces = False))

        return predicted_results

    def inference(self, data):
        model_input = self.preprocess(data)
        model_output = self.process(model_input)
        
        return self.postprocess(model_output)