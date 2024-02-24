'''
       
       products = ['mobile','mouse','moneypot','monitor','mousepad']
       searchWord = 'mouse'
       '''


class Solution:
    def SearchSuggestion(self,products:list[str], searchWord:str)-> list[list[str]]:
          
        products.sort()

        l,r = 0, len(products)-1

        results = []

        for i in range(len(searchWord)):
            search = searchWord[i]

            while l <= r and (len(products[l])<=i or products[l][i]!=search):
                l+=1
            while l <= r and (len(products[r])<=i or products[r][i]!=search):
                r+=1
            
            world_left = r-l+1
            if world_left >=3:
                results.append([products[l],products[l+1],products[l+2]])
            elif world_left == 2:
                results.append([products[l],products[l+1]])
            elif world_left == 1:
                results.append([products[l]])
            else:
                results.append([])
        return results
    
ss = Solution()

products = ['mobile','mouse','moneypot','monitor','mousepad']
searchWord = 'mouse'   

print(ss.SearchSuggestion(products=products,searchWord=searchWord))
