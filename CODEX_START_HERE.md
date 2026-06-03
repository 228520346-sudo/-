# 给 Codex 的第一条指令

请先阅读 `AGENTS.md` 和 `docs/tasks/01_dxf_audit.md`，然后只完成任务01。

不要开发 GUI，不要一次性实现任务02~05。

完成后请确保：

```bash
pytest
python -m hvac_tool.cli audit samples/sample.dxf --out output
```

能够运行，并在 `output/` 生成：
- `dxf_audit.xlsx`
- `dxf_audit.json`
- `manual_review.xlsx`（如有无法识别项）
