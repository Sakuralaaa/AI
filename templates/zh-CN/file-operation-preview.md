# 文件操作预演

## 范围

- 根目录：
- 允许读取：
- 允许写入：
- 禁止访问：

## 规则

- 命名格式：
- 分类规则：
- 重复文件处理：标记 `REVIEW`，默认不删除。
- 同名冲突处理：停止并报告，默认不覆盖。

## 执行前交付

生成 `operation-plan.csv`，字段至少包括：

```text
action,source,target,reason,status,rollback
```

第一轮只生成计划，不执行。人工确认后在副本上试运行；完成后生成 `rollback.csv` 和失败清单。
