import pygame.font  # 导入pygame.font模块,它让python能够将文本渲染到屏幕上.


class Button():
    """初始化按钮的属性"""

    def __init__(self, ai_settings, screen, msg):  # msg参数是要在按钮中显示的文本
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 按钮为亮绿色
        self.text_color = (255, 255, 255)  # 文本为白色
        self.font = pygame.font.SysFont(None, 48)  # 实参Nnone让Pygame使用默认字体,48为文本字号

        # 创建按钮的rect对象,并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像, 并使其在按钮上居中"""
        # 调用font.render()将存储在msg中的文本转换为图像
        # 该方法中接收一个布尔实参True,指定开启还是关闭反锯齿功能(反锯齿让文本的边缘更平滑)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮, 再绘制文本
        # 调用screen.fill()方法来绘制表示按钮的图形
        self.screen.fill(self.button_color, self.rect)
        # 再调用screen.blit()方法,并向它传递一幅图像以及与该图像相关联的rect对象,从而在屏幕上绘制文本图像
        self.screen.blit(self.msg_image, self.msg_image_rect)
