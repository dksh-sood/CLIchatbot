from transformers.pipelines import pipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def load_model_and_tokenizer(model_name="google/flan-t5-large"):
    """
    Loads a Hugging Face instruction-tuned model and tokenizer for Q&A and general knowledge.
    Default: google/flan-t5-large (better for factual answers).
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Add pad token if missing
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        model.resize_token_embeddings(len(tokenizer))
    pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id

    generator = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        pad_token_id=pad_token_id
    )
    return generator, tokenizer
