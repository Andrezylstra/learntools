import numpy as np
import matplotlib.pyplot as plt
from learntools.core import *

def get_last_printed_string(i = -1):
    #In is a global variable with inputs.
    i = i - 1
    output = In[i]
    for line in reversed(output.split('\n')):
        if line.startswith('print('):
            string = line.replace('print(', '')[:-1]
            return eval(string)
        

def are_strings_the_same(string1, string2):
    string1_lower_no_space = string1.replace(' ', '').lower()
    string2_lower_no_space = string2.replace(' ', '').lower()
    
    if string1_lower_no_space == string2_lower_no_space:
        return True
    else:
        return False


def get_print_output_colab(input_,  **kwargs):
  from google.colab import _message
  nb = _message.blocking_request('get_ipynb')
  
  for cell in nb['ipynb']['cells']:
    if cell['cell_type'] == 'code':
      for line in cell['source']:
        if line.lower().startswith(input_):
          #selects the string between parentheses in print()
          print_str = line[line.find("(")+1:line.rfind(")")]
          #print_str = line[6:-1]
          output = eval(print_str, kwargs)
          return output
      
class JanJanssen(EqualityCheckProblem):
    _vars = ['name', 'age']
    _hint = "Define variables `name` and `age` correctly. Then use the function print() in a similar way as in `Welcome to Groningen` example."
    _solution = CS('We do not provide the solution here')

    def check(self, name, age):
        correct_name = 'Jan Janssen'
        correct_age = 32
        correct_string = 'This is {}. He is {} years old.'.format(correct_name, correct_age)
        assert name == correct_name, ("The variable `name` should contain the string `{}`. You have `{}`."
                                      .format(correct_name, name))
        assert age == correct_age, ("The variable `age` should contain the integer `{}`. You have `{}`."
                                      .format(correct_age, age))
        assert are_strings_the_same(correct_string,  get_print_output_colab("print('this is", **locals())), ('Variables `name` and `age` are defined correctly but the final sentence is not correct, perhaps you have a typo?')
   
    
class CreateEvenList(EqualityCheckProblem):
    _vars = ['even', 'length_even']
    _hint = "To create the list use the function range(start, end, step). To check the legnth use the function len()."
    _solution = CS('We do not provide the solution here')

    def check(self, even, length_even):
        correct_list = range(20,1001,2)  
        assert isinstance(length_even, int), ("The list length should be integer"
                " not `{}`").format(type(list_),)
        assert len(correct_list) == length_even, ('The length of the list should be {}, you have {}'.
                                                  format(len(correct_list), length_even))
        assert even[0] == correct_list[0], ('The first element of the list is not correct')
        assert all([i%2==0 for i in correct_list]) == True, ('Not each element in the list is an even number')

class ShoppingPriceLists(EqualityCheckProblem):
    _vars = ['shopping_list', 'price_list']
    _hint = "Create two lists `shopping_list` and `price_list`. If you forgot how to print the ouput, take a look at the Jan Janssen exercise."
    _solution = CS('We do not provide the solution here')

    def check(self, shopping_list, price_list):
        correct_shopping_list = ['banana', 'lettuce', 'cake']
        correct_price_list = [0.3, 0.9, 10]
        assert len(shopping_list) == len(correct_shopping_list), ('Your `shopping_list` has more that {} values.'.format(len(correct_shopping_list)))
        assert len(price_list) == len(correct_price_list), ('Your `price_list` has more that {} values.'.format(len(correct_price_list)))
        assert shopping_list == correct_shopping_list, ("Your shopping list doesn't contain the correct products")
        assert price_list == correct_price_list, ("Your price list doesn't contain the correct values.")


class AppendElementToList(EqualityCheckProblem):
    _vars = ['shopping_list', 'price_list']
    _hint = "Use the `.append(element)` method on the previosly created lists."
    _solution = CS('We do not provide the solution here')

    def check(self, shopping_list, price_list):
        correct_shopping_list = ['banana', 'lettuce', 'cake', 'cheese']
        correct_price_list = [0.3, 0.9, 10, 6]
        assert len(shopping_list) == len(correct_shopping_list), ('Your `shopping list` has more that {} values.'.format(len(correct_shopping_list)))
        assert len(price_list) == len(correct_price_list), ('Your `shopping list` has more that {} values.'.format(len(correct_price_list)))
        assert shopping_list == correct_shopping_list, ("Your shopping list doesn't contain the correct products")
        assert price_list == correct_price_list, ("Your price list doesn't contain the correct values.")
        
class EnzymesDict(EqualityCheckProblem):
    _vars = ['enzymes']
    _hint = "See the rules above on how to create a dictionary."
    _solution = CS('We do not provide the solution here')

    def check(self, enzymes):
        correct_dict = {'glucose-6-phosphate dehydrogenase': 'pentose phosphate pathway',
                        'citrate synthase': 'TCA',
                        'glyceraldehyde-3-phosphate dehydrogenase': 'glycolysis'}
        
        shared_items = {k: correct_dict[k] for k in correct_dict if k in enzymes and correct_dict[k] == enzymes[k]}
        assert len(enzymes) == len(correct_dict), ("Your dictionary should have {} elements but it has {}"
                                                   .format(len(correct_dict), len(enzymes)))
        assert len(shared_items) == len(correct_dict), ("Your dictionary has {} elements but only {} correct elements. Check the spelling."
                                                        .format(len(enzymes), len(shared_items)))
        
class CreateArray(EqualityCheckProblem):
    import numpy as np
    _vars = ['a']
    _hint = "See the rules above on how to create an array."
    _solution = CS('We do not provide the solution here')

    def check(self, a):
        correct_array = np.array([4,5,9,11,7])
        assert isinstance(a, np.ndarray), ("You should create a `np.array`, not `{}`").format(type(a),)   
        assert len(a) == len(correct_array), ('Your array `a` should have {} elements.'.format(len(correct_array)))
        assert (a == correct_array).all(), ('Did you put the numbers in the arrary in the correct order?')
        
class OperateWithArray(EqualityCheckProblem):
    import numpy as np
    _vars = ['a_mult', 'a_div', 'a_power']
    _hint = "See the rules above on how to create an array."
    _solution = CS('We do not provide the solution here')

    def check(self, a_mult, a_div, a_power):
        correct_array = np.array([4,5,9,11,7])
        assert (a_mult == correct_array*2).all(), ("You didn't mulptiply the array correctly")   
        assert (a_div == correct_array/6).all(), ("You didn't divide the array correctly")   
        assert (a_power == correct_array**2).all(), ("You didn't exponentiated the array correctly")   
        
class MichaelisMenten(FunctionProblem):
    _var = 'Michaelis_Menten'
    #Alex: Douwe, I think we should rename the function to michaelis_menten()
    _hint = '''Use the same syntax for defining functions as described above, 
    ```python
    def function_name(variables):
        #function_body here
        return output```
    '''
    _solution = CS("""""")
    def correct_function(S, Vmax, Km):
        v = Vmax * S / (Km + S)
        return v
    _test_cases = [
        ((10, 50, 25), correct_function(10, 50, 25)),
        ((50, 100, 5), correct_function(50, 100, 5)),
        ((1, 10, 0.2), correct_function(1, 10, 0.2))
        ]
    
class PlotThreeLines(EqualityCheckProblem):
    import matplotlib.pyplot as plt
    
    _vars = ['figure_6d']
    _hint = "See the rules above on how to create an array."
    _solution = CS('We do not provide the solution here')

    def check(self, fig):
         vmax_km = [(50,25),(50,5),(50,50)]
         def michaelis_menten(S, Vmax, Km):
            v = Vmax * S / (Km + S)
            return v
         plot = fig.get_axes()[0]
         colors = set([line.get_color() for line in plot.get_lines()])
         assert len(colors) == 3, "You should use three different colors for the plot."
         
         assert len(plot.get_lines()) == 3, "You should have plotted three different lines."
         
         linewidths = [line.get_linewidth() for line in plot.get_lines()]
         assert linewidths == [5, 5, 5], "All lines should have linewidth = 5"
         
         linestyles = [line.get_ls() for line in plot.get_lines()]
         assert linestyles == ['-', '-', '-'], "All lines should have solid linestyle ('-')."

         for line in plot.get_lines():
           S = line.get_xdata()
           v = line.get_ydata()
           assert any([(v == michaelis_menten(S, Vmax, Km)).all() for (Vmax, Km) in vmax_km]), (
               '''You should have plotted three different lines with Km = 5, 25, 50 mM and Vmax = 50 mM/s.
               At least one of the lines is missing.'''
           )


qvars = bind_exercises(globals(), [
    JanJanssen,
    CreateEvenList,
    ShoppingPriceLists,
    AppendElementToList,
    EnzymesDict,
    CreateArray,
    OperateWithArray,
    MichaelisMenten,
    PlotThreeLines
    ],
    var_format='ex_{n}',
    var_names = ['ex_1a', 'ex_2a', 'ex_2b', 'ex_2c',
                 'ex_3','ex_4a', 'ex_4b', 'ex_5a', 'ex_6d']
    )
__all__ = list(qvars)
     