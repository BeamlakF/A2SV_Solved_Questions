def removeComments(self, source):
        result = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            if not in_block:
                buffer = ""

            while i < len(line):
                # Start of block comment
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2

                # End of block comment
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2

                # Line comment
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                # Normal character
                elif not in_block:
                    buffer += line[i]
                    i += 1

                # Inside block comment
                else:
                    i += 1

            if not in_block and buffer:
                result.append(buffer)

        return result

# need to do this question again; 