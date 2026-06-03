"""风机编号和风量候选识别脚本。
用法：python fan_detector.py input.dxf fans.csv
输出：layer,text,x,y,type
"""
import csv, re, sys
FAN_ID = re.compile(r"\b[A-Z]{2,4}-[A-Z]-B\d+-\d+\b|\b[A-Z]{2,4}-B\d+-\d+\b")
AIRFLOW = re.compile(r"(\d{3,6})\s*(CMH|m3/h|m³/h)", re.I)

def iter_pairs(path, encoding="gbk"):
    with open(path, "r", encoding=encoding, errors="ignore") as f:
        while True:
            c=f.readline(); v=f.readline()
            if not c or not v: break
            yield c.strip(), v.strip()

def collect_texts(path):
    sec=None; ent=None; cur={}; texts=[]
    for code,value in iter_pairs(path):
        if code=="0" and value=="SECTION": sec="pending"; continue
        if sec=="pending" and code=="2": sec=value; continue
        if code=="0" and value=="ENDSEC": sec=None; continue
        if sec=="ENTITIES":
            if code=="0":
                if ent in ("TEXT","MTEXT") and cur.get("text"):
                    texts.append(cur)
                ent=value; cur={}
            elif ent in ("TEXT","MTEXT"):
                if code=="8": cur["layer"]=value
                elif code in ("1","3"): cur["text"]=(cur.get("text","")+value)
                elif code=="10": cur["x"]=value
                elif code=="20": cur["y"]=value
    return texts

if __name__ == "__main__":
    src=sys.argv[1]
    dst=sys.argv[2] if len(sys.argv)>2 else "fans.csv"
    rows=[]
    for t in collect_texts(src):
        text=t.get("text","")
        typ=None
        if FAN_ID.search(text): typ="fan_id"
        elif AIRFLOW.search(text): typ="airflow"
        elif "FAN" in t.get("layer","").upper(): typ="fan_related_text"
        if typ:
            rows.append([t.get("layer",""), text, t.get("x",""), t.get("y",""), typ])
    with open(dst,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(["layer","text","x","y","type"]); w.writerows(rows)
    print(f"Wrote {dst}: {len(rows)} rows")
