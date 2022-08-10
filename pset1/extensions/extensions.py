types = {
    "aac":"audio/aac",
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}
file = input("File name: ").rstrip().split(".")[-1].lower()
type = types.get(file,"application/octet-stream")
print(type)