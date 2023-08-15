#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Generate a tuple with length of sentence and its first character.
    
    Args:
        sentence (str): The input sentence.
        
    Returns:
        A tuple containing length of sentence and its first character.
    """
    my_tuple = ()
    
    if len(sentence) == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = len(sentence), sentence[0]
    
    return my_tuple
