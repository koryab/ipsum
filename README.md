# ipsum
 IP addresses summarization app, supposed to summarize list of IP addresses to common subnet.
 IPv4 and IPv6 addresses supported.

 The kernel of app is basic summarization algorithm: 
 
 0. Convert the addresses to binary format and align them in a sorted list.
 1. Locate the bit where the common pattern of digits ends.
 2. Count the number of common bits.
 
 Only difference for app implementation of this algorithm is that entire list not needed,
 but only the first and last addreses. Because they differ the most.
 Finding the longest common prefix implemented using binary search.

# Installation
 
 Download [package](https://github.com/koryab/ipsum/blob/main/dist/ipsum-0.0.1.tar.gz) from this repository.
 Intstall it using `pip`:
 
 ```console
 python -m pip install path\to\package\ipsum-0.0.1.tar.gz
 ```

# Run
 Run app via console.
 For IPv4 or IPv6 addresses respectively:

 ```console
  python -m ipsum path\to\ipv4_list_file v4

  python -m ipsum path\to\ipv6_list_file v6
 ```
 First console argument is "path\to\ip_list_file", and second one is version of IP protocol `v4` for IPv4 and `v6` for IPv6.

 # Algorithm and complexity  
 
 1. Read IP list from file. App expects that file contents are addresses and spaces separating them.
 2. Start handling addresses. If IPv6 address is compressed with **"::"**, unpack it. Next steps are same for both types.
 3. Convert addresses to binary form.
 4. Sorting.
 5. Binary search the bitmask from the first and last addresses. 
 6. Fill bitmask's end with zeros. Convert back to regular form.
 7. Return summarized subnet and it's bitmask.

 There used two algorithms: Binary Search **O(log n)** and standart Python sorting - Timsort **O(n log n)**.
 Consequently, total complexity is **O(n log n)**.
