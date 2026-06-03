"""DXF图层和实体快速体检脚本。
用法：python dxf_audit.py input.dxf layer_audit.csv
说明：不依赖ezdxf，直接按DXF group code粗解析，适合先判断图纸是否可自动化。
"""
import csv, sys
from collections import Counter

def iter_pairs(path, encoding="gbk"):
    with open(path, "r", encoding=encoding, errors="ignore") as f:
        while True:
            code = f.readline()
            if not code:
                break
            value = f.readline()
            if not value:
                break
            yield code.strip(), value.strip()

def audit(path):
    sec = None
    ent = None
    layer = None
    entity_counter = Counter()
    layer_counter = Counter()
    for code, value in iter_pairs(path):
        if code == "0" and value == "SECTION":
            sec = "pending"
            continue
        if sec == "pending" and code == "2":
            sec = value
            continue
        if code == "0" and value == "ENDSEC":
            sec = None
            continue
        if sec == "ENTITIES":
            if code == "0":
                if ent:
                    entity_counter[ent] += 1
                    if layer:
                        layer_counter[layer] += 1
                ent = value
                layer = None
            elif code == "8":
                layer = value
    return entity_counter, layer_counter

if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else "layer_audit.csv"
    ents, layers = audit(src)
    with open(dst, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["type", "name", "count"])
        for k, v in ents.most_common():
            w.writerow(["ENTITY", k, v])
        for k, v in layers.most_common():
            w.writerow(["LAYER", k, v])
    print(f"Wrote {dst}")
