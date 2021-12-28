
import operator

from cv2 import ORB_FAST_SCORE 
"""
uppgift 2 
--------------------------------------------------------------------------------------------------------------------------------
"""
# a function that removes commenets and nested comments from a text (comments begning with ** and nested comments with (*(**))
def comment_remover(Text): 
    
    offset = 0 ; comments =0 ; New_Text = []
    while offset < len(Text): 
        if Text[offset] == "(*": 
            offset += 2 
            comments  += 1 
        elif Text[offset] == "*)" and comments > 0:
            offset += 1 
            comments -= 1 
        else: 
            if comments == 0: 
                New_Text.append(Text[offset])
            offset += 1 
    return ' '.join(New_Text)




# Test our Text_without_comments

#Test_text = "Hi this is the (* Hi this (* and any of the allternative *) hi how are the dummies *) uncommented text".split()
#print(comment_remover(Test_text))

"""
uppgift 3
--------------------------------------------------------------------------------------------------------------------------------
"""
def postfix(stack): 
    return NotImplementedError

"""
uppgift 4 : stack
--------------------------------------------------------------------------------------------------------------------------------
input = "it was - the best - of times - - - it was - the - -"
Stack = [it]  #final stack
printed = {
    was 
    best
    times
    of 
    the
    was
    the 
    it
}
left on the stack = 1 
"""

"""
uppgift 5 : queue
--------------------------------------------------------------------------------------------------------------------------------
input = "it was - the best - of times - - - it was - the - -"
Stack = [ the ]  #final queue 
printed = {
    it
    was
    the 
    best 
    it 
    times 
    it 
    was 
}
left on the stack = 1 
"""
"""
uppgift 6 
--------------------------------------------------------------------------------------------------------------------------------
becaues it is queue the becaues we push the in order they should be poped out somehow in order
"""
