import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "Sally sells sea shells down by the seashore."
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, sentence):
    words_typed = len(sentence.split())
    time_taken = end_time - start_time
    words_per_minute = (words_typed / time_taken) * 60
    return words_per_minute

def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start the test.")
    sentence = generate_random_sentence()
    print("\nType the following sentence as fast as you can:\n")
    print(sentence)
    input("\nPress Enter when you are ready to start typing.")

    start_time = time.time()
    user_input = input("\nStart typing here: ")
    end_time = time.time()

    accuracy = calculate_accuracy(sentence, user_input)
    words_per_minute = calculate_typing_speed(start_time, end_time, sentence)

    print("\nTest Results:")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typing Speed: {words_per_minute:.2f} words per minute")

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct_words = [1 for word1, word2 in zip(original_words, typed_words) if word1 == word2]
    accuracy = (len(correct_words) / len(original_words)) * 100
    return accuracy

if __name__ == "__main__":
    typing_test()
