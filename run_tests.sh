# テストを実行する
# 使い方:
#   全テスト実行:
#     ./run_tests.sh
#   特定のテスト実行:
#     ./run_tests.sh tests/XXXXXX.py


# jupyter_workspaceはマウントされているので、依存ライブラリは別の場所に配置し、conftest.pyでsys.pathに追加している
docker compose cp ./modules/some_module.py glue.dev:/home/glue_user/workspace/
# コンテナ内でpytestを実行する
# -T: ttyをoffにする。ttyありだとエラーになるため
# -u: ユーザー名指定。コンテナ内でsparkを実行できるユーザーにする
# -w: cwdの指定。テストファイルをマウントしている場所でpytestを実行するため

docker compose exec -T -u glue_user -w /home/glue_user/workspace/jupyter_workspace glue.dev  /home/glue_user/.local/bin/pytest $1
