"""
This is a stub for COMP16321 Coursework 01.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here" and before the pass for that method.

Each method is documented to explain what work is to be placed within it.

NOTE: You can create as many more methods as you need. However, you need to add 
self as a parameter of the new method and  to call it with the prefix self.name 

"""

class Basics:#(s)
    # ---Section 1 --- #

    #(Question:a)
    def read_file(self):#(s)
        """
            Read in the text file and save the paragraph to a single string

            :return: A text file paragraph as a string
        """

        with open('./test.txt', encoding="utf-8") as f:

            read_data = f.read()

        return read_data
    
    # ---Section 2 --- #

    
    #(Question:a)
    def length_of_file(self):#(s)
        """
            Reports the length of the paragraph including numbers and whitespace
        
            :input_text: The text file paragraph as a string
            :return: An integer length of the file
        """
        input_text = self.read_file()#(s)

        return len(input_text)

    
    #(Question:b)
    def if_apple(self):#(s)
        """
            Reports a boolean True/False if the paragraph contains the entire word "apple"

            :input_text: The text file paragraph as a string
            :return: A boolean True/false
        """
        input_text = self.read_file()#(s)
        if "apple" in input_text.lower():

            return True

    #(Question:c)
    def if_upper_case_exists(self):#(s)
        """
            Reports a boolean True/False if the paragraph contains any number of upper case letters

            :input_text: The text file paragraph as a string
            :return: A boolean True/false
        """
        input_text = self.read_file()#(s)

        for char in list(input_text):

            if char.isupper() == True:

                return True
            
    #(Question:d)
    def if_numbers_exist(self):#(s)
        """
            Reports a boolean True/False if the paragraph contains any number of integers

            :input_text: The text file paragraph as a string
            :return: A boolean True/false
        """
        input_text = self.read_file()#(s)
        for char in list(input_text):

            if char.isnumeric() == True:

                return True

    #(Question:e)
    def if_spaces_exist(self):#(s)
        """
            Reports a boolean True/False if the paragraph contains any number of blank spaces

            :input_text: The text file paragraph as a string
            :return: A boolean True/false
        """
        input_text = self.read_file()#(s)
        for char in list(input_text):

            if char.isspace() == True:

                return True
            

    #(Question:f)
    def if_first_letter_t(self):#(s)
        """
            Reports a boolean True/False if the first letter of the paragraph is a t

            :input_text: The text file paragraph as a string
            :return: A boolean True/false
        """
        input_text = self.read_file()#(s)
        if input_text[0].lower() == "t":

                return True
    
    #(Question:g)
    def fourth_letter_seventh_word(self):#(s)
        """
            Reports the fourth letter in the seventh word of the paragraph as a string

            :input_text: The text file paragraph as a string
            :return: A string letter
        """
        input_text = self.read_file()#(s)

        return input_text.split()[6][3]

    # ---Section 3 --- #

    #(Question:a)
    def convert_to_lower_case(self):#(s)
        """
            Converts the paragraph to entirely lowercase with no other changes

            :input_text: The text file paragraph as a string
            :return: A string paragraph
        """
        input_text = self.read_file()#(s)

        return input_text.lower()
    

    #(Question:b)
    def reverse_paragraph(self):#(s)
        """
            Reverses the paragraph such that it can be read backwards with no other changes

            :input_text: The text file paragraph as a string
            :return: A string paragraph
        """
        input_text = self.read_file()#(s)

        text_as_list = list(input_text)

        text_as_list.reverse()

        return ''.join(text_as_list)

    
    #(Question:c)
    def duplicate_and_concatenate_paragraph(self):#(s)
        """
            Duplicate the paragraph and combine them such that they can be read twice in order with
            no other changes

            :input_text: The text file paragraph as a string
            :return: A string paragraph
        """
        input_text = self.read_file()#(s)

        return input_text + input_text

    
    #(Question:d)
    def remove_whitespace_from_paragraph(self):#(s)
        """
            Remove any whitespace from the paragraph except spaces between words and numbers with no
            other changes

            :input_text: The text file paragraph as a string
            :return: A string paragraph
        """
        input_text = self.read_file()#(s)

        return input_text.strip()
    

    if __name__ == '__main__':#(s)

        pass

