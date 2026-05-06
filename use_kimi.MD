如何讓 graphify 在 Claude Code 中使用 Kimi

  第 1 步：安裝 Kimi 支援

  pip install 'graphify[kimi]'

  第 2 步：設置環境變數

  在你的系統環境中設置 Kimi API Key：

  # Linux/Mac
  export MOONSHOT_API_KEY=sk-xxxxxxxxxxxxx

  # Windows (PowerShell)
  $env:MOONSHOT_API_KEY="sk-xxxxxxxxxxxxx"

  # 或在 .env 檔案中
  MOONSHOT_API_KEY=sk-xxxxxxxxxxxxx

  第 3 步：在 Claude Code 中使用

  /graphify .

  系統會自動偵測：
  - 如果 MOONSHOT_API_KEY 已設置 → 使用 Kimi K2.6
  - 如果未設置 → 自動退回到 Claude API

  ---
  為什麼要用 Kimi？

  成本對比：
  ├─ Kimi K2.6：$0.74 輸入 + $4.66 輸出 per 1M tokens
  └─ Claude：  $3.0  輸入 + $15.0 輸出 per 1M tokens

  結果：Kimi 便宜 3 倍！

  ---
  強制指定後端

  如果同時設置了兩個 API Key，也可以明確指定：

  # 命令列中強制使用 Kimi
  graphify extract . --backend kimi

  # 強制使用 Claude
  graphify extract . --backend claude

  ---
  快速檢查

  你可以查看 .env 或環境變數是否已設置：

  # 檢查 Kimi key
  echo $MOONSHOT_API_KEY

  # 檢查 Claude key  
  echo $ANTHROPIC_API_KEY