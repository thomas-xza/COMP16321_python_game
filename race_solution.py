"""
This is a stub for the comp16321 midterm.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.

NOTE: You can create as many more methods as you need. However, you need to add 
self as a parameter of the new method and to call it with the prefix self.name 

EXAMPLE:

def class_table_result(self, boat_type, race_results):#(s)
    strings_value = "0601-0501-0702-0803-0904-0405-0306-0207-1008-0609-0110"
    single_boat = self.remove_highest_value(strings_value)
    return(single_boat)

def remove_highest_value(self, strings_value):
    strings_value.pop(10)
    return strings_value

"""

class Races:#(s)

    def read_results(self):#(s)
    
        """
        Read in the text file and save the races_results into a python list

        :return: A list of strings denoting each race_result
        """
        # Your code here

        pass#(s)

    def race_result(self, boat_type, race_number, results_string):#(s)

        """
        Query results_string which is read form the input.txt and  get the  result
        for the given params
        
        :param: boat_type: An integer denoting which type of boat 
        :param: race_number: An integer denoting which race
        :return: A string with the race result for the given boat_type and race_number
        """
        # Your code here

        pass#(s)

    def class_table_result(self, boat_type, results_string):#(s)

        """
        Output the results for a given boat_type

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf
        """

        # Your code here

        pass#(s)

    def class_table_discard_result(self, boat_type, results_string):#(s)

        """
        Output the class table discard string

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf
        """
        # Your code here

        pass#(s)

    def medal_table_result(self, results_string):#(s)

        """
        Output the class table discard string

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf 
        """

        # Your code here

        pass#(s)


if __name__ == '__main__':#(s)
    # You can place any ad-hoc testing here
    # e.g. my_instance = Races()
    # e.g. section_1 = my_instance.read_results()
    # e.g. print(section_1)

    pass#(s)