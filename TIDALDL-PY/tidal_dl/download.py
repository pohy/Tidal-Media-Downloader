#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   download.py
@Time    :   2020/11/08
@Author  :   Yaronzz
@Version :   1.0
@Contact :   yaronhuang@foxmail.com
@Desc    :
'''

from concurrent.futures import ThreadPoolExecutor

from decryption import *
from printf import *
from tidal import *
from mutagen import flac


def __isSkip__(finalpath, url):
    if not SETTINGS.checkExist:
        return False
    curSize = aigpy.file.getSize(finalpath)
    if curSize <= 0:
        return False
    netSize = aigpy.net.getSize(url)
    return curSize >= netSize


def __encrypted__(stream, srcPath, descPath):
    if aigpy.string.isNull(stream.encryptionKey):
        os.replace(srcPath, descPath)
    else:
        key, nonce = decrypt_security_token(stream.encryptionKey)
        decrypt_file(srcPath, descPath, key, nonce)
        os.remove(srcPath)


def __parseContributors__(roleType, Contributors):
    if Contributors is None:
        return None
    try:
        ret = []
        for item in Contributors['items']:
            if item['role'] == roleType:
                ret.append(item['name'])
        return ret
    except:
        return None


def __setMetaData__(track: Track, album: Album, filepath, contributors, lyrics):
    try:
        obj = aigpy.tag.TagTool(filepath)
    except:
        __fixFileWithFFmpeg__(filepath)
        obj = aigpy.tag.TagTool(filepath)

    obj.album = track.album.title
    obj.title = track.title
    if not aigpy.string.isNull(track.version):
        obj.title += ' (' + track.version + ')'

    obj.artist = list(map(lambda artist: artist.name, track.artists))
    obj.copyright = track.copyRight
    obj.tracknumber = track.trackNumber
    obj.discnumber = track.volumeNumber
    obj.composer = __parseContributors__('Composer', contributors)
    obj.isrc = track.isrc

    obj.albumartist = list(map(lambda artist: artist.name, album.artists))
    obj.date = album.releaseDate
    obj.totaldisc = album.numberOfVolumes
    obj.lyrics = lyrics
    if obj.totaldisc <= 1:
        obj.totaltrack = album.numberOfTracks
    coverpath = TIDAL_API.getCoverUrl(album.cover, "1280", "1280")
    obj.save(coverpath)


def __fixFileWithFFmpeg__(filepath):
    try:
        import os
        import shutil
        import tempfile
        from ffmpeg import FFmpeg, Progress
        
        # Create temporary output file
        temp_fd, temp_path = tempfile.mkstemp(suffix=os.path.splitext(filepath)[1])
        os.close(temp_fd)
        
        try:
            ffmpeg = FFmpeg().option('y').input(filepath).output(temp_path)

            @ffmpeg.on('start')
            def on_start(arguments: list[str]):
                Printf.info(f"Fixing file with FFmpeg: arguments: {arguments}")

            @ffmpeg.on('progress')
            def on_progress(progress: Progress):
                Printf.info(f"Fixing file with FFmpeg: progress: {progress}")

            ffmpeg.execute()
            
            # Replace original with fixed file (handle cross-drive moves on Windows)
            shutil.move(temp_path, filepath)
            return True
        finally:
            # Clean up temp file if it still exists
            if os.path.exists(temp_path):
                os.unlink(temp_path)
                
    except Exception as e:
        Printf.err(f"Failed to fix file with FFmpeg: {str(e)}")
        return False


def downloadCover(album):
    if album is None:
        return
    path = getAlbumPath(album) + '/cover.jpg'
    url = TIDAL_API.getCoverUrl(album.cover, "1280", "1280")
    aigpy.net.downloadFile(url, path)


def downloadAlbumInfo(album, tracks):
    if album is None:
        return

    path = getAlbumPath(album)
    aigpy.path.mkdirs(path)

    path += '/AlbumInfo.txt'
    infos = ""
    infos += "[ID]          %s\n" % (str(album.id))
    infos += "[Title]       %s\n" % (str(album.title))
    infos += "[Artists]     %s\n" % (TIDAL_API.getArtistsName(album.artists))
    infos += "[ReleaseDate] %s\n" % (str(album.releaseDate))
    infos += "[SongNum]     %s\n" % (str(album.numberOfTracks))
    infos += "[Duration]    %s\n" % (str(album.duration))
    infos += '\n'

    for index in range(0, album.numberOfVolumes):
        volumeNumber = index + 1
        infos += f"===========CD {volumeNumber}=============\n"
        for item in tracks:
            if item.volumeNumber != volumeNumber:
                continue
            infos += '{:<8}'.format("[%d]" % item.trackNumber)
            infos += "%s\n" % item.title
    aigpy.file.write(path, infos, "w+")


def downloadVideo(video: Video, album: Album = None, playlist: Playlist = None):
    try:
        stream = TIDAL_API.getVideoStreamUrl(video.id, SETTINGS.videoQuality)
        path = getVideoPath(video, album, playlist)

        Printf.video(video, stream)
        logging.info("[DL Video] name=" + aigpy.path.getFileName(path) + "\nurl=" + stream.m3u8Url)

        m3u8content = requests.get(stream.m3u8Url).content
        if m3u8content is None:
            Printf.err(f"DL Video[{video.title}] getM3u8 failed.{str(e)}")
            return False, f"GetM3u8 failed.{str(e)}"

        urls = aigpy.m3u8.parseTsUrls(m3u8content)
        if len(urls) <= 0:
            Printf.err(f"DL Video[{video.title}] getTsUrls failed.{str(e)}")
            return False, "GetTsUrls failed.{str(e)}"

        check, msg = aigpy.m3u8.downloadByTsUrls(urls, path)
        if check:
            Printf.success(video.title)
            return True
        else:
            Printf.err(f"DL Video[{video.title}] failed.{msg}")
            return False, msg
    except Exception as e:
        Printf.err(f"DL Video[{video.title}] failed.{str(e)}")
        return False, str(e)


def downloadTrack(track: Track, album=None, playlist=None, userProgress=None, partSize=1048576):
    try:
        stream = TIDAL_API.getStreamUrl(track.id, SETTINGS.audioQuality)
        path = getTrackPath(track, stream, album, playlist)

        if SETTINGS.showTrackInfo and not SETTINGS.multiThread:
            Printf.track(track, stream)

        if userProgress is not None:
            userProgress.updateStream(stream)

        # check exist
        if __isSkip__(path, stream.url):
            Printf.success(aigpy.path.getFileName(path) + " (skip:already exists!)")
            return True, ''

        # download
        logging.info("[DL Track] name=" + aigpy.path.getFileName(path) + "\nurl=" + stream.url)

        tool = aigpy.download.DownloadTool(path + '.part', stream.urls)
        tool.setUserProgress(userProgress)
        tool.setPartSize(partSize)
        check, err = tool.start(SETTINGS.showProgress and not SETTINGS.multiThread)
        if not check:
            Printf.err(f"DL Track '{track.title}' failed: {str(err)}")
            return False, str(err)

        # encrypted -> decrypt and remove encrypted file
        __encrypted__(stream, path + '.part', path)

        # contributors
        try:
            contributors = TIDAL_API.getTrackContributors(track.id)
        except:
            contributors = None

        # lyrics
        try:
            lyrics = TIDAL_API.getLyrics(track.id).subtitles
            if SETTINGS.lyricFile:
                lrcPath = path.rsplit(".", 1)[0] + '.lrc'
                aigpy.file.write(lrcPath, lyrics, 'w')
        except:
            lyrics = ''

        __setMetaData__(track, album, path, contributors, lyrics)
        Printf.success(track.title)

        return True, ''
    except Exception as e:
        # TODO: Invalid FLAC file
        Printf.err(f"DL Track '{track.title}' failed: {str(e)}")
        return False, str(e)


def downloadTracks(tracks, album: Album = None, playlist: Playlist = None):
    def __getAlbum__(item: Track):
        album = TIDAL_API.getAlbum(item.album.id)
        if SETTINGS.saveCovers and not SETTINGS.usePlaylistFolder:
            downloadCover(album)
        return album

    if not SETTINGS.multiThread:
        for index, item in enumerate(tracks):
            itemAlbum = album
            if itemAlbum is None:
                itemAlbum = __getAlbum__(item)
                item.trackNumberOnPlaylist = index + 1
            downloadTrack(item, itemAlbum, playlist)
    else:
        thread_pool = ThreadPoolExecutor(max_workers=5)
        for index, item in enumerate(tracks):
            itemAlbum = album
            if itemAlbum is None:
                itemAlbum = __getAlbum__(item)
                item.trackNumberOnPlaylist = index + 1
            thread_pool.submit(downloadTrack, item, itemAlbum, playlist)
        thread_pool.shutdown(wait=True)


def downloadVideos(videos, album: Album, playlist=None):
    for item in videos:
        downloadVideo(item, album, playlist)
