import sys

def num1():
    #import win64api
    print()
    print(sys.dllhandle)
    # print(win64api.GetModuleFileName(sys.dllhandle))

#num1()

def num2():
    print()
    print(sys.exec_prefix)
    print(sys.base_exec_prefix)

#num2()

def num3():
    print()
    print(sys.executable)

#num3()

def num4():
    print()
    print(sys.getfilesystemencoding())
    print()
    print(sys.getdefaultencoding())

#num4()

def num5():
    print()
    print(sys.getwindowsversion())
    print(sys.getwindowsversion().platform_version)

#num5()

def num6():
    print()
    print(sys.platform)
    print()
    print(sys.winver)

#num6()

def num7():
    print()
    print(sys.argv)
    print()
    print(sys.byteorder)
    print()
    print(sys.builtin_module_names)
    print()
    print(sys.modules)
    print()
    print(sys.copyright)

#num7()

def num8():
    print()
    print(sys.flags)
    print()
    print(sys.float_info)

#num8()

def num9():
    print()
    print(sys.exc_info())

#num9()

