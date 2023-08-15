#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return a tuple containing the length of the sentence and its first character.

    Args:
        sentence (str): The input sentence.

    Returns:
        A tuple containing the length of the sentence and its first character.
    """
    if not sentence:
        return
    result_tuple = (len(sentence), sentence[0])
    return result_tuple
