def encode(tokens, vocabulary):
    """Replace each word by its number.

    Input:   tokens, a list of strings, and vocabulary, a dictionary of the
             kind build_vocabulary returns. Every word in tokens is a key of
             vocabulary.
    Output:  a list of integers, the same length as tokens, in the same
             order: the number of each word.

        encode(["the", "cat", "the"], {"the": 0, "cat": 1}) -> [0, 1, 0]
        encode([], {"the": 0}) -> []
    """
    ids = [vocabulary[word] for word in tokens] # Replace each word with its corresponding number
    return ids # Return the list of numbers


# Test my function
print(encode(["the", "cat", "the"], {"the": 0, "cat": 1})) # Should print [0, 1, 0]
print(encode([], {"the": 0})) # Should print []