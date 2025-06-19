# Hugging Face CLI Chatbot

A simple command-line chatbot in Python using a small Hugging Face text generation model (google/flan-t5-large).

## Features
- Loads a Hugging Face-supported text generation model and tokenizer
- Uses the Hugging Face `pipeline` for text generation
- Maintains a sliding window of the last 5 message exchanges for chat memory
- Command-line interface with continuous chat loop
- Type `/exit` to quit
- Type `/history` to  check history

## Installation

1. **Clone the repository** (if needed):
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install transformers torch
   ```

## Usage

Run the chatbot from the terminal:

```bash
python interface.py
```

## Sample Interaction

```
Welcome to the Hugging Face CLI Chatbot! Type /exit to quit.
You: Hello!
Bot: Hello! How can I help you today?
You: Tell me a joke.
Bot: Why did the chicken cross the road? To get to the other side!
You: /exit
Goodbye!
```

## Customization
- To use a different Hugging Face model, edit the `model_name` in `model_loader.py`.

## Files
- `model_loader.py`: Loads the model and tokenizer
- `chat_memory.py`: Manages chat memory buffer
- `interface.py`: Command-line interface and integration 