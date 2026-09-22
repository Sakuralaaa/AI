<!-- lang: zh-CN | status: source | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 08｜完整案例库：把方法跑一遍

[English](../en/08-case-studies.md) · [返回首页](../../README.md)

## 先记住一句话

案例的价值不在于复制最终文件，而在于看见每一次输入、转换、检查和人工决定。

## 案例A：资料到汇报

目标是把一组公开材料变成可核查的汇报包：

```text
材料清单
→ 带来源的主题摘要
→ 报告初稿
→ CSV行动表
→ 12至15页PPT故事线
→ 事实与视觉检查
```

关键做法：原文与摘要分离；每条结论保留来源；报告确认后再做PPT；PPT中的数字回到CSV或原文核对。共享说明见 [office-workflow](../../examples/office-workflow/README.md)。

推荐任务开头：

```text
先盘点input，不写报告。输出材料清单、可引用范围、缺失信息和处理计划。
所有事实必须标注来源文件；你的推断必须单独标记。
```

## 案例B：Stata-MCP

Stata在这里展示“MCP如何连接专业软件”，不是整套教程的主线。示例使用合成面板数据，不包含真实个人信息。

1. 准备有效的Stata安装和许可证。
2. 按 [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata) 当前文档安装并注册到Codex。
3. 重启客户端，用项目提供的测试方法确认连接。
4. 将 [synthetic_panel.csv](../../examples/stata-mcp/synthetic_panel.csv) 导入Stata。
5. 让Agent先审计变量、缺失值、唯一键和描述统计。
6. 运行共享的 [analysis.do](../../examples/stata-mcp/analysis.do)，保存log、表格和图形到独立输出目录。
7. 对照[核验清单](../../examples/stata-mcp/verification.md)检查样本量、模型设定、系数和标准误。
8. 只有核验后，才让Agent撰写结果摘要或PPT故事线。

不要把统计显著自动翻译成因果关系，也不要让Agent为获得显著结果不断更换样本和模型。相同方法可以迁移到R、Python或SPSS：换掉专业工具连接，保留数据审计、可重复脚本和人工复核。

## 案例C：批量文件整理

共享目录提供 [manifest-before.csv](../../examples/file-organization/manifest-before.csv) 和预期的 [rename-plan.csv](../../examples/file-organization/rename-plan.csv)。练习分三轮：

1. 只生成计划，不改文件。
2. 检查同名、无法识别和需要人工决定的记录。
3. 在副本中执行并生成 `rollback.csv`。

真正的批量操作必须使用自己的实际文件清单重新生成映射，不能把示例路径直接套用。

## 我踩过的坑

- 只保存最终PPT，无法追踪某个数字来自哪里。
- Stata命令跑通就接受解释，没有看log和样本量。
- 把合成数据案例的结论当成真实研究发现。
- 批量改名计划里存在同名冲突，却仍然直接执行。

## 正常结果与验收

- [ ] 每个案例有输入、计划、中间产物、输出和核验。
- [ ] 办公案例中的结论可以回到原始材料。
- [ ] Stata案例保存可重复脚本与log，统计解释经过人工检查。
- [ ] 文件案例在副本中运行并有恢复映射。
- [ ] 案例不包含真实凭证或敏感数据。

## 来源与核验

- [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata)
- 本仓库 `examples/` 中的合成与示范材料
- 最后核验：2026-09-22

[上一章](07-upgrades-and-tools.md) · [下一章：安全驾驶](09-safety-and-ethics.md)
