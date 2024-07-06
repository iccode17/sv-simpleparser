from hdl import SystemVerilogLexer
from dataclasses import dataclass
from lexer_tokens import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace, Module

@dataclass
class Port:
    '''Class used to store data about a verilog port'''
    direction: str
    ptype: str = None
    name: list = None
    width: str = None
    comment: list = None

    def proc_tokens(self, token, string):
        '''Processes Module.Port tokes and extract data'''
        if token is Module.Port.PortDirection:
            self.direction = string
        elif token is Module.Port.PortType:
            self.ptype = string
        elif token is Module.Port.PortName:
            if self.name is None:
                self.name = [string]
            else:
                self.name.append(string)
        elif token is Module.Port.PortWidth:
            self.width = string
        elif token is Module.Port.Comment:
            if self.comment is None:
                self.comment = [string]
            else:
                self.comment.append(string) 

    





def compare_tuples(x, token, strings=None):
    """
    Compares a tuple `x` with a given token and an optional list or tuple of strings.

    Parameters:
    - x: tuple to compare (expected to be of the form (Token, string)).
    - token: token to compare against the first element of the tuple.
    - strings: (optional) list or tuple of strings to compare against the second element of the tuple.

    Returns:
    - True if both token and any of the strings match when strings are provided.
    - True if only the token matches when strings are not provided.
    - False otherwise.
    """
    if strings is None:
        # Check only token
        return x[0] == token
    else:
        # Check both token and any of the strings
        return x[0] == token and x[1] in strings


with open('svfiles_examples/up_down_counter.sv', 'r') as fid:
    file_content = fid.read()

import pdb

port_lst = []

lexer = SystemVerilogLexer()

for token, string in lexer.get_tokens(file_content):

    if token[:2] == ('Module', 'Port'):
        if token is Module.Port.PortDirection:
            port_lst.append(Port(direction=string))
        else:
            port_lst[-1].proc_tokens(token, string)

        
print(port_lst[:])



    #if compare_tuples(tokens, Keyword, ['input', 'output']) and active == False:
    #    active = True
    #    print('Enter input')
    #    print(tokens)

    #if compare_tuples(tokens, Punctuation, [';']) and active:
    #    print('Exit' )
    #    print(tokens)
    #    active = False
    #if compare_tuples(tokens, Keyword, None) and active:
    #    print('Exit' )
    #    print(tokens)
    #    active = False
