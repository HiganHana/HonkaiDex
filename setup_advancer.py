
if __name__ == '__main__':
    # edit setup.py
    with open("setup.py", "r") as f:
        lines = f.readlines()

    version = lines[0].split("=")[1].strip()
    version_split = version.rsplit(".", 1)
    minor_version = int(version_split[-1].replace("'", ""))
    minor_version += 1
    version_split[-1] = str(minor_version)
    version = ".".join(version_split)

    with open("setup.py", "w") as f:
        lines[0] = f"VERSION = {version}'\n"
        f.writelines(lines)