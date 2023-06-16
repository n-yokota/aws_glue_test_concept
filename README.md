# テスト付きの glue scripts

## 全体像

GithubActions を使った CI/CD のイメージ

```mermaid
graph LR
    subgraph AWS
        Glue
        S3[(S3)]

    end
    subgraph GithubActionsServer
        docker[docker-compose.yml]
        GlueContainer
        ScriptFile
    end

    docker -. 起動 .-> GlueContainer
    S3 -- スクリプトの参照 --> Glue
    ScriptFile -- upload --> S3
    GlueContainer -. test .-> ScriptFile
```

## テスト方法

```bash

cd glue-jobs-with-tests
docker compose up -d
./run_tests.sh tests/test_some_batch_script.py
```

- Spark・Glue の実行環境は docker で準備している
- docker 内に pytest がすでにインポートされているため、run_tests.sh でそれをキックする
