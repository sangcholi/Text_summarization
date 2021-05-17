class ModelHandler:
    def __init__(self):
        pass

    def initialize(self, ):
        from transformers import BartTokenizer
        from transformers import BartForConditionalGeneration
        from transformers import BartConfig
        self.model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
        self.tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

    def preprocess(self, text):
        model_input = tokenizer([text], max_length = len(text),
                                return_tensors = 'pt')

        return model_input

    def inference(self, model_input):
        model_output = model.generate(inputs['input_ids'], num_beams = 3,
                                    max_length = 100, early_stopping = True)

        return model_output

    def postprocess(self, model_output):
        predicted_results = []
        for o in model_output:
            predicted_result.append(stokenizer.decode(o, skip_special_tokens = True,
                                                    clean_up_tokenization_spaces = False))
        
        return predicted_results

    def handle(self, data):
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        
        return self.postprocess(model_output)