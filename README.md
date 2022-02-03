# GenoMaker 家系圖產生器

**GenoMaker 是一個家系圖的繪製程式**

GenoMaker 是一個用 Python 編寫而成的家系圖繪製工具，透過 GenoMaker，使用者得以用簡單的「輸入」及「點選」來完成家系圖的繪製。

## GenoMaker 是什麼？
#### 何謂「家系圖」？
在介紹 GenoMaker 之前，我們首先必須知道家系圖（Genogram）是什麼。

家系圖是社會工作場域中常用的「視覺化評估工具」，其功能主要在於用簡單的「圖形」及「文字標示」呈現出個案的家庭關係。家系圖被廣泛的使用在個案紀錄中，藉以取代大量的文字敘述，讓家庭關係變得一目瞭然。

#### 家系圖之於實務工作
家系圖雖受到廣泛使用，但其繪製對社工而言卻是一大麻煩。在實務現場，為了快速紀錄個案的資訊，社工通常都會以手繪的方式繪製家系圖，而後再用電腦軟體（如：PowerPoint、小畫家等）進行重製，抑或是直接保留手稿。然而繪製家系圖不但費工費時，繪製方式更會因專業的使用習慣不同而略有差異，這將使得保存及易讀性都成為問題。

#### GenoMaker 的特色
為解決上述問題，設計一款繪製家系圖的程式便有其必要，而據我們所知，目前也確實存在一些繪製家系圖的程式。然而不同於其他程式的是，GenoMaker 是透過使用者輸入的資料自動繪製家系圖，而非讓使用者自行將圖案拼湊在一起。就我們的觀點，我們認為這樣的設計會對於使用者來說更為直觀。

## 安裝環境
GenoMaker 是由 Python 編寫而成，故須透過 Python file 來操作，且僅支援 Python3 以上的版本。此外，若要順利進行操作，則尚須下載以下套件：
- Graphviz
- Pygraphviz
- tkinter
- Pillow

由於以上四個套件的安裝方式在 MacOS 系統與 Windows 系統有著巨大的差別，因此以下分作兩部分個別陳述。

#### MacOS 系統
這邊建議依照 Pillow，tkinter，Graphviz，Pygraphviz 的順序安裝環境。

首先，安裝 Pillow 及 tkinter 的方式比較簡單，只要在終端機輸入 `pip3 install --upgrade Pillow` 及 `pip3 install tk` 即可安裝成功。

> 如遇到系統報錯的情況，可能是因為您的 Python 尚未更新至最新的版本。此時，您可以嘗試在終端機輸入 `pip3 install --upgrade pip` 更新後，再輸入上述兩條程式碼安裝套件。

成功安裝 Pillow 及 tkinter 後，則可開始安裝 Graphviz。安裝 Graphviz 的步驟如下：

Step1：下載 Homebrew

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Step2：輸入以下程式碼

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 2> /dev/null 

Step3：安裝 Graphviz

    brew install graphviz

如上述程式碼皆成功執行，則在終端機輸入 `pip3 install pygraphviz` 即可安裝 Pygraphviz。若成功安裝 Pygraphviz，則執行 GenoMaker 的環境即安裝完成。

#### Windows 系統
這邊建議依照 Pillow，tkinter，Graphviz，Pygraphviz 的順序安裝環境。

首先，輸入 `pip install Pillow` 及 `pip install tk` 安裝 Pillow 及 tkinter，安裝成功後即可開始安裝 Graphviz，步驟如下：

Step1：至 [Graphviz](https://graphviz.org/download/) 官網下載 Windows 版本的 Graphviz 執行檔。
Step2：在終端機輸入 `pip install graphviz`

如依照以上步驟成功安裝 Graphviz，則可進一步安裝 Pygraphviz。安裝 Pygraphviz 須符合以下三個條件，分別為：
- Python (version 3.7, 3.8, or 3.9)
- Graphviz (version 2.42 or later)
- C/C++ Compiler
（如您尚未安裝 C/C++ 編譯器，則建議依照 [Pygraphviz](https://pygraphviz.github.io/documentation/stable/install.html) 官網的指示安裝）

如符合以上條件，則可至終端機輸入：

    python -m pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz

接著在終端機輸入 `pip install pygraphviz`，Pygraphviz 即安裝成功。

## GenoMaker 使用說明
開啟程式後，可以看到在使用者介面中的最下方有五個選項，由左到右分別為Add Person(新增人物)、Delete Person(刪除人物)、Add Relation(新增關係)、Delete Relation(刪除關係)、Export Graph(輸出圖檔)，以下分別說明這些功能如何使用：

#### Add Person（新增人物）
點選Add Person後，會彈出一個視窗，視窗中有四個欄位可供使用者輸入人物資訊，分別為Name(人物姓名)、Sex(生理性別)、Birth(出生年)、Death(死亡年)。這邊需特別注意，若人物還未死亡，則在Death欄位點選”None”即可。輸入完成後點選Apply即可新增，若想取消輸入，則點選Cancel即可把Add Person視窗關閉。

#### Delete Person（刪除人物）
點選Delete Person後，會彈出一個視窗，視窗內只有一個欄位Name，供使用者選擇想要刪除的人物選項，選擇好想刪除的人物選項後，點選Apply即可刪除，若想取消刪除，則點選Cancel即可把Delete Person視窗關閉。

#### Add Relation（新增關係）
點選Add Relation後，會彈出一個視窗，在視窗中的第一個欄位Relation Type中，可供使用者選擇其想輸入的關係型態(ex. Couples(伴侶關係)、Child(親子關係)等等)。
選擇好想輸入的關係型態後，即可根據欄位中的稱謂輸入對應的人物(ex. Chris(male)與Ana(female)為伴侶關係，就在Husband的欄位選擇Chris；在Wife的欄位選擇Ana即可。最後點選最下方欄位的Apply即可新增關係，若想取消新增，則點選Cancel即可把Add Relation的視窗關閉。

#### Delete Relation（刪除關係）
點選Delete Relation後，會彈出一個視窗，在視窗中的第一個欄位Relation Type可供使用者選擇其想刪除的關係種類，選擇完成後即可根據下方欄位的稱謂選擇對應的人物，操作上如同Add Relation的功能。最後點選最下方欄位的Apply即可刪除關係，若想取消刪除，則點選Cancel即可把Delete Relation的視窗關閉。


#### Export Graph（輸出圖形）
點選Export Graph後，會彈出一個視窗，在視窗的第一個欄位Save As，可供使用者為畫出來的圖命名，輸入完名稱後，可在下一欄選出欲存入的位置，而最後一欄可選擇欲輸出的檔案形式（可選擇JPG或PNG）。最後點選Save即可輸出圖片，若想取消輸出，則點選Cancel即可將Export Graph的視窗關閉。

> 使用提醒：
1. 在使用此程式時，必須先把所有人物添加完成，再添加人物之間的關係型態。
2. 在添加關係型態時，若有伴侶關係則需優先建立，最後再建立親子的關係。

本文作者：Kuan, Shuan and Le
