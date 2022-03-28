class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        
        result = []
        intervals.sort( key = lambda x: (x[START], x[END] ) ) 
        
        for interval in intervals:
            
            if not result or ( result[-1][END] < interval[START] ):
				# no overlapping
                result.append( interval )
            
            else:
				# has overlapping
				# merge with previous interval
                result[-1][END] = max(result[-1][END], interval[END])
                
        return result
