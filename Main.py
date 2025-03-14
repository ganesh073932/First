from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from moviepy.editor import *
import os

# Your Telegram Bot Token
TOKEN = '8052511893:AAEtpFPK2IuO0c_hcl59hpLwWciejHVCtLw'

def start(update, context):
    update.message.reply_text("Send your video for Auto Editing! 🎬")

def handle_video(update, context):
    video = update.message.video
    file = context.bot.get_file(video.file_id)
    file.download('input.mp4')

    # 🎯 Auto Shake Effect + Velocity Sync
    clip = VideoFileClip('input.mp4').fx(vfx.speedx, 1.5)  # Velocity
    edited_clip = clip.fx(vfx.lum_contrast, 1.2, 50)  # Shake Effect
    edited_clip.write_videofile("output.mp4")

    update.message.reply_video(video=open('output.mp4', 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video, handle_video))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
