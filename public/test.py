

def content(x):
    return f"""
---
title: "Il mio {x} post"
date: 2023-10-27T10:00:00+02:00
tags: ["Hugo", "Go", "Web Development"]
---

    Tempor proident minim aliquip reprehenderit dolor et ad anim Lorem duis sint eiusmod. Labore ut ea duis dolor. Incididunt consectetur proident qui occaecat incididunt do nisi Lorem. Tempor do laborum elit laboris excepteur eiusmod do. Eiusmod nisi excepteur ut amet pariatur adipisicing Lorem.

    Occaecat nulla excepteur dolore excepteur duis eiusmod ullamco officia anim in voluptate ea occaecat officia. Cillum sint esse velit ea officia minim fugiat. Elit ea esse id aliquip pariatur cupidatat id duis minim incididunt ea ea. Anim ut duis sunt nisi. Culpa cillum sit voluptate voluptate eiusmod dolor. Enim nisi Lorem ipsum irure est excepteur voluptate eu in enim nisi. Nostrud ipsum Lorem anim sint labore consequat do.


    """

for x in range(100):
    with open(f"./posts/{x}_post.md", "w") as f:
        f.write(content(x))
