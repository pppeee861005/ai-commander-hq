# Graph Report - D:\數位資產\AI 指揮官總部  (2026-05-07)

## Corpus Check
- 74 files · ~123,627 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 16 nodes · 12 edges · 7 communities (4 shown, 3 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_核心戰略文檔|核心戰略文檔]]
- [[_COMMUNITY_寫作方法論|寫作方法論]]
- [[_COMMUNITY_發布管理系統|發布管理系統]]
- [[_COMMUNITY_世界觀與願景|世界觀與願景]]
- [[_COMMUNITY_Agent 架構|Agent 架構]]
- [[_COMMUNITY_工具與方案|工具與方案]]

## God Nodes (most connected - your core abstractions)
1. `新人類聯盟 (Homo Coalitio)` - 3 edges
2. `Facebook 引流成功案例分析` - 3 edges
3. `Software 3.0 的散戶基礎設施` - 3 edges
4. `Agentic 四柱` - 2 edges
5. `Graphify 知識圖譜工具` - 2 edges

## Surprising Connections (you probably didn't know these)
- `六層系統架構` --semantically_similar_to--> `Agentic 四柱`  [INFERRED] [semantically similar]
  agent.md → 🎯-戰略心法庫/Agentic_Writing_Guide.md
- `Facebook 引流成功案例分析` --analyzes_using--> `Graphify 知識圖譜工具`  [INFERRED]
  🎯-戰略心法庫/Facebook引流成功案例分析.md → 有興趣的主題/agentic_new_city_主體規劃.md
- `指揮官指令：graphify 授權` --authorizes--> `Graphify 知識圖譜工具`  [EXTRACTED]
  📝-工作日誌庫/2026.05.07-工作日誌.md → 有興趣的主題/agentic_new_city_主體規劃.md

## Hyperedges (group relationships)
- **新人類聯盟架構** — homo_coalitio, agentic_four_pillars, software_3_article, lobster_community [INFERRED 0.90]
- **Facebook 引流系統** — facebook_traffic_success_case, software_3_article, lobster_community, publication_tracker [EXTRACTED 0.95]

## Communities (7 total, 3 thin omitted)

### Community 0 - "核心戰略文檔"
Cohesion: 0.4
Nodes (5): 新人類聯盟 (Homo Coalitio), Agentic 四柱, 指揮官指令：術語調整 (超級個體→新人類聯盟), AION 世界觀, 六層系統架構

### Community 1 - "寫作方法論"
Cohesion: 0.67
Nodes (3): 龍蝦社團 (量化交易社群), Facebook 引流成功案例分析, Graphify 知識圖譜工具

### Community 2 - "發布管理系統"
Cohesion: 0.67
Nodes (3): 已發布文章完整目錄, Software 3.0 的散戶基礎設施, 文章發布追蹤系統

## Knowledge Gaps
- **7 isolated node(s):** `Agent 概念`, `Claude Code Agent 角色定位`, `六層系統架構`, `龍蝦社團 (量化交易社群)`, `文章發布追蹤系統` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `指揮官指令：graphify 授權` connect `Community 3` to `Community 1`?**
  _High betweenness centrality (0.343) - this node is a cross-community bridge._
- **Why does `Facebook 引流成功案例分析` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.333) - this node is a cross-community bridge._
- **Why does `Graphify 知識圖譜工具` connect `Community 1` to `Community 3`?**
  _High betweenness centrality (0.333) - this node is a cross-community bridge._
- **What connects `Agent 概念`, `Claude Code Agent 角色定位`, `六層系統架構` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._