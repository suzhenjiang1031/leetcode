class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        # 使用 defaultdict 来存储异位词分组
        anagrams = defaultdict(list)

        # 遍历字符串列表
        for word in strs:
            # 对每个字符串排序，得到一个标准化的键
            sorted_word = ''.join(sorted(word))
            # 将当前单词添加到对应的分组中
            anagrams[sorted_word].append(word)

        # 返回所有分组
        return list(anagrams.values())

# 测试代码
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # 输出: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
