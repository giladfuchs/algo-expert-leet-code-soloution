from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = {}
        for _ in paths:
            files = _.split(' ')
            path = files.pop(0)
            for file in files:
                file_path, content = file.split('.txt')
                full_path = f"{path}/{file_path}.txt"
                if ans.get(content):
                    ans[content].append(full_path)
                else:
                    ans[content] = [full_path]

        ans = [_ for _ in ans.values() if len(_)> 1]
        return ans
