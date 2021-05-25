#!/bin/bash


# 사용 방법
#
# 1. csinit.sh 파일을 최상위 폴더(guest-어쩌구저쩌구)에 놓는다.
# 2. Ctrl+` 를 눌러 터미널을 열고, 터미널에 bash csinit.sh 을 친다.
# 3. y 를 입력한다.


while [ true ]; do

    echo "Install Dotnet? (Y/N)"
        read yorn

    if [ ${yorn} = "y" ] || [ ${yorn} = "Y" ] ; then

        # dotnet 명령어가 이미 있을 경우 중단한다.
        if command -v dotnet &> /dev/null ; then
            echo "Dotnet has already installed."
            break
        fi

        # https://dot.net/v1/dotnet-install.sh 에서 닷넷 설치 스크립트를 받는다.
        wget https://dot.net/v1/dotnet-install.sh
        bash dotnet-install.sh -c Current

        # export PATH="$PATH:$HOME/.dotnet"
        # 환경변수 영구적 추가
        echo -e "export PATH=\"$PATH:$HOME/.dotnet\"" >> ~/.bashrc
        # source ~/.bashrc

        # VSCode CSharp extension 설치
        code --install-extension ms-dotnettools.csharp

        break
    elif [ ${yorn} = "n" ] || [ ${yorn} = "N" ]; then
        echo "Goodbye"
        break
    fi

done

bash
exit 0


# 참고문헌
#
# 전체적인 것들 https://docs.microsoft.com/ko-kr/dotnet/core/install/linux-scripted-manual
# 환경변수 영구적 추가 https://trend21c.tistory.com/1450
# 간단한 bash https://wiseworld.tistory.com/51
# bash shell script 작성 https://blog.naver.com/PostView.nhn?blogId=lunarispars&logNo=221491991449
# if문 https://hand-over.tistory.com/32
