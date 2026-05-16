from transformers import pipeline

def get_qa_chain():

    pipe = pipeline(
        "text-generation",
        model="distilgpt2"
    )

    return pipe