from model_loader import load_model_and_tokenizer
from chat_memory import ChatMemory


def main() -> None:
    print("Welcome to the Hugging Face CLI Chatbot!")
    print("Use /history to view recent messages or /exit to quit.\n")

    # ---- Load model + tokenizer ---------------------------------------------
    generator, tokenizer = load_model_and_tokenizer()

    # ---- Sliding‑window memory (last 5 messages) ----------------------------
    memory = ChatMemory(max_length=5)

    system_prompt = (
        "You are a helpful, concise assistant. "
        "Answer as clearly and relevantly as possible."
    )

    try:
        while True:
            user_input = input("You: ").strip()

            # -------- Special commands ----------------------------------------
            lower = user_input.lower()
            if lower == "/exit":
                print("Goodbye!")
                break

            if lower == "/history":
                # Print persistent chat history from file
                try:
                    with open("chat_history.txt", "r", encoding="utf-8") as f:
                        file_history = f.read()
                    if not file_history.strip():
                        print("(history is empty)\n")
                    else:
                        print("\n--- Full Chat History ---")
                        print(file_history)
                        print("------------------------\n")
                except FileNotFoundError:
                    print("(history is empty)\n")
                continue
            # ------------------------------------------------------------------

            # -------- Build prompt & store user message -----------------------
            memory.add_message("user", user_input)
            # Append user message to persistent history
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write(f"You: {user_input}\n")
            chat_history = memory.get_context()
            prompt = f"{system_prompt}\n{chat_history}\nbot:"

            # -------- Generate reply ------------------------------------------
            output = generator(
                prompt,
                max_new_tokens=64,
                pad_token_id=tokenizer.eos_token_id
            )

            # pipeline returns list[dict]; grab first element's text
            generated = (
                output[0]["generated_text"]
                if isinstance(output, list) and output
                else ""
            )

            if not generated:
                print("[Error] Model did not return expected output.")
                continue

            response = generated.strip()
            print(f"Bot: {response}\n")
            memory.add_message("bot", response)
            # Append bot message to persistent history
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write(f"Bot: {response}\n")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
