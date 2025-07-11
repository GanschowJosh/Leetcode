def groupAnagrams(strs):
        d = {}
        for string in strs:
            bucket = str(sorted(string))
            if bucket in d:
                d[bucket].append(string)
            else:
                d[bucket] = [string]
        return list(d.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))