import pygame, sys, re#, Gameflow

#SETUP
Path = "src/assets/gui/"
MusicVolume = 0.5
SoundVolume = 0.8
LoggedInUsername = ''
LoggedIn = False

#ASSETS
FontPath = Path +"font.ttf"
Music = Path + "BackgroundMusic.mp3"
ButtonClickPath = Path + "ButtonClick.mp3"
PygameIcon = pygame.image.load(Path+"Icon.png")
BackgroundMenu = pygame.image.load(Path + "BackgroundMenu.png")
BackgroundLogin = pygame.image.load(Path + "BackgroundLogin.png")
BackgroundSignIn = pygame.image.load(Path + "BackgroundSignIn.png")
BackgroundLeaderboard = pygame.image.load(Path + "BackgroundLeaderboard.png")
BackgroundPlay = pygame.image.load(Path + "BackgroundPlay.png")
BackgroundTicTacToe = pygame.image.load(Path + "BackgroundTicTacToe.png")
BackgroundBauernschach = pygame.image.load(Path + "BackgroundBauernschach.png")
BackgroundDame = pygame.image.load(Path + "BackgroundDame.png")

#BUTTON BACKGROUND
ButtonBackgroundPlay = Path + "PlayButton.png"
ButtonBackgroundBack = Path + "BackButton.png"
ButtonBackgroundLogout = Path + "LogoutButton.png"
ButtonBackgroundMenu = Path + "MenuButton.png"

#COLORS
ButtonTextColorBlack = "#292929"
ButtonTextColorWhite = "#e5e5e5"
ButtonHoverColor = "#f1c232"

#GLOBAL VARIABLES
Window = pygame.display.set_mode((1280, 720))

#KLASSEN
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def Update(self, Window):
        if self.image is not None:
            Window.blit(self.image, self.rect)
            Window.blit(self.text, self.text_rect)

    def CheckForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def ChangeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

#NEBENFUNKTIONEN
def PlayMusic():
    PlayList = []
    PlayList.append(Music)
    pygame.mixer.music.load(PlayList[0])
    pygame.mixer.music.set_volume(MusicVolume)
    pygame.mixer.music.play()
    pygame.mixer.music.rewind()
    
def PlayClickSound():
    ClickSound = pygame.mixer.Sound(ButtonClickPath)
    ClickSound.set_volume(SoundVolume)
    ClickSound.play()

def GetFont(size): 
    return pygame.font.Font(FontPath, size)

#REGISTER/LOGIN
def IsUsernameUsed():
    print('TODO IsUsernameUsed')
    SqlQueryFindUsername = False
    return SqlQueryFindUsername

def GetUsername():
    print('TODO GetUsername')
    SqlQueryGetUsername = "Spielername"
    return SqlQueryGetUsername

#REGISTER
def RegisterUser(Username, Password):
    print('TODO RegisterUser')

def TryRegister(Username, Password):
    if not IsUsernameUsed:
        RegisterUser(Username, Password)
        TryLogin(Username, Password)
        return True
    else:
        return False

#LOGIN
def LoginUser(Username, Password):
    print('TODO LoginUser')
    SqlQueryTryLogin = False
    return SqlQueryTryLogin

def TryLogin(Username, Password):
    global LoggedIn, LoggedInUsername
    
    if IsUsernameUsed:
        LoggedInUsername = Username
        LoggedIn = True
        return True
    else:
        LoggedIn = False
        return False

#LEADERBOARD
def GetLeaderboard():
    #TODO Leaderboard (username, punkte) kriegen
    print('TODO GetLeaderboard')
    
def GetLeaderboardCount():
    #TODO Anzahl LeaderboardSpieler für For Schleife
    SqlQueryLeaderboardCount = 12
    return SqlQueryLeaderboardCount

def GetLeaderboardPoints():
    SqlQueryLeaderboardPoints = 12
    return SqlQueryLeaderboardPoints

def WriteToLeaderboard():
    #TODO Leaderboard reinschreiben (username, punkte)
    print('TODO WriteToLeaderboard')

#SONSTIGES
def HideWindow(Hide):
    if Hide:
        Window = pygame.display.set_mode((1280, 720), flags=pygame.HIDDEN)
    else:
        Window = pygame.display.set_mode((1280, 720), flags=pygame.SHOWN)

def RunGame(Game, Difficulty):
    global LoggedIn
    global LoggedInUsername
    Wins = 0
    #LeaderboardPoints = Difficulty
    #GameFlow = Gameflow.Spielesammlung(Game, Difficulty)
    #Wins = GameFlow.gameloop():
    #if LoggedIn:
        #WriteToLeaderboard(LoggedInUsername, LeaderboardPoints * Wins)
    HideWindow(False)

def StartBauernschach(Difficulty):
    RunGame("Bauernschach", Difficulty)
    
def StartDame(Difficulty):
    RunGame("Dame", Difficulty)
    
def StartTicTacToe(Difficulty):
    RunGame("TicTacToe", Difficulty)

#SEITEN
def OpenLeaderboard():
    global LoggedIn
    HasPrinted = False
    UsernameList = ['','','','','','','','','','','','']
    PointList = [0,0,0,0,0,0,0,0,0,0,0,0]
    while True:
        #REFRESH
        pygame.display.update()  
        MousePosition = pygame.mouse.get_pos()
        
        #BACKGROUND
        Window.blit(BackgroundLeaderboard, (0, 0))
        
        #TEXT
        LeaderboardTitle = GetFont(40).render("LEADERBOARD", True, "#7f6d13")
        LeaderboardRect = LeaderboardTitle.get_rect(center=(640, 52))
        Window.blit(LeaderboardTitle, LeaderboardRect)
        
        #BUTTONS
        BackButton = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 650), 
                            text_input="- BACK -", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
            
        for button in [BackButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)
            
        #LOGIK
        if not HasPrinted:
            GetLeaderboard()
            if GetLeaderboardCount() > 12:
                LeaderboardCount = 12
            else:
                LeaderboardCount = GetLeaderboardCount()
            for ControlVariable in range (LeaderboardCount):
                UsernameList[ControlVariable] = GetUsername()
                PointList[ControlVariable] = GetLeaderboardPoints()
                print(str(UsernameList[ControlVariable]))
            HasPrinted = True
        else:
            for ControlVariable in range (LeaderboardCount): 
                Position = str(ControlVariable + 1)+". "
                Height = 110 + ((ControlVariable + 1) * 40)
                PlayerEntree = Position + str(UsernameList[ControlVariable]) + " - " + str(PointList[ControlVariable]) + " Pts."
                LeaderboardTitle = GetFont(20).render(PlayerEntree, True, "#514504")
                LeaderboardRect = LeaderboardTitle.get_rect(center=(640, Height))
                Window.blit(LeaderboardTitle, LeaderboardRect)
                
        #EVENTS    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BackButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenMenu()
                if LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False       

def OpenSignIn():
    global LoggedIn
    UsernameInputText = ''
    PasswordInputText = ''
    HiddenPasswordInputText = ''
    WhiteSpaceText= '                       '
    ShowFailedLogin = False
    SelectedTextbox = 0
    UsernameTitleTextColor = ButtonTextColorWhite
    PasswordTitleTextColor = ButtonTextColorWhite
    while True:
        #REFRESH
        pygame.display.update()
        MousePosition = pygame.mouse.get_pos()
        
        #BACKGROUND
        Window.blit(BackgroundSignIn, (0, 0))
        
        #USERNAME TEXTBOX
        UsernameButton = Button(image=None, pos=(640, 130), 
                            text_input=WhiteSpaceText, font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        UsernameTextboxTitle = GetFont(20).render("USERNAME", True, UsernameTitleTextColor)
        UsernameTextboxTitleRect = UsernameTextboxTitle.get_rect(center=(640, 80))
        Window.blit(UsernameTextboxTitle, UsernameTextboxTitleRect)
        
        UsernameTextbox = GetFont(20).render(UsernameInputText, True, ButtonTextColorBlack)
        UsernameTextboxRect = UsernameTextbox.get_rect(center=(640, 130))
        Window.blit(UsernameTextbox, UsernameTextboxRect)
        
        #PASSWORD TEXTBOX
        PasswordButton = Button(image=None, pos=(640, 275), 
                            text_input=WhiteSpaceText, font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        PasswordTextboxTitle = GetFont(20).render("PASSWORD", True, PasswordTitleTextColor)
        PasswordTextboxTitleRect = PasswordTextboxTitle.get_rect(center=(640, 225))
        Window.blit(PasswordTextboxTitle, PasswordTextboxTitleRect)
        PasswordTextbox = GetFont(20).render(HiddenPasswordInputText, True, ButtonTextColorBlack)
        PasswordTextboxRect = PasswordTextbox.get_rect(center=(640, 275))
        Window.blit(PasswordTextbox, PasswordTextboxRect)

        #BUTTONS
        RegisterButton = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 380), 
                            text_input="REGISTER", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        BackButton = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 550), 
                            text_input="- BACK -", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
            
        if ShowFailedLogin:
            LoggedInBottomText = GetFont(10).render("Registration Failed!", True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 290))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
            
        for button in [UsernameButton, PasswordButton, RegisterButton, BackButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)
        
        #EVENTS
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if UsernameButton.CheckForInput(MousePosition):
                    SelectedTextbox = 1
                    UsernameTitleTextColor = ButtonTextColorBlack
                    PasswordTitleTextColor = ButtonTextColorWhite
                    PlayClickSound()
                    ShowFailedLogin = False
                
                elif PasswordButton.CheckForInput(MousePosition):
                    SelectedTextbox = 2
                    UsernameTitleTextColor = ButtonTextColorWhite
                    PasswordTitleTextColor = ButtonTextColorBlack
                    PlayClickSound()
                    ShowFailedLogin = False

                elif RegisterButton.CheckForInput(MousePosition):
                    PlayClickSound() #TODO
                    if len(UsernameInputText) < 6 or len(PasswordInputText) < 6:
                        ShowFailedLogin = True
                    elif TryRegister(UsernameInputText, PasswordInputText):
                        TryLogin(UsernameInputText, PasswordInputText)
                        OpenMenu()
                    else:
                        ShowFailedLogin = True
                    
                elif BackButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenMenu()
                    
                elif LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False
                
                else:
                    SelectedTextbox = 0
                    UsernameTitleTextColor = ButtonTextColorWhite
                    PasswordTitleTextColor = ButtonTextColorWhite
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    PlayClickSound() #TODO
                    if len(UsernameInputText) < 6 or len(PasswordInputText) < 6:
                        ShowFailedLogin = True
                    elif TryRegister(UsernameInputText, PasswordInputText):
                        TryLogin(UsernameInputText, PasswordInputText)
                        OpenMenu()
                    else:
                        ShowFailedLogin = True

                elif SelectedTextbox == 1 :
                        if event.key == pygame.K_BACKSPACE:
                            UsernameInputText = UsernameInputText[:-1]

                        elif event.key == pygame.K_SPACE:
                            UsernameInputText = UsernameInputText
                        
                        elif event.key == pygame.K_TAB:
                            PlayClickSound()
                            SelectedTextbox = 2
                            ShowFailedLogin = False
                            UsernameTitleTextColor = ButtonTextColorWhite
                            PasswordTitleTextColor = ButtonTextColorBlack
                        
                        elif len(UsernameInputText) <= 16:
                            UsernameInputText += event.unicode
                            
                        UsernameInputText = re.sub(r"[^a-zA-Z0-9 ]", "", UsernameInputText)

                elif SelectedTextbox == 2:
                        if event.key == pygame.K_BACKSPACE:
                            HiddenPasswordInputText = HiddenPasswordInputText[:-1]
                            PasswordInputText = PasswordInputText[:-1]

                        elif event.key == pygame.K_TAB:
                            PlayClickSound()
                            SelectedTextbox = 1
                            ShowFailedLogin = False
                            UsernameTitleTextColor = ButtonTextColorBlack
                            PasswordTitleTextColor = ButtonTextColorWhite

                        elif len(PasswordInputText) <= 16:
                            HiddenPasswordInputText += "*"
                            PasswordInputText += event.unicode
            
                else:
                    PlayClickSound()
                    SelectedTextbox = 1
                    ShowFailedLogin = False
                    UsernameTitleTextColor = ButtonTextColorBlack
                    PasswordTitleTextColor = ButtonTextColorWhite

 
def OpenLogin():
    global LoggedIn
    ShowFailedLogin = False
    UsernameInputText = ''
    PasswordInputText = ''
    HiddenPasswordInputText = ''
    WhiteSpaceText= '                       '
    SelectedTextbox = 0
    UsernameTitleTextColor = ButtonTextColorWhite
    PasswordTitleTextColor = ButtonTextColorWhite
    while True:
        #REFRESH
        pygame.display.update()  
        MousePosition = pygame.mouse.get_pos()
        
        #BACKGROUND
        Window.blit(BackgroundLogin, (0, 0))
        
        #TEXT
        if ShowFailedLogin:
            LoggedInBottomText = GetFont(10).render("Login Failed!", True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 290))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        
        #USERNAME TEXTBOX
        UsernameButton = Button(image=None, pos=(640, 130), 
                            text_input=WhiteSpaceText, font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        UsernameTextboxTitle = GetFont(20).render("USERNAME", True, UsernameTitleTextColor)
        UsernameTextboxTitleRect = UsernameTextboxTitle.get_rect(center=(640, 80))
        UsernameTextbox = GetFont(20).render(UsernameInputText, True, ButtonTextColorBlack)
        UsernameTextboxRect = UsernameTextbox.get_rect(center=(640, 130))
        Window.blit(UsernameTextboxTitle, UsernameTextboxTitleRect)
        Window.blit(UsernameTextbox, UsernameTextboxRect)
        
        #PASSWORD TEXTBOX
        PasswordButton = Button(image=None, pos=(640, 275), 
                            text_input=WhiteSpaceText, font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        PasswordTextboxTitle = GetFont(20).render("PASSWORD", True, PasswordTitleTextColor)
        PasswordTextboxTitleRect = PasswordTextboxTitle.get_rect(center=(640, 225))    
        PasswordTextbox = GetFont(20).render(HiddenPasswordInputText, True, ButtonTextColorBlack)
        PasswordTextboxRect = PasswordTextbox.get_rect(center=(640, 275))
        Window.blit(PasswordTextboxTitle, PasswordTextboxTitleRect)
        Window.blit(PasswordTextbox, PasswordTextboxRect)
        
        #BUTTONS
        LOG_IN_BUTTON = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 380), 
                            text_input="LOGIN", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        SIGN_IN_BUTTON = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 450), 
                            text_input="SIGN IN", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        BackButton = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 550), 
                            text_input="- BACK -", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        
        for button in [UsernameButton, PasswordButton, LOG_IN_BUTTON, SIGN_IN_BUTTON, BackButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)
        
        #EVENTS    
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if UsernameButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    SelectedTextbox = 1
                    ShowFailedLogin = False
                    UsernameTitleTextColor = ButtonTextColorBlack
                    PasswordTitleTextColor = ButtonTextColorWhite
                
                elif PasswordButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    SelectedTextbox = 2
                    ShowFailedLogin = False
                    UsernameTitleTextColor = ButtonTextColorWhite
                    PasswordTitleTextColor = ButtonTextColorBlack
                
                elif LOG_IN_BUTTON.CheckForInput(MousePosition):
                    PlayClickSound()
                    if len(UsernameInputText) < 6 or len(PasswordInputText) < 6:
                        ShowFailedLogin = True
                    elif not TryLogin(UsernameInputText, PasswordInputText):
                        ShowFailedLogin = True
                        LoggedIn = False
                    else:
                        LoggedIn = True
                        OpenMenu()

                elif SIGN_IN_BUTTON.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenSignIn()
                    
                elif BackButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenMenu()
                
                elif LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False
                
                else:
                    SelectedTextbox = 0
                    UsernameTitleTextColor = ButtonTextColorWhite
                    PasswordTitleTextColor = ButtonTextColorWhite      
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    PlayClickSound()
                    if len(UsernameInputText) < 6 or len(PasswordInputText) < 6:
                        ShowFailedLogin = True
                    elif not TryLogin(UsernameInputText, PasswordInputText):
                        ShowFailedLogin = True
                        LoggedIn = False
                    else:
                        LoggedIn = True
                        OpenMenu()

                elif SelectedTextbox == 1 :
                        if event.key == pygame.K_BACKSPACE:
                            UsernameInputText = UsernameInputText[:-1]

                        elif event.key == pygame.K_SPACE:
                            UsernameInputText = UsernameInputText
                        
                        elif event.key == pygame.K_TAB:
                            PlayClickSound()
                            SelectedTextbox = 2
                            ShowFailedLogin = False
                            UsernameTitleTextColor = ButtonTextColorWhite
                            PasswordTitleTextColor = ButtonTextColorBlack
                        
                        elif len(UsernameInputText) <= 16:
                            UsernameInputText += event.unicode
                            
                        UsernameInputText = re.sub(r"[^a-zA-Z0-9 ]", "", UsernameInputText)

                elif SelectedTextbox == 2:
                        if event.key == pygame.K_BACKSPACE:
                            HiddenPasswordInputText = HiddenPasswordInputText[:-1]
                            PasswordInputText = PasswordInputText[:-1]

                        elif event.key == pygame.K_TAB:
                            PlayClickSound()
                            SelectedTextbox = 1
                            ShowFailedLogin = False
                            UsernameTitleTextColor = ButtonTextColorBlack
                            PasswordTitleTextColor = ButtonTextColorWhite

                        elif len(PasswordInputText) <= 16:
                            HiddenPasswordInputText += "*"
                            PasswordInputText += event.unicode
            
                else:
                    PlayClickSound()
                    SelectedTextbox = 1
                    ShowFailedLogin = False
                    UsernameTitleTextColor = ButtonTextColorBlack
                    PasswordTitleTextColor = ButtonTextColorWhite


def OpenGame(game):
    global LoggedIn
    TextDifficulty = GetFont(20).render("Difficulty", True, "#f5fffa")
    RectDifficulty = TextDifficulty.get_rect(center=(1110, 80))
    Difficulty = 2
    ClickedButtonColor = ButtonTextColorBlack
    NotClickedButtonColor = ButtonTextColorWhite
    EasyButtonColor = NotClickedButtonColor
    NormalButtonColor = ClickedButtonColor
    HardButtonColor = NotClickedButtonColor

    while True:
        #REFRESH
        pygame.display.update()
        MousePosition = pygame.mouse.get_pos()
        
        #BACKGROUND
        if game == 1:
            Window.blit(BackgroundBauernschach, (0, 0))
        if game == 2:
            Window.blit(BackgroundTicTacToe, (0, 0))
        if game == 3:
            Window.blit(BackgroundDame, (0, 0))
        
        #TEXT
        Window.blit(TextDifficulty, RectDifficulty)
        
        #BUTTONS
        StartButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(680, 600), 
                            text_input="START GAME", font=GetFont(25), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
        
        EasyButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(1103, 200), 
                            text_input="EASY", font=GetFont(25), base_color=EasyButtonColor, hovering_color=ButtonHoverColor)
        
        NormalButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(1103, 320), 
                            text_input="NORMAL", font=GetFont(25), base_color=NormalButtonColor, hovering_color=ButtonHoverColor)
        
        HardButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(1103, 440), 
                            text_input="HARD", font=GetFont(25), base_color=HardButtonColor, hovering_color=ButtonHoverColor)
        
        BackButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(213, 600), 
                            text_input="- BACK -", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
            
        for button in [StartButton, EasyButton, NormalButton, HardButton, BackButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartButton.CheckForInput(MousePosition):
                    if game == 1:
                        StartBauernschach(Difficulty)
                    if game == 2:
                        StartTicTacToe(Difficulty)
                    if game == 3:
                        StartDame(Difficulty)
                    
                if EasyButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    Difficulty = 1
                    EasyButtonColor = ClickedButtonColor
                    NormalButtonColor = NotClickedButtonColor
                    HardButtonColor = NotClickedButtonColor
                
                if NormalButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    Difficulty = 2
                    EasyButtonColor = NotClickedButtonColor
                    NormalButtonColor = ClickedButtonColor
                    HardButtonColor = NotClickedButtonColor
                    
                if HardButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    Difficulty = 3
                    EasyButtonColor = NotClickedButtonColor
                    NormalButtonColor = NotClickedButtonColor
                    HardButtonColor = ClickedButtonColor
                    
                if BackButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenGameSelection()
                    
                if LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False
        
def OpenGameSelection():
    global LoggedIn
    while True:
        #REFRESH
        pygame.display.update()
        MousePosition = pygame.mouse.get_pos()
        
        #BACKGROUND
        Window.blit(BackgroundPlay, (0, 0))
        
        #BUTTONS
        GameBauerButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(248, 540), 
                            text_input="Bauernschach", font=GetFont(25), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
        
        GameTicTacToeButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(640, 540), 
                            text_input="Tic-Tac-Toe", font=GetFont(25), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
        
        GameDameButton = Button(image=pygame.image.load(ButtonBackgroundPlay), pos=(1030, 540), 
                            text_input="Dame", font=GetFont(30), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)

        BackButton = Button(image=pygame.image.load(ButtonBackgroundBack), pos=(640, 630), 
                            text_input="- BACK -", font=GetFont(25), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)

        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)

        for button in [GameBauerButton, GameTicTacToeButton, GameDameButton, BackButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GameBauerButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenGame(1)
                if GameTicTacToeButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenGame(2)
                if GameDameButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenGame(3)
                if BackButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenMenu()
                if LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False  
        
def OpenMenu():
    global LoggedIn
    while True:
        #REFRESH
        pygame.display.update()
        MousePosition = pygame.mouse.get_pos()  
        
        #BACKGROUND
        Window.blit(BackgroundMenu, (0, 0))
        
        #TEXT
        MenuTitleLeft = GetFont(100).render("SPI", True, "#292929")
        MenuTitleLeftRect = MenuTitleLeft.get_rect(center=(475, 80))
        Window.blit(MenuTitleLeft, MenuTitleLeftRect)
        
        MenuTitleRight = GetFont(100).render("ESA", True, "#ededed")
        MenuTitleRightRect = MenuTitleRight.get_rect(center=(820, 80))
        Window.blit(MenuTitleRight, MenuTitleRightRect)
        
        #BUTTONS
        PlayButton = Button(image=pygame.image.load(ButtonBackgroundMenu), pos=(640, 230), 
                            text_input="- PLAY -", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
        
        LoginButton = Button(image=pygame.image.load(ButtonBackgroundMenu), pos=(640, 340), 
                            text_input="LOGIN", font=GetFont(45), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        LeaderboardButton = Button(image=pygame.image.load(ButtonBackgroundMenu), pos=(640, 450), 
                            text_input="LEADERBOARD", font=GetFont(45), base_color=ButtonTextColorWhite, hovering_color=ButtonHoverColor)
        
        QuitButton = Button(image=pygame.image.load(ButtonBackgroundMenu), pos=(640, 560), 
                            text_input="- QUIT -", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
        
        if not LoggedIn:
            LogoutButton = Button(image=None, pos=(50, 50), 
                                text_input="", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "You are not logged in"
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        else:
            LogoutButton = Button(image=pygame.image.load(ButtonBackgroundLogout), pos=(1233, 670), 
                                text_input=" ", font=GetFont(45), base_color=ButtonTextColorBlack, hovering_color=ButtonHoverColor)
            LoggedInBottom = "Logged in as " + LoggedInUsername
            LoggedInBottomText = GetFont(15).render(LoggedInBottom, True, ButtonTextColorBlack)
            LoggedInBottomTextRect = LoggedInBottomText.get_rect(center=(640, 700))
            Window.blit(LoggedInBottomText, LoggedInBottomTextRect)
        
        for button in [PlayButton, LoginButton, LeaderboardButton, QuitButton, LogoutButton]:
            button.ChangeColor(MousePosition)
            button.Update(Window)
        
        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenGameSelection()
                if LoginButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenLogin()
                if LeaderboardButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    OpenLeaderboard()
                if LogoutButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    LoggedIn = False
                if QuitButton.CheckForInput(MousePosition):
                    PlayClickSound()
                    pygame.quit()
                    sys.exit()

def GuiMain():
    pygame.init()
    pygame.display.set_caption("SPIESA.exe")
    pygame.display.set_icon(PygameIcon)
    PlayMusic()
    OpenMenu()