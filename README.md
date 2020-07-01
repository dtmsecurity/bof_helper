# Beacon Object File (BOF) Creation Helper

Cobalt Strike has now introduced the concept of Beacon Object File (BOF) as a way to rapidly extend its Beacon agent. This involves making and compiling a C program. These programs are much like normal C programs but with a few tweaks to make it work with Beacon as described in this video: [https://youtu.be/gfYswA_Ronw](https://youtu.be/gfYswA_Ronw).

I knocked together this script to make the process of making BOFs slightly easier. It tries automatically do what is described in the above video, by identifying which library in which the method exists via Microsoft's [docs.microsoft.com](http://docs.microsoft.com) endpoint. It also essentially greps the mingw header files for a declaration.

Note: The Microsoft endpoint and dorks used are liable to change which may break this script. Also ensure that the full and method name is supplied for best results.

**Dependencies**

Use *install.sh* to check and sort this but all that is required is the following:

- python3
- requests python library
- git clone [https://git.code.sf.net/p/mingw/mingw-org-wsl](https://git.code.sf.net/p/mingw/mingw-org-wsl) mingw-mingw-org-wsl to current directory.

**Usage**

python3 bof_helper.py <API Method>

**Example**

```bash
python3 bof_helper.py DsGetDcNameA
██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║█████╗
██╔══██╗██║   ██║██╔══╝
██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝ ╚═╝
BOF Helper by @dtmsecurity

[Library] DsGetDcNameA is probably in NetApi32

[Declaration] DWORD WINAPI DsGetDcNameA(LPCSTR, LPCSTR, GUID*, LPCSTR, ULONG, PDOMAIN_CONTROLLER_INFOA*);

[BOF Helper]
DECLSPEC_IMPORT DWORD WINAPI NETAPI32$DsGetDcNameA(LPCSTR, LPCSTR, GUID*, LPCSTR, ULONG, PDOMAIN_CONTROLLER_INFOA*);
```

**References**

- [https://www.cobaltstrike.com/help-beacon-object-files](https://www.cobaltstrike.com/help-beacon-object-files)
- [https://youtu.be/gfYswA_Ronw](https://youtu.be/gfYswA_Ronw).

**Author**

[@dtmsecurity](https://twitter.com/dtmsecurity)
