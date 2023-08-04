# Ref

[CircleCI 教程(Python 的 CircleCI 调度程序)](https://www.muyuanzhan.com/tutorials/python/2849.html)

[2022 CI/CD X Jenkins、CircleCI、Github Action 從把妹角度理解前後端如何和平相處](https://linyencheng.github.io/2022/10/10/relationships-between-frontend-and-backend/devops-ci-cd-jenkins-circleci-and-github-action/)

[CI/CD是什麼？一篇認識CI/CD工具及優勢，將日常瑣事自動化](https://www.wingwill.com.tw/zh-tw/%E9%83%A8%E8%90%BD%E6%A0%BC/%E9%9B%B2%E5%9C%B0%E6%B7%B7%E5%90%88%E6%87%89%E7%94%A8/cicd%E5%B7%A5%E5%85%B7/)

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

1. **開發**時會因為有時程壓力導致技術債的產生，此時從**維運**角度看，累積技術債，累積小 bug，不良的命名和無抽系的程式碼和測試方式，使得該程式碼後續難以維護，因此開發和維運常常吵架

## Pros of CI

1. 及早發現bug，避免問題隨著時間越滾越大 - 例如因應該bug，所做的patch，都是後續重構的成本，CICD 工具，每一位開發人員完成任務後，都必須被檢查是否符合標準，確認無誤才能 merge

2. 降低各項時間成本 - 由於每次發布都會檢查和驗證，一次要驗證的內容很少，此時 CICD 工具可以迅速檢查錯誤根源，以利開發人員修復，預防小錯變大錯

# Hello World CircleCI

repo : https://github.com/YLTsai0609/cicd

https://www.muyuanzhan.com/tutorials/python/2849.html

<img src='./assets/cicd_1.png'></img>

check document @ https://circleci.com/docs/language-python/

# FutherMore

[Concept](concept.md)