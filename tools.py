import json

while True:
    app_name = input("资源名称(例: 澎湃哔哩): ")
    if app_name != "":
        break
    else:
        print("资源名称不能未空!")

app_description = input("资源描述(例: 为Xiaomi Vela穿戴设备打造的第三方哔哩哔哩客户端): ")

preview = []

while True:
    preview_path = input("预览图文件名(可输入多次 输入end结束输入 例: preview.png): ")
    if preview_path == "end":
        break

    if preview_path != "":
        preview.append(preview_path)

while True:
    icon_path = input("资源图标文件名(例: icon.png): ")
    if icon_path != "":
        break
    else:
        print("资源图标文件名不能为空!")

repo_path = input("github链接(例: https://github.com/Searchstars/Hyperbilibili): ")

author = []

while True:

    author_info = {}

    author_name = input("作者(可输入多次 输入end结束输入 例: Searchstars): ")

    if author_name == "end":
        break

    author_url = input("作者主页(可输入多次 输入end结束输入 例: https://github.com/Searchstars): ")

    if author_url == "end":
        break

    if author_name != "":
        author_info["name"] = author_name
        author_info["author_url"] = author_url
        author.append(author_info)

downloads = {}

while True:
    download_info = {}

    device = input("支持的设备(可输入多次 输入end结束输入 例: o66): ")

    if device == "end":
        if len(downloads) == 0:
            print("请至少提供一个设备的下载信息!")
            continue
        else:
            break

    device_version = input("当前设备资源版本(可输入多次 输入end结束输入 例: 1.0): ")

    if device_version == "end":
        if len(downloads) == 0:
            print("请至少提供一个设备的下载信息!")
            continue
        else:
            break
    
    device_file = input("当前设备资源文件名(可输入多次 输入end结束输入 例: o66.rpk): ")

    if device_file == "end":
        if len(downloads) == 0:
            print("请至少提供一个设备的下载信息!")
            continue
        else:
            break

    if device_version != "" and device_file != "" and device != "":
        download_info["version"] = device_version
        download_info["file_name"] = device_file
        downloads[device] = download_info


manifest = {}
manifest["item"] = {}
manifest["item"]["name"] = app_name
manifest["item"]["description"] = app_description
manifest["item"]["preview"] = preview
manifest["item"]["icon"] = icon_path
manifest["item"]["source_url"] = repo_path
manifest["item"]["author"] = author
manifest["downloads"] = downloads

json_string = json.dumps(manifest, ensure_ascii=False, indent=4)

open("manifest.json", "w", encoding="utf8").write(json_string)

print("已成功生成manifest.json")