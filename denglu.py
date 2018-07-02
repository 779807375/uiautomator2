# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport

class TestKTS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        hrp = htmlreport.HTMLReport(cls.u, 'report')
        hrp.patch_click()

        # cls.u.disable_popups(True)  # 允许自动处理弹出框
        cls.u.make_toast("测试开始", 3)

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service("uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.d = self.u.session("com.shijiabao.quickbook")  # restart app
        time.sleep(5)  # 等待首页广告结束

        #登录
        self.d(resourceId='com.shijiabao.quickbook:id/tv_mine').click()
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').click()
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').clear_text()
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').set_text('13631264416')
        self.d.press("back")
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_code').click()
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_code').clear_text()
        self.d(resourceId='com.shijiabao.quickbook:id/login_edt_code').set_text('123456')
        self.d.press("back")
        self.d(resourceId='com.shijiabao.quickbook:id/submit_lg').click()

    def tearDown(self):
        #pass

        #退出
        self.d(resourceId='com.shijiabao.quickbook:id/tv_mine').click()
        self.d.drag(0.5, 0.7, 0.5, 0.3)
        self.d(resourceId='com.shijiabao.quickbook:id/tv_dropout').click()
        self.d(resourceId='com.shijiabao.quickbook:id/confirm_bt').click()

    def test_shuku(self):  # 书库
        self.d(text="书库").click()
        self.d(resourceId='com.shijiabao.quickbook:id/tv_title').click()
        self.d(text="积分购书(599册)").click()

    def test_wode(self):  #

        self.d(resourceId='com.shijiabao.quickbook:id/tv_home').click()
        self.d(resourceId="com.shijiabao.quickbook:id/iv_more").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_bookName", text=u"生活").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_content", text=u"育儿百科").click()
        self.d(resourceId='com.shijiabao.quickbook:id/tv_home').click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_book_shelf").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_book_review").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_video").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_forum").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_chat_book").click()
        self.d(resourceId="com.shijiabao.quickbook:id/tv_circle").click()

        self.d(text="我的").click()


if __name__ == '__main__':
    unittest.main()

