def clean_tags(raw: str)-> list[str]:
    return [t.strip().lower() for t in raw.split(",") if t.strip()!=""]

def add_tag(tag: str, tags: list[str] | None = None)-> list[str]:
    if tags == None:
        tags = []
        tags.append(tag)
    return tags