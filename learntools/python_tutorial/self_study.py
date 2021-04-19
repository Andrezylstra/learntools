from learntools.core import *
from learntools.core import tracking 
import numpy as np
import matplotlib.pyplot as plt

def get_last_printed_string(i = -1):

    #In is a global variable with inputs.
    #global In
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

class RNALength(EqualityCheckProblem):
    _vars = ['RNA_length']
    _hint = "Use the function len()."
    _solution = CS('We do not provide the solution here')
    correct_RNA = 'ACACGUCCAACUCAGUUUGCCUGUUUUACAGGUUCGCGACGUGCUCGUACGUGGCUUUGGAGACUCCGUGGAGGAGGUCUUAUCAGAGGCACGUCAACAUCUUAAAGAUGGCACUUGUGGCUUAGUAGAAGUUGAAAAAGGCGUUUUGCCUCAACUUGAACAGCCCUAUGUGUUCAUCAAACGUUCGGAUGCUCGAACUGCACCUCAUGGUCAUGUUAUGGUUGAGCUGGUGCAGAACUCGAAGGCAUUCAGUACGGUCGUAGUGGUGAGACACUUGGUGUCCUUGUCCCUCAUGUGGGCGAAAUACCAGUGGCUUACCGCAAGGUUCUUCUUCGUAAGAACGGUAAUAAAGGAGCUGGUGGCCAUAGUUACGGCGCCGAUCUAA'
    _expected = len(correct_RNA)

class ArrayOperations(EqualityCheckProblem):
    _vars = ['x_array', 'y_array', 'figure_2']
    _hint = "You can first create a range using the function range(start, end, step). Then convert it to numpy array by passing the range to the np.array() function."
    _solution = CS('We do not provide the solution here')

    def check(self, x_array, y_array, fig):
        correct_x = np.array(range(0,31,1))
        correct_y = (correct_x*3)**2
        assert isinstance(x_array, np.ndarray) and isinstance(y_array, np.ndarray), (
            "`x_array` and `y_array` should be numpy arrays, not ({}, {})".format(type(x_array), type(y_array))
        )
        assert (x_array == correct_x).all(), ("Your `x_array` is not correct. Reminder: it should contain all integers between 0 and 30, including 0 and 30.") 
        assert (y_array == correct_y).all(), ("Your `y_array` is not correct. Check if you have performed all calculations correctly.")

        plot = fig.get_axes()[0]    
        assert len(plot.get_lines()) == 1, "You should have plotted only one line"       
        x = plot.get_lines()[0].get_xdata()
        y = plot.get_lines()[0].get_ydata()
        assert (x == correct_x).all(), ("Check if you have correct data on the x-axis")
        assert (y == correct_y).all(), ("Check if you have correct data on the y-axis")
        assert 'x' == plot.get_xlabel().lower(), "You should have `x` on your x-label"
        assert 'y' == plot.get_ylabel().lower(), "You should have `y` on your y-label"


class FirstLastElement(FunctionProblem):
    _var = 'first_and_last'
    _hint = ('''1) Remember that python starts counting from 0. 2) You can check the last element of a list using a notation like that `list_name[-1]`.''')
    _solution = CS("""""")
    _test_cases = [
        ([5,10,25,30,50], [5, 50 ]),
        ([1,1,1,1,1,1,1], [1,1]),
        ([5], [5, 5])
        ]

class CodonDict(EqualityCheckProblem):
    _vars = ['codon_dict']
    _hint = "Check how to create a dictionary in the tutorial notebook."
    _solution = CS('We do not provide the solution here')

    def check(self, codon_dict):
        correct_dict =  {'UCA' : 'Ser','GCC' : 'Ala','CGA' : 'Arg',
                        'UUU' : 'Phe','GGG' : 'Gly','AAG' : 'Lys',
                        }
      
        shared_items = {k: correct_dict[k] for k in correct_dict if k in codon_dict and correct_dict[k] == codon_dict[k]}
        correct_strings = ['Codon {} codes the {} amino acid.'.format(codon, aa) for codon, aa in correct_dict.items()]
        assert len(codon_dict) == len(correct_dict), ("Your dictionary should have {} elements but it has {}"
                                                   .format(len(correct_dict), len(codon_dict)))
        assert len(shared_items) == len(correct_dict), ("Your dictionary has {} elements but only {} correct elements. Check the spelling."
                                                        .format(len(codon_dict), len(shared_items)))
        #TODO fix the check for printing. 
        # local_vars = locals()
        # assert any([are_strings_the_same(correct_string, get_print_output_colab("print('c", **local_vars)) for 
                    # correct_string in correct_strings]), ("`codon_dict` is defined correctly but the final sentence is not correct, perhaps you have a typo?")


class YeastCompetition(EqualityCheckProblem):
    import matplotlib.pyplot as plt
    _vars = ['figure_5a']
    _hint = '''Check the plotting exercise in the tutorial. You should run the function plt.plot() to plot each line
    and create x and y-labels using plt.xlabel() and plt.ylabel()'''
    _solution = CS('We do not provide the solution here')

    def check(self, fig):
      time = [0, 12, 24, 36, 48, 60, 72, 84, 96]
      co2_strain1 = [0, 0.8, 2.5, 3.8, 4.5, 4.9, 5.0, 5.2, 5.3]
      co2_strain2 = [0, 0.1, 0.3, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6]

      plot = fig.get_axes()[0]    
      assert len(plot.get_lines()) == 2, "You should have plotted two different lines."
           
      markers = [line.get_marker() for line in plot.get_lines()]
      assert markers != ['-', '-'], "You should plot the data as points, not lines."
      assert markers == ['o', 'o'], "You should plot the data as points."

      for line in plot.get_lines():
        x = line.get_xdata()
        y = line.get_ydata()
        assert (x == time).all(), ("Check if you have correct data on the x-axis")
        assert any(
            [
             (y == co2).all() for co2 in [co2_strain1, co2_strain2]
            ]), ("One of the lines does not have correct data.")
      assert 'time' in plot.get_xlabel().lower(), "You should have the word time with units in your x-label."
      assert 'co2' in plot.get_ylabel().lower(), "You should have the word CO2 with units in your y-label."

class YeastCompetition2(EqualityCheckProblem):
    import matplotlib.pyplot as plt
    _vars = ['figure_5b']
    _hint = "To add element to a list use the .append() function."
    _solution = CS('''
    The new points are probably a measurment artifact,
    since the amount of CO2 couldn't decrease biologically in this experiment.''')

    def check(self, fig):
      time = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108]
      co2_strain1 = [0, 0.8, 2.5, 3.8, 4.5, 4.9, 5.0, 5.2, 5.3, 4.0]
      co2_strain2 = [0, 0.1, 0.3, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6, 0.3]

      plot = fig.get_axes()[0]    
      assert len(plot.get_lines()) == 2, "You should have plotted two different lines."
           
      markers = [line.get_marker() for line in plot.get_lines()]
      assert markers != ['-', '-'], "You should plot the data as points, not lines."
      assert markers == ['o', 'o'], "You should plot the data as points."

      for line in plot.get_lines():
        x = line.get_xdata()
        y = line.get_ydata()
        assert (x == time).all(), ("Check if you have correct data on the x-axis")
        assert any([(y == co2).all() for co2 in [co2_strain1, co2_strain2]]), (
            "One of the lines doesn't have correct data."
        )
      assert 'time' in plot.get_xlabel().lower(), "You should have the word time with units in your x-label."
      assert 'co2' in plot.get_ylabel().lower(), "You should have the word CO2 with units in your y-label."


class SubstrateInhibition(EqualityCheckProblem):
    _vars =['michaelis_menten','mm_substrate_inhibition']
    _hint = ("1) Copy paste the michaelis_menten fucntion from the tutorials. Use it as a basis for the substrate_inhibition function."
            "2) Be careful with the order of math operations. "
            "3) Pay attention to the order of the input arguments (S, Vmax, Km, Kinh)")
    _solution = CS("""""")
    def check(self, mm, substrate_inhibiton):
      
      def correct_substrate_inhibition(S, Vmax, Km, Kinh):
          v = Vmax * S / (Km + S * (1 + S / Kinh))
          return round(v,2)
      def correct_mm(S, Vmax, Km):
          v = Vmax * S / (Km + S)
          return round(v,2)
      assert (round(mm(50, 100, 5),2) == correct_mm(50, 100, 5)), "Check your `michaelis_menten` function"
      assert (round(mm(10, 50, 25),2) == correct_mm(10, 50, 25)), "Check your `michaelis_menten` function"
      assert (round(substrate_inhibiton(1, 10, 0.2,5),2)== correct_substrate_inhibition(1, 10, 0.2,5)), "Check your `mm_substrate_inhibition` function"
      assert (round(substrate_inhibiton(10, 50, 5,5),2)== correct_substrate_inhibition(10, 50, 5,5)), "Check your `mm_substrate_inhibition` function"

class SubstrateInhibitionPlots(EqualityCheckProblem):
    _var = 'figure_6b'
    _hint = '''Use a numpy array (np.array) to define the substrate range. If you get stuck with plotting check how it was done in the tutorial.'''
    _solution = CS("""
    Substrate inhibition kinetics achieves flatter response in certain substrate ranges. \n
    For example, see the range from 30 μM to 50 μM. \n
    According to she standard Michaelis-Menten kinetics the rate changes from ~25 to ~35 μM/min (an increase by 40%!), \n
    while in case of substrate inhibition kinetics the rate only slightly varies around 23 μM/min
    """)

    def check(self, fig):
      vmax_km_kinh = [(50, 25, None),(50, 25, 10),(50, 25, 75)]
      def correct_function(S, Vmax, Km, Kinh):
        if Kinh == None:
          v = Vmax * S / (Km + S)
          return round(v,2)
        else:
          v = Vmax * S / (Km + S * (1 + S / Kinh))
          return round(v,2)

      plot = fig.get_axes()[0]    
      assert len(plot.get_lines()) == 3, "You should have plotted two different lines."
           
      for line in plot.get_lines():
        x = line.get_xdata()
        y = line.get_ydata()
        assert (x[0] == 0) and (x[-1] == 100), ("The first and the last points on the x-axis should be 0 and 100 respectively.")
        assert any([( abs(y == correct_function(x, Vmax, Km, Kinh))<0.01 ).all() for (Vmax, Km, Kinh) in vmax_km_kinh])

      assert plot.get_xlabel() is not None, "You should add a proper x-label."
      assert plot.get_ylabel() is not None, "You should add a proper y-label."


qvars = bind_exercises(globals(), [
    RNALength,
    ArrayOperations,
    FirstLastElement,
    CodonDict,
    YeastCompetition,
    YeastCompetition2,
    SubstrateInhibition,
    SubstrateInhibitionPlots,
    ],
    var_format='ex_{n}',
    var_names = ['ex_1', 'ex_2', 'ex_3','ex_4','ex_5a', 'ex_5b', 'ex_6a', 'ex_6b']
    )
__all__ = list(qvars)


def count_solved_exercises(exercises = __all__):
  results = []
  for ex in exercises:
    if ex.startswith('ex'):
      try:
        result = eval(ex + "._last_outcome")
        if result == tracking.OutcomeType.PASS:
          results.append('Correct')
        else:
          results.append('Not correct or not solved')
      except:
        pass
  return results.count('Correct')


feedback_options = {(8,8) : "Really great job!",
            (5,7) : "You did a good job! You could try a bit more and maybe ask advice from teaching assistants or fellow students to get everything done.",
            (1,5) : "You have solved some exercises. Perhaps you need to spend more time with the exercises or ask for help from teaching assistants or fellow students to get a better understanding.",
            (0,0) : "You haven not solved any exercises. Please study more."}

def get_final_result():
  number_solved = count_solved_exercises()
  for (grade_min, grade_max) in feedback_options.keys():
    if (number_solved >=grade_min) and (number_solved <=grade_max):
      feedback = feedback_options[(grade_min, grade_max)]
      print("You have got {} out of {} points".format(number_solved, 8))
      print(feedback)
      break