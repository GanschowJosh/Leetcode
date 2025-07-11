def simplifyPath(path: str) -> str:
        stack = []
        for direc in path.split("/"):
            direc = direc.strip("/")
            if not direc: #empty string
                continue
            if direc == "..": #go back directory
                if not stack: #curr directory path is empty:
                    return -1 #shouldn't reach
                else:
                    stack.pop(-1)
                    continue
            if direc == ".": #current directory:
                continue

            stack.append(direc)
        
        return "/".join(stack)

print(simplifyPath("/home/")) #/home