class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        result = []
        
        # Pehle element ko fix karte hai (i se n-2 tak kyunki baad mein 2 aur elements chahiye)
        for i in range(n - 2):
            # HashMap banate hai jo store karega element -> us element ke saare indices ka list
            # Ye sirf i ke baad wale elements store karega
            seen = {}
            
            # Doosra element j, i+1 se start hota hai
            for j in range(i + 1, n):
                # Teesra element kya hona chahiye calculate karte hai
                # arr[i] + arr[k] + arr[j] = 0, so arr[k] = -(arr[i] + arr[j])
                complement = -(arr[i] + arr[j])
                
                # Check karte hai ki ye complement pehle se seen hai ya nahi
                if complement in seen:
                    # Agar complement mil gaya, to saare valid triplets add kar dete hai
                    # seen[complement] mein us element ke saare indices stored hai
                    for k in seen[complement]:
                        # Triplet mil gaya: (i, k, j) where i < k < j
                        result.append([i, k, j])
                
                # Current element (arr[j]) ko seen map mein add karte hai
                # Agar pehle se nahi hai to nayi list banate hai
                if arr[j] not in seen:
                    seen[arr[j]] = []
                # Current index j ko us element ki list mein add kar dete hai
                seen[arr[j]].append(j)
        
        return result
