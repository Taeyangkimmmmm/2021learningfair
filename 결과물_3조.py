print("<2022학년도 상명대학교 역사콘텐츠전공 교과우수전형>_내신등급 및 합불 가능성을 산출해 드립니다.")
print("국어/영어/수학/사회의 석차등급과 이수단위, 진로우수선택과목의 성취등급과 이수단위를 순서대로 입력하세요.")
print("단,석차등급은 1~9 사이 소수점 둘째 자리수까지, 성취등급의 경우 A는 1, B는 3, C는 5로 입력하세요.")
print("진로우수선택과목은 최대 3개까지 입력 가능하고, 없을 경우에는 등급과 이수단위란에 반드시 0을 입력하세요")

subject1 = 4
subject2 = 3
grade = []
sum = 0


for i in range(subject1):
     
     gr=float(input("석차등급을 입력하시오 : "))
     unit=int(input("이수단위를 입력하시오 :"))

     sum1 = sum + gr*unit
     sum2 = sum + unit


for j in range(subject2):
     
     gr=float(input("성취등급을 입력하시오 : "))
     unit=int(input("이수단위를 입력하시오 :"))

     sum3 = sum + gr*unit
     sum4 = sum + unit

     
if sum3 == 0 and sum4 == 0 :
     agv = sum1/sum2

else :
     agv = (sum1/sum2 + sum3/sum4)/2

cut=2
n = agv
n = float(int(n*(10**cut)))
n /=(10**cut)
     

print("내신등급: ", n)


if n <= 2.23 :
     print("안정")
     
elif 2.23 < n <= 2.59 :
     print("적정")
     
else :
     print("위험")
