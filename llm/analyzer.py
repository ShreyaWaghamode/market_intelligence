from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)