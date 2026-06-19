from typing import List
from dataclasses import dataclass

@dataclass
class trienode:
  best_idx: int
  children: list

class Solution:
  def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    wordsContainer = map(lambda x: x[::-1], wordsContainer)
    words_container = list(enumerate(wordsContainer))
    words_container.sort(key=lambda x: len(x[1]))

    ch_idx = lambda x: ord(x)-97

    trie = trienode(best_idx = words_container[0][0], children=[None for _ in range(26)])

    for word in words_container:
      # print("processing:",word)
      curr = trie
      for ch in word[1]:
        idx=ch_idx(ch)
        if curr.best_idx is None:
          curr.best_idx = word[0]
        if curr.children[idx] is None:
          curr.children[idx] = trienode(word[0], [None for _ in range(26)])
        curr=curr.children[idx]
        
  
    ans=[]
    for query in wordsQuery:
      query=query[::-1]
      curr=trie
      for ch in query:
        idx = ch_idx(ch)
        if curr.children[idx] is None:
          ans.append(curr.best_idx)
          break
        curr=curr.children[idx]
      else:
        ans.append(curr.best_idx)
    
    return ans