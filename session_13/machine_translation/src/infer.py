from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import config


model = AutoModelForSeq2SeqLM.from_pretrained(config.PRETRANIDED_MODEL)
tokenizer = AutoTokenizer.from_pretrained(config.TOKENIZER_NAME)
pipe = pipeline("translation_en_to_de", model=model, tokenizer=tokenizer)


text = "Hello, how are you?"

print(pipe(text)[0]["translation_text"])
