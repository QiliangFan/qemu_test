import libvirt

def main():
    # 如果要在远程创建虚拟机, 记得保证远程用户具有相应权限
    # 如果要避免输入密码, 需要配置SSH免密
    con  = libvirt.open("qemu+ssh://fanqiliang@127.0.0.1/system")  

    # 操作远程与操作本地虚拟机没有什么不同

if __name__ == "__main__":
    main()