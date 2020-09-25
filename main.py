#import json
import falcon
import ffmpeg_streaming
#from ffmpeg_streaming import Bitrate, Size, Representation
from ffmpeg_streaming import Formats
from waitress import serve

class myclass(object):
    #GET Method
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        video = ffmpeg_streaming.input("http://demo.unified-streaming.com//video//tears-of-steel//tears-of-steel.ism//.m3u8")

        hls = video.hls(Formats.h264())
        hls.auto_generate_representations()
        hls.output("D:\\docker-first-build\\media\\abc%06d.png")

    #POST METHOD
    # def on_post(self,req,resp):
    #     resp.status = falcon.HTTP_200
    #     xyz = req.stream.read().decode("utf-8")
    #     raw = json.loads(xyz)
    #     print(raw)
    #     link = raw["url"]
    #     resp.body = link
    #     out = ffmpeg_streaming.input(link)
    #
    #     _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    #     _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    #     _720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))


        # hls = out.hls(Formats.h264())
        # hls.representations(_360p,_480p,_720p)
        # hls.output("D:\\work\\falcon\\data\\abc%06d.png")


app = falcon.API()
abc = myclass()
app.add_route('/',abc)
serve(app, listen='*:8080')