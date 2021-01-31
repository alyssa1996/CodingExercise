'''
참고한 설명 : https://journeytosth.tistory.com/16
센서 그룹핑까지는 생각해냈는데, 어떻게 그룹핑을 해야하나 막막하던 차에
다른 사람들의 풀이를 보기 위해 검색을 했었다. 위에 적어놓은 블로그에서
정말 친절한 설명을 읽어보면서, 무릎을 탁 쳤다! 센서들을 그룹핑 하는게 아니라
센서들 간에 길이 차를 계산하고, 그 길이 차들 중에서 가장 긴 것들 순서대로
k-1개를 빼는 계산이라니. 정말 사람들이 문제에 접근하여 푸는 방식들을 볼 때마다
감탄이 절로 나오고, 나도 저만큼 하고 싶다는 생각이 든다. 
'''

n=int(input())
k=int(input())
sensors=list(map(int,input().split()))
sensors=sorted(sensors)

distances=[]
for i in range(1,n):
    distances.append(sensors[i]-sensors[i-1])
distances.sort()

for i in range(k-1):
    if len(distances)==0:
        break
    distances.pop()
print(sum(distances))
