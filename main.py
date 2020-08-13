import os
import instaloader

def profilePic(username):
    parser = instaloader.Instaloader()

    os.chdir(os.path.join(os.path.expanduser('~'), 'Downloads'))

    if os.path.isdir('Insta pics'):
        os.chdir('Insta pics')

        return parser.download_profile(username, profile_pic_only=True)
    else:
        os.mkdir('Insta pics')
        os.chdir('Insta pics')
        return parser.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    user = input('Enter Insta account name : ')
    profilePic(user)
