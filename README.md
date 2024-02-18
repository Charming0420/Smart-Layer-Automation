# Smart-Layer-Automation

### 事前準備

1. 準備兩隻帳號
2. 各買 N 隻貓（兩隻帳號數量可以不一樣多）
3. 開始腳本嚕貓

---

### 腳本運行

1. 將相應資料填入 config.py，A 帳號放 A 的部分，B 帳號放 B 的部分
2. 請申請 Infura 的私人節點 RPC 來跑，公用節點也可以，自己決定
3. 貓的 ID 請以陣列方式填進去，如 [353512249,673400642]...
4. 缺什麼套件裝什麼套件，詳情自行 Google pip or pip3 install
5. 裝完套件後直接開跑，等級上限其實超級遠，無腦放著跑就行
6. 建議 SmartLayer_A 跑一陣子換 B 依此類推
7. inviteCat 可以累積可能十分鐘再去跑 acceptInvite 接受約會

```
python3 Smartlayer_A.py
```
```
python3 Smartlayer_B.py
```
```
python3 inviteCat.py
```
```
python3 acceptInvite.py
```

---

### 解釋

- Smartlayer_A.py : A 帳號的貓咪 Feed、Clean、LevelUp 動作
- Smartlayer_B.py : B 帳號的貓咪 Feed、Clean、LevelUp 動作
- inviteCat.py : A 帳號的貓咪邀請 B 帳號的貓咪約會
- acceptInvite.py : B 帳號的貓咪接受 A 帳號的貓咪約會

---

### 備註

1. 由於是兩隻帳戶一直互邀和接受，有被女巫的風險，自行注意
2. 雖然交互過程都有加入隨機數的延遲，但或許還是會被抓到一致的腳本動作
3. 如果擔心 Gas 或連續失敗 Bug 等等，可以上 Scan 看一下記錄
4. 本人坦蕩蕩程式絕對僅本地執行，開源保證不上傳私鑰，不放心請用小錢包
5. 時間稀少，沒有過度優化程式，一定可以寫得更好，希望各位見諒
6. 程式還是會遇到 Gas 臨時拉不夠而終止的狀況，重新啟動程式即可

- https://polygonscan.com/
