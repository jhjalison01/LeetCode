class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 각 문자가 문자열에서 몇 번씩 나타나는지 딕셔너리로 반환
        note, mag = Counter(ransomNote), Counter(magazine)
        # magazine에 있는 문자로 ransomNote를 만들 수 있는지 확인
        if note & mag == note:
            return True
        return False