import libvirt

def main():
    con  = libvirt.open("qemu:///system")
    print(con.listAllDomains())

    # 创建虚拟机
    dom = con.createXML(open("tests/example.xml").read())

    # 获取所有虚拟机
    dom_list = con.listAllDomains()

    for _dom in dom_list:
        if _dom.name() == "kvm-1":  # 获取指定名字(名字在xml配置文件中配置)的虚拟机
            # 获取CPU信息 (也可以获取其他指标信息)
            print(_dom.getCPUStats(0))

            # 获取虚拟机之后, 摧毁指定名字虚拟机
            _dom.destroy()

    # 摧毁虚拟机, 如果有必要
    # dom.destroy()
    
 
if __name__ == "__main__":
    main()