from .rag import rag


if __name__ == "__main__":

    question = "What did Mohammad study at university?"

    result = rag(question)

    print("Answer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print("-", source)