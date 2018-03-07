class Settings():
    """存储外星人入侵的所有设置类"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        # 设置颜色:浅灰色，每个值都是在0~255
        self.bg_color = (230,230,230)
        #飞船设置

        self.ship_limit = 2

        #子弹设置

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #外星人设置

        self.fleet_drop_speed = 10


        #以什么样的速度加速游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而发生的变化"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        #计分
        self.alien_point = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)