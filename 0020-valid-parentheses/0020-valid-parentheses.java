import java.util.*;
class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack();
        
        try
        {
            for(char c: s.toCharArray())
            {
                if(c=='('||c=='{'||c=='[')
                {
                    stack.push(c);
                }
                else
                {
                    if(c==')')
                    {
                        if(stack.peek() == '(')
                        {
                            stack.pop();
                        }
                        else
                        {
                            return false;
                        }
                    }

                    else if(c=='}')
                    {
                        if(stack.peek() == '{')
                        {
                            stack.pop();
                        }
                        else
                        {
                            return false;
                        }
                    }

                    else if(c==']')
                    {
                        if(stack.peek() == '[')
                        {
                            stack.pop();
                        }
                        else
                        {
                            return false;
                        }
                    }
                }
            }
            
        }
        catch(EmptyStackException e)
        {
            return false;
        }
        
        
        return stack.isEmpty();
    }
}