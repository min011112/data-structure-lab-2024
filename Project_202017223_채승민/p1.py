# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = 0
    median = 0
    result = [0,0]
    
    # 평균 구하기 위해서 입력의 합을 입력의 크기로 나눠준다
    mean = sum(input)//len(input)

    #중앙값을 계산하기 위해 입력을 정렬하고 중앙값을 median에 저장한다
    #이때 sort 대신 sorted를 사용해 정렬 후 반환까지 해준 뒤 a 리스트에 저장한다.
    a = sorted(input)
    median = a[len(input)//2]
    
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
