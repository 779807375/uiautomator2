import uiautomator2 as u2
import time


def main():

    '''cmd初始化手机  
        python -m uiautomator2 init
        ui元素查看
        python -m weditor
        '''
    '''连接手机'''
    d=u2.connect('192.168.1.125')

    '''打印信息'''
    print(d.info)

    '''点亮屏幕'''
    d.screen_on()
    d.unlock()
    d.press("home")

    '''启动应用'''
    d.app_start('com.shijiabao.quickbook')
    time.sleep(8)

    '''操作步骤'''
    #d(text="书库").click()
    d(resourceId='com.shijiabao.quickbook:id/tv_home').click()
    time.sleep(3)

    d(resourceId='com.shijiabao.quickbook:id/tv_self').click()
    time.sleep(3)

    d(resourceId='com.shijiabao.quickbook:id/tv_forum').click()
    time.sleep(3)

    d(resourceId='com.shijiabao.quickbook:id/tv_mine').click()
    time.sleep(3)

    '''登录'''
    d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').click()
    d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').clear_text()
    d(resourceId='com.shijiabao.quickbook:id/login_edt_phone').set_text('13631264416')
    d.press("back")
    d(resourceId='com.shijiabao.quickbook:id/login_edt_code').click()
    d(resourceId='com.shijiabao.quickbook:id/login_edt_code').clear_text()
    d(resourceId='com.shijiabao.quickbook:id/login_edt_code').set_text('123456')
    d.press("back")
    d(resourceId='com.shijiabao.quickbook:id/submit_lg').click()

    '''退出'''
    d(resourceId='com.shijiabao.quickbook:id/tv_mine').click()
    d.drag(0.5, 0.7, 0.5, 0.3)
    #if d(resourceId='com.shijiabao.quickbook:id/tv_dropout').exists:
    d(resourceId='com.shijiabao.quickbook:id/tv_dropout').click()
    d(resourceId='com.shijiabao.quickbook:id/confirm_bt').click()

    time.sleep(3)

    '''关闭应用'''
    d.app_stop('com.shijiabao.quickbook')
    time.sleep(2)
    d.screen_off()

if __name__ == '__main__':
    main()



