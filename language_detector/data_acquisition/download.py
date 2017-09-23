import os
import yaml
import subprocess

def download(language, source, source_name, source_type):
    output_path = os.path.join(
        os.path.dirname(__file__),
        "../../data/raw/{0}/{1}".format(language, source_name))
    if os.path.exists(output_path):
        print "skipping {0} {1} because the target folder already exists".format(source_type, source_name)
    else:
        print "downloading {0} {1}".format(source_type, source_name)
        command = """
                youtube-dl -i --max-downloads 5 \
                --extract-audio --audio-format wav \
                "{0}" -o "{1}/%(title)s.%(ext)s"
            """.format(source, output_path)
        subprocess.call(command, shell=True)

def download_user(language, user):
    user_selector = "ytuser:%s" % user
    download(language, user_selector, user, "user")

def download_playlist(language, playlist_name, playlist_id):
    download(language, playlist_id, playlist_name, "playlist")

if __name__ == '__main__':
    source_file_path = os.path.join(os.path.dirname(__file__), "sources.yml")
    with open(source_file_path, "r") as f:
        sources = yaml.load(f)
    for language, categories in sources.items():
        for user in categories["users"]:
            download_user(language, user)
        for playlist_name, playlist_id in categories["playlists"].items():
            download_playlist(language, playlist_name, playlist_id)
