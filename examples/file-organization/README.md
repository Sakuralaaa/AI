# 文件整理示例

[English](README.en.md)

本案例只演示“先生成映射，再执行”的方法。`manifest-before.csv`描述一个虚构目录，`rename-plan.csv`是人工检查前的计划。

练习：

1. 让Agent读取清单，不接触真实文件。
2. 检查同名冲突、无法识别项和可能重复项。
3. 修改计划，使所有 `REVIEW` 都有人工作出决定。
4. 在自己的临时副本目录中生成全新的计划，不要直接执行示例路径。
5. 真正执行后生成 `rollback.csv`，其中source和target与执行后的恢复方向相反。
