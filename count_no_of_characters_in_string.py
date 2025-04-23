def count_no_of_characters_in_string(string):
    """

    :param string: str: sequence of characters.
    :return: int: count the no.of characters.
    """
    count=0
    s=string.replace(" ","")
    for i in s:
        count+=1
    return count

string="The sun is shining today"

print(count_no_of_characters_in_string(string))
