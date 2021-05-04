from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import time


def summarization(TEXT):
    now_time = time.time()
    model = BartForConditionalGeneration.from_pretrained(
        'sshleifer/distilbart-cnn-12-6')
    tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')
    inputs = tokenizer([TEXT],
                       max_length=len(TEXT), return_tensors='pt')

    summary_ids = model.generate(
        inputs['input_ids'], num_beams=3, max_length=100, early_stopping=True)
    print(f'Process_time : {time.time() - now_time}')
    print(f'**Original Text** \n {TEXT}')
    print('-' * 100)
    print(f'**Summarization Text**')
    for g in summary_ids:
        print(tokenizer.decode(g, skip_special_tokens=True,
                               clean_up_tokenization_spaces=False))
    return


if __name__ == "__main__":
    print('****testing*****')
    text = '''Son can basically play in any attacking position,[4][150] (winger, second striker, striker) and can even be deployed as an attacking midfielder or wing-back if necessary. He himself has confirmed this, saying, \"I don't care where I play. The main thing is I'm in the game. I can play as a second striker or behind. Whatever the coach says, I'll do. I don't have a favorite position. I'll be anywhere and always on the throttle.\"
    Son is known for his two-footed ability, explosive pace, positional sense, movement, close control and clinical finishing which make him especially effective on the counter-attack.[153] Moreover, he has drawn praise from teammates and in the media for his selfless work-rate and defensive contribution, and is capable of providing assists for teammates, in addition to scoring goals himself.[152][154]'''
    summarization(text)
