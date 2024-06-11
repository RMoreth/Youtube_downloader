from pytube import YouTube
from pytube.cli import on_progress  # importa a barra de progresso


def salvar_video(link_do_video):
    print('iniciando download...')

    try:
        yt = YouTube(link_do_video, on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()

        return '\nDownload comleto!'
    except:
        return 'Não foi possível baixar o video.'


if __name__ == "__main__":
    while True:
        link_do_video = input(
            'informe o link do YouTube para baixar oou aperte Enter para encerrar o programa: ')

        if link_do_video != '':
            print(salvar_video(link_do_video))
            continue
        else:
            print('Programa Encerrado')
            break
