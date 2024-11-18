class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack();
        
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
                    if(stack.size()==0)
                    {
                        return false;
                    }
                    else
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
                }
                
                else if(c=='}')
                {
                    if(stack.size()==0)
                    {
                        return false;
                    }
                    else
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
                }
                
                else if(c==']')
                {
                    if(stack.size()==0)
                    {
                        return false;
                    }
                    else
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
        return stack.isEmpty();
    }
}