#인트로
print('으으... 여긴 어디지?')
print('조금 전까지 가족들과 함께 있었는데... 커다란 손이 갑자기 날 덮친 후 의식을 잃었다.')
print('주변이 어두워서 잘 보이지 않는다. 대신 온몸에 한기가 느껴진다.(엔터를 입력해서 진행하세요)')
input()
print('나는 누구...?')
print('높은 곳에서 떨어졌는지 몸이 물러졌다.')
print('두통 때문에 아무것도 기억나지 않는다.')
input()

#첫번째 조사
while True:
    direction = input('일단 주변을 둘러볼까?(위, 아래, 왼쪽, 오른쪽을 한번씩 순서대로 입력): ')
    if direction == '위' :
        print('> 춥다. 히터가 고장 난 건가?')
        input()
        continue
    elif direction == '아래':
        print('> 바닥에 정체를 알 수 없는 끈적한 액체가 가득하다. 저 캔에서 나온 건가?')
        input()
        continue
    elif direction == '왼쪽':
        print('> 추위 때문인지 벽에 성에가 가득하다.')
        input()
        continue
    elif direction == '오른쪽':
        print('> 깜짝아!!! 저 멀리 보이는 얼어붙은 물체는 설마...... 시체?')
        break
    else:
        continue
input()
print('잘은 모르겠지만 일단 여기서 탈출해야겠어.')
input()

#물건 배열하기
grocery = ['상자', '사과박스']

input('참치캔, 사과 박스, 정체 모를 기름에 젖은 상자, 터진 포대자루 그리고 하얗게 성에가 낀 팩이 있다.')
input('물건이 가득해서 이 앞으로는 지나갈 수 없을 것 같다. 물건을 좀 정리해야 할 것 같은데...')
input()
input('[참치캔, 상자, 포대자루, 사과박스, 팩]순으로 배열해야 지나갈 수 있을 것 같다.')
print('현재 상태: [상자, 사과박스]')
input()
while True:
    tuna = input('참치캔을 몇 번째에 넣을까?(숫자만 입력): ')
    if tuna == '1':
        grocery.insert(0, '참치캔')
        print(grocery)
        break
    else:
        print('> 공간이 없다...') 
        input()
        continue
input()
while True:
    sack = input('포대자루를 몇 번째에 넣을까?(숫자만 입력): ')
    if sack == '3':
        grocery.insert(2, '포대자루')
        print(grocery)
        print('> 거의 다 왔어!')
        break
    else:
        print('> 공간이 없다...')
        input()
        continue
input()
while True:
    mask = input('팩을 몇 번째에 넣을까?(숫자만 입력): ')
    if mask == '5':
        grocery.insert(4, '팩')
        print(grocery)
        print('> 됐다! 지나갈 수 있겠어!')
        break
    else:
        print('> 공간이 없다...')
        input()
        continue
input()

#수상한 메모
while True:
    memo = input('길을 가다가 무엇인가를 발견했다. 확인해볼까?(그래, 아니 중 선택 입력): ')
    if memo == '그래' :
        input('> 메모를 발견했다. 글자가 흐려져서 잘 보이지 않지만...')
        print()
        print()
        print('               영 ? 증               ')
        print()
        print(' 2021년 11월 ??일          ')
        print('===================================')
        print(' ??명                 수량      금?  ')
        print('===================================')
        print(' 토?토                 1       ?00   ')
        print(' 치즈                   ?      ?2??   ')
        print(' 느타리버섯               2      19??   ')
        print('-----------------------------------')
        print(' ?매?액                       ?1??')
        input()
        input('> 이 메모가 뜻하는 것은 무엇일까...')
        break
    elif memo == '아니' :
        input('> 그냥 계속 걷기로 했다.')
        break
    else:
        continue
input()

#물건 쌓기
input('그러고 보니 이곳이 지하인지, 지상인지도 모른다. 위쪽에 다른 층이 있는 것 같은데...')
input('올라가 볼까?')
input('계단이나 사다리는 없지만 주변 물건을 쌓으면 올라갈 수 있을 것 같다.')
input()
input('큰 것부터 차례로 쌓아보자.')
input("(10크기의 ‘상자’/ 1크기의 ‘고무조각’/7크기의 ‘나무발판’/5크기의 ‘페트병’이 있다.)")
input("(순서대로 ‘’안의 글자만 입력)")
while True:
    물건순서=[]
    쌓기반복횟수=0
    for 쌓기반복횟수 in range(0,4):
        물건순서.append(input(':'))
    if 물건순서==['상자','나무발판','페트병','고무조각']:
        input('> 위층으로 올라왔다.')
        break
    else:
        input('쌓은 물건들이 무너져 버렸다.')
        input('처음부터 다시 쌓아야 할 것 같다.')
print()

#위층둘러보기
input('위층도 아래와 별반 다르지 않다.')
input('공기는 냉기로 가득하고 벽에는 성에가 덕지덕지 붙어 있다.')
input('아니, 조금 더 추운가?')
input('내 몸이 점점 얼어가는 건지도...')
input()
input('저 안쪽에 뭔가 윙윙 돌아가는 소리가 들린다.')
input('소리가 울릴 때마다 내 머리도 같이 둔해지는 것만 같아.')
input('어서 이곳을 나가야겠다.')
input()

#윗층 자세히 둘러보기
input('주변을 좀 더 자세하게 둘러보자.')
input('이곳을 나갈 수 있는 통로나 단서를 찾을 수 있을지도 모르니까.')
input('(빛이 있는 곳/벽/소리가 나는 곳/큰 유리병/그만 둘러본다)')
while True:
    윗층_둘러보기=input(':')
    if 윗층_둘러보기=='빛이 있는 곳':
        input()
        input('> 희미한 빛을 따라갔다.')
        input('전등이 반쯤 나갔는지 지지직거리기도 한다.')
        input('빛을 보고 달려들었는지 작은 초파리 따위들이 죽어있다.')
        input('모든 것이 단단히 얼어 있다. 초파리마저 꿈쩍하지 않는다.')
    elif 윗층_둘러보기=='벽':
        input()
        input('> 성에가 가득 낀 벽을 살펴보았다.')
        input('주변에 물건이 많은 탓에 빛이 잘 들지 않아 어둡다.')
        input('벽에 불그스름한게 묻어 있다.')
        input('...설마 피인가...?')
        input('자세히 보니 피보다는 음식물 같기도...')
        input('뭘까? 아무 냄새도 나지 않는다. 코가 얼어버렸나...')
        input('에츄!')
    elif 윗층_둘러보기=='소리가 나는 곳':
        input()
        input('> 아까부터 윙윙 울리던 소음의 근원지를 찾아갔다.')
        input('위층에 올라와서 더 추워진 게 기분 탓만은 아니었다.')
        input('찬 공기가 이곳을 통해 나오고 있었다.')
        input('여기에 계속 있다가는 몸이 더 차가워질 것만 같다.')
    elif 윗층_둘러보기=='큰 유리병':
        input()
        input('> 내 키의 2~3배쯤 되어보이는 큰 유리병이 있다.')
        input('안은 온통 붉은 것으로 가득 차 있다.')
        input('이게 뭐지...?')
        input('유리병의 뒷면에는 그림이 붙어 있다.')
        input('나와 내 친구들, 그리고 가족들과 닮은 듯한 그림.')
        input('위아래로 뭔가 적혀 있는 것이 보이지만, 저 병을 계속 쳐다볼 용기가 나지 않는다.')
        input('우리와 닮은 그림.')
        input('그 안에 가득 찬 붉은 무언가.')
    elif 윗층_둘러보기=='그만 둘러본다':
        input('> 이만하면 다 둘러본 것 같다.')
        break
    else:
        continue
    input()
    input('다른곳을 더 둘러보자.')


#유리병 지나기
print()
input('계속해서 움직이다 보니 또 다른 유리병이 보였다.')
input('습기 때문에 잘 보이지 않는다.')
input('문득 비친 내 모습은…(유리병을 닦아보세요)')
print('░░░░░░░░')
닦은횟수=0
while True:
    닦기여부=input('닦아볼까?(닦는다/그냥 간다):')
    if 닦기여부=='닦는다':
        닦은횟수+=1
        if 닦은횟수==1:
            print('동░░고░░░░')
        elif 닦은횟수==2:
            print('동그░고░붉░░')
        elif 닦은횟수==3:
            print('동그░고 붉다░')
        elif 닦은횟수==4:
            print('동그랗고 붉다.')
        else:
            print('이제 더이샹 닦지 않아도 잘 보인다.')
            break
    elif 닦기여부=='그냥 간다':
        input('이런것까지 신경쓸 시간이 없다.')
        input('빨리 나갈 단서라도 찾아야지.')
        break
    else:
        continue
input('가던 길을 계속 갔다.')



#정체추정
input()
input('이제 탈출이 머지 않은 것 같다.')
input('동시에… 내가 무엇인지 좀 알 것 같아.')
input('사실 나는… (정체를 맞혀보세요)')
정체=input(':')
if 정체=='토마토':
    input('그래… 나는 토마토였어!')
    input('나는 얼마 전까지만 해도 사랑하는 가족들과 친구들이랑 나무에 매달려 있었어.')
    input('그런 나를 누군가가 이곳으로 끌고 온 거야.')
    input('그렇다면 춥디 추운 이 곳은...')
else:
    input('> 아무래도 아직 두통이 가시지 않은 것 같아. ')
print()

#나갈까?
input('드디어 나갈 수 있는 길을 찾았다.')
input('탈출할까?')
while True:
    탈출대답=input('(나간다/나가지 않는다):')
    if 탈출대답=='나간다':
        input()
        input('밝은 빛이다!')
        input('드디어 밖으로 나왔다. 이제 집으로 돌아갈 수…!')
        input('')
        input('[어라? 토마토가 왜 밖에 나와 있지?]')
        input('[꺼낸 적 없는데... ]')
        input('[보인 김에 오늘은 토마토 파스타나 해 먹을까?]')
        break
    elif 탈출대답=='나가지 않는다':
        input()
        input('내가 있는 곳은 바로 냉장고 속이었다.')
        input('인간의 손길이 뻗치길 수 번.')
        input('나는 꽁치 통조림 뒤에 숨고, 대파 단 사이에 위장을 하며 인간에게 먹히지 않고 버텨냈다.')
        input('수많은 식재료들이 들어왔다 끌려가며 인간의 식사로 전락해 버렸지만 나는 죽지 않아!')
        input('끝까지 살아남을거야!')
        break
    else:
        continue

input('────────────────────\n──────░──────░──────\n───────░────▒░──────\n──────▒░▒▒█▒░░░▓──────\n────░░░░░░▒▒▓▓▓▓▓▓░░░░░░────\n───░░░░░░░░░░░░░░░░░░░░░░░░░░───\n──░░░░░░░░░░░░░░░░░░░░░░░░▒░▒░──\n─░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░─\n─░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒─\n─░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒─\n─░░░░░░░░░▒▒  END  ▒▒▒▒▒▒▒─\n─░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒─\n─░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒─\n──░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░─\n──░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒──\n───░░░░░░▒▒▒▒▒▒▒▒▒▒───\n────░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▒────')
