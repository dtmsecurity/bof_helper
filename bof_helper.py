import glob
import sys
import requests

def find_declaration(method):
    results = []
    dork = " {}".format(method)
    for filename in glob.iglob('**/*.h', recursive=True):
        try:
            with open(filename,"r") as fh:
                 lines = fh.readlines()
                 for line in lines:
                     if dork in line and "WINAPI" in line:
                        results.append(line.strip())
        except:
            pass
    return results


def find_library(method):
        library = 0
        try:
            ms_uri="https://docs.microsoft.com/api/search?search={}&scope=Desktop&locale=en-us&scoringprofile=search_for_en_us_a_b_test&%24filter=scopes%2Fany(t%3A%20t%20eq%20%27Desktop%27)&facet=category&%24top=1".format(method)
            ms_search = requests.get(ms_uri)
            doc_uri = ms_search.json()["results"][0]["url"]
            doc_request = requests.get(doc_uri)
            doc_content = doc_request.text

            lines = doc_content.split("\n")
            i = 0
            for line in lines:
                    if "<td><strong>Library</strong></td>" in line:
                            lib_tmp = lines[i+1].replace("<td style=\"text-align: left;\">","").replace("</td>","")
                            if ".lib" in lib_tmp:
                                    library = lib_tmp.replace(".lib","")
                    i+=1
        except:
            pass
        return library


print("██████╗  ██████╗ ███████╗ ");
print("██╔══██╗██╔═══██╗██╔════╝ ");
print("██████╔╝██║   ██║█████╗   ");
print("██╔══██╗██║   ██║██╔══╝   ");
print("██████╔╝╚██████╔╝██║      ");
print("╚═════╝  ╚═════╝ ╚═╝      ");
print("BOF Helper by @dtmsecurity ");
print("")

if len(sys.argv) != 2:
    print("python3 {} <API Method>".format(sys.argv[0]))
    exit()

method = sys.argv[1]

library = find_library(method)

if library != 0:
        print("[Library] {} is probably in {}\n".format(method,library))

declarations = find_declaration(method)

for declaration in declarations:
    print("[Declaration] {}".format(declaration))

print("")

if library != 0:
        print("[BOF Helper]")
        for declaration in declarations:
            print("DECLSPEC_IMPORT {}".format(declaration.replace(method, "{}${}".format(library.upper(),method))))

