
from SDK.offline_agent import OfflineJobSearchAgent


def main():
    print("=" * 45)
    print("Welcome to the Offline Job Search Agent!")
    print("Type 'exit' to quit.")
    print("=" * 45)

    agent = OfflineJobSearchAgent()

    while True:
        user_message = input("\nYou: ").strip()

        if user_message.lower() in ["exit", "quit", "יציאה"]:
            print("Goodbye!")
            break

        if not user_message:
            continue

        try:
            answer = agent.chat(user_message)
            print(f"\nAgent: {answer}")
        except Exception as error:
            print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()
