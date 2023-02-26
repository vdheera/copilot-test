# write a function to find the longest common prefix string amongst an array of strings
# if there is no common prefix, return an empty string ""
# example:
# input: ["flower","flow","flight"]
# output: "fl"
# input: ["dog","racecar","car"]
# output: ""
# explanation: there is no common prefix among the input strings
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
