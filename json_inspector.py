import argparse,json
from pathlib import Path
def summarize(value):
 if isinstance(value,dict):return {"type":"object","count":len(value),"keys":list(value)[:100]}
 if isinstance(value,list):return {"type":"array","count":len(value),"first_type":type(value[0]).__name__ if value else None}
 return {"type":type(value).__name__}
def main():
 a=argparse.ArgumentParser();a.add_argument("file",type=Path);x=a.parse_args()
 value=json.loads(x.file.read_text(encoding="utf-8"));print(json.dumps(summarize(value),indent=2,ensure_ascii=False))
if __name__=="__main__":main()
