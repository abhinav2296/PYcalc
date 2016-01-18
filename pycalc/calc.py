from __future__ import division             # For float division of two integers
from gi.repository import Gtk
import sys,math,re

class Handler:                              #Class of functions connected to widgets of gui of calculator
    text_list=[]    
    opth=0                                  #To count the occurrences of open parenthesis in the expression
    cpth=0                                  #To count the occurrences of closed parenthesis in the expression
    dflag=0                                 #Flag to check the decimal in the last number written
    lastans = None                          #Last answer calculated by calculator
    pi="3.141592653589793"
    e="2.718281828459045"
    ops = [pi,e,')']                    
    bset = ['*log(','log(','*ln(','ln(','(','*(']       #Set containing elements that end with open parenthesis

    def __init__ (self):
        self.textview=builder.get_object("textview1")
        self.textview.set_justification(Gtk.Justification.RIGHT)
        self.textview.set_editable(False)
        self.viewbuffer = self.textview.get_buffer()
        self.textview.set_cursor_visible(False)
        
    def onDeleteWindow (self,*args):
        Gtk.main_quit(*args)
        sys.exit()
        
    def on_button1_clicked (self, button1): #Press Button1 for '7'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("7")
        self.text_list.append('7')
        
    def on_button2_clicked (self, button2): #Press Button2 for '4'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("4")
        self.text_list.append('4')
    
    def on_button3_clicked (self, button3): #Press Button3 for '1'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("1")
        self.text_list.append('1')
    
    def on_button4_clicked (self, button4): #Press Button4 for clearscreen
        self.viewbuffer.set_text("")
        del self.text_list[:]
        self.dflag=0
        self.opth=0
        self.cpth=0
        
    def on_button5_clicked (self, button5): #Press Button5 for '8'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("8")
        self.text_list.append('8')
    
    def on_button6_clicked (self, button6): #Press Button6 for '5'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("5")
        self.text_list.append('5')
    
    def on_button7_clicked (self, button7): #Press Button7 for '2'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("2")
        self.text_list.append('2')
    
    def on_button8_clicked (self, button8): #Press Button8 for '0'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("0")
        self.text_list.append('0')
    
    def on_button9_clicked (self, button9): #Press Button9 for '9'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("9")
        self.text_list.append('9')
    
    def on_button10_clicked (self, button10): #Press Button10 for '6'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("6")
        self.text_list.append('6')
    
    def on_button11_clicked (self, button11): #Press Button11 for '3'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor ("3")
        self.text_list.append('3')
    
    def on_button12_clicked (self, button12): #Press Button12 for evaluation of expression
        if (len(self.text_list)>0):
            text = ''.join(self.text_list)
            re.sub(r'(?<!\.)\b0+(?!\b)', '', text)
            text=text.replace('^','**')
            text=text.replace('log','(1/2.303)*math.log')
            text=text.replace('ln','math.log')
            text=text.replace('e','2.718281828459045')
            if (self.opth >= self.cpth):
                text+=')'*(self.opth-self.cpth)
            else:
                text = '('*(self.cpth-self.opth) + text
            #print text
            try:
                ans=eval(text)
                if (ans%1==0):
                    ans=int(ans)
                if (abs(ans)>(10**15) or abs(ans)<(10**-6)):
                    x='%E'%ans
                    ans=x
                ans=str(ans)
            except:
                ans="ERROR"
            self.viewbuffer.insert_at_cursor('\n\n'+ans)
            self.lastans=ans
            self.lastans.replace('e','E')
            del self.text_list[:]
            self.opth=0
            self.cpth=0
    
    def on_button13_clicked (self, button13): #Press Button13 for addition operation '+'
        if len(self.text_list)>0 and not ((self.text_list[-1]).isdigit() or (self.text_list[-1] not in [' - ',' * ',' + ',' / ']) or '.' in self.text_list[-1]):
            del self.text_list[-1]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
        if (len(self.text_list)>0):
            self.viewbuffer.insert_at_cursor (" + ")
            self.text_list.append(' + ')
            self.dflag=0
        elif (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.viewbuffer.insert_at_cursor (" + ")
            self.text_list.append(' + ')
            self.dflag=0
            self.lastans=None
    
    def on_button14_clicked (self, button14): #Press Button14 for subtraction operation '-'
        if len(self.text_list)>0 and not ((self.text_list[-1]).isdigit() or self.text_list[-1]!=' + ' or '.' in self.text_list[-1]):
            del self.text_list[-1]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
        if (len(self.text_list)>0):
            self.viewbuffer.insert_at_cursor (" - ")
            self.text_list.append(' - ')
            self.dflag=0
        elif (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.viewbuffer.insert_at_cursor (" - ")
            self.text_list.append(' - ')
            self.dflag=0
            self.lastans=None
        
    def on_button15_clicked (self, button15): #Press Button15 for multiplication operation '*'
        if len(self.text_list)>0 and not ((self.text_list[-1]).isdigit() or self.text_list[-1] in self.ops or '.' in self.text_list[-1]):
            del self.text_list[-1:]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
        if (len(self.text_list)>0):
            self.viewbuffer.insert_at_cursor (" * ")
            self.text_list.append(' * ')
            self.dflag=0
        elif (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.viewbuffer.insert_at_cursor (" * ")
            self.text_list.append(' * ')
            self.dflag=0
            self.lastans=None
        
    def on_button16_clicked (self, button16): #Press Button16 for division operation '/'
        if len(self.text_list)>0 and not ((self.text_list[-1]).isdigit() or self.text_list[-1] in self.ops or '.' in self.text_list[-1]):
            del self.text_list[-1:]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
        if (len(self.text_list)>0):
            self.viewbuffer.insert_at_cursor (" / ")
            self.text_list.append(' / ')
            self.dflag=0
        elif (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.viewbuffer.insert_at_cursor (" / ")
            self.text_list.append(' / ')
            self.dflag=0
            self.lastans=None
            
    def on_button17_clicked (self, button17): #Press Button17 for open parenthesis '('
        m=None
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            m=self.lastans
            self.lastans=None
        self.viewbuffer.insert_at_cursor ("(")
        if len(self.text_list)>0 and ((self.text_list[-1]).isdigit() or self.text_list[-1]==m or self.text_list[-1]==self.pi or self.text_list[-1]==self.e):
            self.text_list.append('*(')
        else:
            self.text_list.append('(')
        self.opth+=1
    
    def on_button18_clicked (self, button18): #Press Button18 for closed parenthesis ')'
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.lastans=None
        self.viewbuffer.insert_at_cursor (")")
        self.text_list.append(')')
        self.cpth+=1
        
    def on_button19_clicked (self, button19): #Press Button19 for log to the base 'e'
        m=None
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            m=self.lastans
            self.lastans=None
        self.viewbuffer.insert_at_cursor ("ln(")
        if len(self.text_list)>0 and ((self.text_list[-1]).isdigit() or self.text_list[-1]==m or self.text_list[-1]==self.pi or self.text_list[-1]==self.e):
            self.text_list.append('*ln(')
        else:
            self.text_list.append('ln(')
        self.opth+=1
        
    def on_button20_clicked (self, button20): #Press Button20 for power operation
        if len(self.text_list)>0 and not ((self.text_list[-1]).isdigit() or self.text_list[-1] in self.ops):
            del self.text_list[-1:]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            self.lastans=None
        self.viewbuffer.insert_at_cursor ("^")
        self.text_list.append('^')
    
    def on_button21_clicked (self, button21): #Press Button21 to undo last entry
        if len(self.text_list)>0:
            if (self.text_list[-1] in self.bset):
                self.opth-=1
            elif (self.text_list[-1] == ')'):
                self.cpth-=1
            del self.text_list[-1]
            text = ''.join(self.text_list)
            self.viewbuffer.set_text(text)
            if len(self.text_list)>0 and '.' not in self.text_list[-1]:
                self.dflag=0
            elif len(self.text_list)>0 and '.' in self.text_list[-1]:
                self.dflag=1
        
    def on_button22_clicked (self, button22): #Press Button22 for 'pi'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor(self.pi)
        self.text_list.append(self.pi)
        
    def on_button23_clicked (self, button23): #Press Button23 for 'e'
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor(self.e)
        self.text_list.append(self.e)
        
    def on_button24_clicked (self, button24): #Press Button24 for exponentiation of 10
        if (self.lastans!=None):
            self.lastans=None
            self.viewbuffer.set_text('')
        self.viewbuffer.insert_at_cursor("10^")
        self.text_list.append('10^')
        
    def on_button25_clicked (self, button25): #Press Button25 for decimal
        if (self.lastans!=None and self.lastans!='ERROR'): 
            if '.' in self.lastans:
                self.dflag=1
        if self.dflag==0:
            self.viewbuffer.insert_at_cursor(".")
            self.text_list.append('.')
            self.dflag=1
       
    def on_button26_clicked (self, button26): #Press Button26 for logarithm to the base 10
        m=None
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            m=self.lastans
            self.lastans=None
        self.viewbuffer.insert_at_cursor ("log(")
        if len(self.text_list)>0 and ((self.text_list[-1]).isdigit() or self.text_list[-1]==m or self.text_list[-1]==self.pi or self.text_list[-1]==self.e):
            self.text_list.append('*log(')
        else:
            self.text_list.append('log(')
        self.opth+=1
    
    def on_button27_clicked (self, button27): #Press Button27 for exponentiation of 'e'
        m=None
        if (len(self.text_list)==0 and self.lastans!=None and self.lastans!="ERROR"):
            self.viewbuffer.set_text(self.lastans)
            self.text_list.append(self.lastans)
            m=self.lastans
            self.lastans=None
        self.viewbuffer.insert_at_cursor("e^")
        if (len(self.text_list)>0 and ((self.text_list[-1]).isdigit() or self.text_list[-1]==')' or self.text_list[-1]==m or self.text_list[-1]==self.e or self.text_list[-1]==self.pi)):
            self.text_list.append('*e^')
        else:
            self.text_list.append('e^')
        
builder = Gtk.Builder()
builder.add_from_file("Calculator.glade")
window = builder.get_object("window1")
builder.connect_signals(Handler())
window.show_all()
Gtk.main()
