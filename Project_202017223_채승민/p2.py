def problem2(input):
    stack = []
    open_number = 0
    #입력으로 들어오는 문자열을 하나씩 받아준 뒤 (면 stack에 넣고
    # ')' 일 때는 stack에 저장된 요소가 없으면 앞에 '('을 추가할 개수를 늘리고
    #저장된 요소가 있을 때는 stack에서 ')'를 제거한다.
    for char in input:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack)>0:
                stack.pop()
            else:
                open_number += 1
    #stack에 남아있는 '('의 개수는 뒤에 추가할 ')'의 개수이다.
    close_number = len(stack)
    
    result = open_number + close_number
    return result

# 입력 예시
input = ")))()"

# 함수 호출 및 결과 확인
result = problem2(input)

assert result == 3
print("정답입니다.")
