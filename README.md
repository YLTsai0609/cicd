# Ref

[CircleCI 教程(Python 的 CircleCI 调度程序)](https://www.muyuanzhan.com/tutorials/python/2849.html)

[2022 CI/CD X Jenkins、CircleCI、Github Action 從把妹角度理解前後端如何和平相處](https://linyencheng.github.io/2022/10/10/relationships-between-frontend-and-backend/devops-ci-cd-jenkins-circleci-and-github-action/)

[CI/CD是什麼？一篇認識CI/CD工具及優勢，將日常瑣事自動化](https://www.wingwill.com.tw/zh-tw/%E9%83%A8%E8%90%BD%E6%A0%BC/%E9%9B%B2%E5%9C%B0%E6%B7%B7%E5%90%88%E6%87%89%E7%94%A8/cicd%E5%B7%A5%E5%85%B7/)

[全棧測試｜交付高品質軟體的實務指南](https://www.books.com.tw/products/0010961495)

# 什麼是 CI/CD (2022)

* 確保程式碼再提交之後，減少因為少部分檯面下的更動，而影響程式碼運作，確保程式碼的品質

* CI (Continuous Integration)
  * 自動化測試和自動化建置
  * e.g. 更動推送到 Git Repo 時， Linter 和測試就會運作
  * 可確保每次推送的版本都是可以運作的，否則就會擋下來
  * Code --> Build --> Test
CD (Continuous Delivery/Deployment)
  * 持續部署，通過自動化測試後，將變更後的程式碼，自動化佈署到對應的機器/叢集 (GCE, GKE, ...)
  * Test --> Release --> Deploy

* CI/CD 工具多元且通常自動化，常見的使用方法就是在專案中加入一個 yaml or README.md
* 安裝版 : DroneCI, Jenkins
* 第三方服務 : Travis CI, CircleCI
* 版控評台服務 : Github Action, Gitlab CI

## Why so serious

* **開發**時會因為有時程壓力導致技術債的產生，此時從**維運**角度看，累積技術債，累積小 bug，不良的命名和無抽象的程式碼和測試方式，使得該程式碼後續難以維護，因此開發和維運常常吵架

## Pros of CI

1. 及早發現bug，避免問題隨著時間越滾越大 - 例如因應該bug，所做的patch，都是後續重構的成本，CICD 工具，每一位開發人員完成任務後，都必須被檢查是否符合標準，確認無誤才能 merge

2. 降低各項時間成本 - 由於每次發布都會檢查和驗證，一次要驗證的內容很少，此時 CICD 工具可以迅速檢查錯誤根源，以利開發人員修復，預防小錯變大錯

3. 為交付做好準備 - 因為有持續的測試，因此我們的應用總是隨時準備好部署到任何地點

4. 強化協作 - 任何人都可以知道每個提交的品質狀況，避免無謂的甩鍋

5. 共同承擔責任 - 所有人都要對自己的提交負責，必此共同肩負產品品質的責任，而非開發老鳥或是測試者

# DevOps 的關鍵指標 - 透過 CI/CD/CT

* Google DevOps 研究與評估團隊設立的四大關檢指標
  * 交期 - 程式碼從提交到可以上生產環境的**時間** - 團隊在交付週期速度的指標
  * 部署頻率 - 軟體部署到生產環境的頻率，或者發佈到應用商店的**頻率** - 團隊在交付週期速度的指標
  * 平均回覆時間 - 恢復任何服務中斷或從故障中恢復的**時間** - 團隊交付週期的穩定性指標
  * 改版改壞比例 - 發佈到生產環境卻還需要修正的**版本比例**，包含回滾到前一版，熱修復(hot fix)，或者因此需要降載服務的比例 - 團隊交付週期的穩定性指標
* 以上是 Gooble DevOps 團隊提出能夠清楚定義一個軟體開發團隊在速度、反應性、品質、穩定性方面的能力

e.g.

|指標|達成條件|
|----|------|
|部署頻率|根據需求 - 一天能做到幾次部署?|
|交期|低於一天|
|平均恢復時間|低於一小時|
|改版改壞比例|0-15%|

* 該團隊的研究表示，以上指標良好的軟體開發團隊能夠帶公司走向成功，這意味著實際的股價、收益、使用者留存率等指標的相關成長



# Hello World CircleCI

repo : https://github.com/YLTsai0609/cicd

https://www.muyuanzhan.com/tutorials/python/2849.html

check document @ https://circleci.com/docs/language-python/

# FutherMore

[Concept](concept.md)

[circleci101](ci101.md)

[Automatic Testing](at.md)