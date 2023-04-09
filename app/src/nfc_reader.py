import nfc

SVC_CODE = 0x1A8B  # サービスコード
SYS_CODE = 0xFE00  # システムコード


class Reader:
    def __init__(self):
        # 表示用
        self.on = False
        self.txt = ""

    def on_connect(self, tag):
        self.on = True
        idm, pmm = tag.polling(system_code=SYS_CODE)
        tag.idm, tag.pmm, tag.sys = idm, pmm, SYS_CODE
        if isinstance(tag, nfc.tag.tt3.Type3Tag):  # Type3Tagの場合
            try:
                # 学籍番号を読み取り，TXTに格納
                sc = nfc.tag.tt3.ServiceCode(SVC_CODE >> 6, SVC_CODE & 0x3F)
                bc_id = nfc.tag.tt3.BlockCode(0, service=0)  # 読取りブロック
                data = tag.read_without_encryption([sc], [bc_id])
                self.txt = data[2:10].decode("utf-8")
            except Exception as e:
                print(e)
            return True
        else:
            # スマホなどの場合
            print("error: tag isn't Type3Tag")
            self.records = tag.ndef.records
            self.txt = f"error: tag isn't Type3Tag\n code: {self.records[0].text}"
            return False

    def on_release(self, tag):
        self.on = False
        self.txt = "タッチしてください"
        return True

    def __call__(self):
        clf = nfc.ContactlessFrontend("usb")
        try:
            clf.connect(rdwr={"on-connect": self.on_connect, "on-release": self.on_release})
        finally:
            clf.close()

    def check_loop(self):
        while True:
            self.__call__()
