# stm_task
 IP addresses summarization app.

# Main solution
 The kernel of app is basic summarization algorithm
 0. Convert the addresses to binary format and align them in a sorted list.
 1. Locate the bit where the common pattern of digits ends.
 2. Count the number of common bits.
 Only difference for app implementation of this algorithm is that entire list not needed,
 but only the first and last addreses. Because they differ the most.
 Finding the longest common prefix implemented using binary search.

 So the whole algorithm of this solution is:
 
 0. Run app via console
    
     For IPv4 or IPv6 addresses separately
    
```console
 ipsum.py path\to\ipv4_list_file v4

 ipsum.py path\to\ipv6_list_file v6
```
 
 1. Read IP list from file. App expects that file contents are addresses and spaces separating them.
 2. Start handling addresses. If IPv6 address is compressed with "::", unpack it. Next step are same for both types.
 3. Convert addresses to binary form.
 4. Sorting.
 5. Binary search the bitmask from the first and last addresses. 
 6. Fill bitmask's end with zeros. Convert back to regular form.
 7. Return summarized subnet and it's bitmask.
