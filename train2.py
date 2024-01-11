from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Load your Q&A log from a TXT file
file_path = r"C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\qna_logbook.txt"
with open(file_path, "r", encoding="utf-8") as file:
    qna_data = file.read()

# Tokenize the dataset
tokenized_data = tokenizer(qna_data, return_tensors="pt", truncation=True)

# Create a TextDataset and DataCollator
dataset = TextDataset(
    file_path=file_path,
    tokenizer=tokenizer,
    block_size=128  # Adjust the block_size as needed
)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Set up Trainer and TrainingArguments
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Fine-tune the GPT-2 model on your Q&A data
trainer.train()
