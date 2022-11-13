import re

def convert(content):
    reheads = []
    alphaspace = re.compile(r"[\w /]+")
    alphanumeric = re.compile(r"[\w]+")
    alphalink = re.compile(r"[\w/]+")
    
    for i in range(7, 0, -1):
        reheads.append((re.compile(i*"#" + " \w+"), i))


    for rehead in reheads:
        print(rehead[1]+1)
        print(rehead)
        replacement = rehead[0].findall(content)
        print(replacement)
        for each in replacement:
            newheading = alphanumeric.findall(each)[0]
            newheading = "<h" + str(rehead[1]) + ">" + newheading + "</h" + str(rehead[1]) + ">"
            print(newheading)
            content = re.sub(each, newheading, content)
        


    rebold = re.compile(r"\*\*[\w\s]+\*\*")
    def bold(match):
        text = match.group()
        text = "<strong>" + alphaspace.findall(text)[0] + "</strong>"
        return text
    content = rebold.sub(bold, content)



    relink = re.compile(r"\[[\w ]+\]\([\w/]+\)")
    def link(match):
        text = match.group()
        linkIn = alphalink.findall(re.compile(r"\([\w/]+\)").findall(text)[0])[0]
        textIn = alphaspace.findall(re.compile(r"\[[\w ]+\]").findall(text)[0])[0]
        text = "<a href = '" + linkIn + "'>" + textIn + "</a>"
        return text
    content = relink.sub(link, content)


    return content
