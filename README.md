# yuruboo
GPSをもとにしてすぐに遊びにゆく友達を探すゆるぼアプリ

# ER図
```mermaid
erDiagram
  user ||--o{ gathering : "ユーザと募集は一対多"
  user ||--o{ message : "ユーザとメッセージは一対多"
  user ||--o{ participation : "ユーザと参加は一対多"
  user ||--o{ ownership : "ユーザと所有者は一対多、ユーザと贈呈者は一対多"
  genre ||--o{ gathering : "ジャンルと募集は一対多"
  gathering ||--o{ message : "募集とメッセージは一対多"
  gathering ||--o{ participation : "募集と参加は一対多"
  
  user {
    bigint id PK "User ID"
    string name "名前"
    string profile "プロフィール"
  }

  genre {
    bigint id PK "Genre ID"
    string name "ジャンル名"
    image icon "アイコン"
  }

  gathering {
    bigint id PK "Gathering ID"
    integer pos_lat "募集場所_緯度"
    integer pos_lng "募集場所_経度"
    user host FK "募集者"
    genre genre FK "ジャンル"
    string body "本文"
    integer num_participant "人数"
    timestamp created_at "募集開始日時"
  }

  message {
    bigint id PK "Message ID"
    gathering gathering FK "募集"
    string body "本文"
    user sender FK "送り手"
    timestamp created_at "投稿日時"
  }

  participation {
    bigint id PK "Participation ID"
    gathering gathering FK "募集"
    user participant FK "参加者"
  }

  ownership {
    bigint id PK "Ownership ID"
    user owner FK "所有者"
    user presenter FK "贈呈者"
    int count "本数"
  }
```

# エンドポイントの定義
```
- user
POST /users
GET, PUT, PATCH, DELETE /users/{user_id}

- genre
GET /genres
GET /genres/{genre_id}

(ジャンルは、変更・追加・削除不可)


- gathering
POST /gatherings
GET /gatherings
GET, PUT, PATCH, DELETE /gatherings/{gathering_id}

- participation
POST /participations
GET /participations (& gathering={gathering_id}) (& participant={user_id})
GET, DELETE /participations/{participation_id}

(参加は、変更不可)

- message
POST /messages
GET /messages (& gathering={gathering_id})
GET /messages/{message_id} 

(個別メッセージは変更・削除不可)

- ownerships
POST /ownerships
GET /ownerships (& owner={user_id})
GET, PUT, PATCH /ownerships/{ownership_id}

(ownershipの削除不可)
```


# 環境構築
プロジェクトをcloneする
```
git clone https://github.com/team-yurubo/yuruboo.git
```
reactの環境構築
```
cd yuruboo
cd frontend
npm install
npm run dev
```
LocalHostに接続して、react + viteの画面が表示されたら成功

djangoの環境構築 & 仮想環境の構築
```
cd ../backend
source venv/bin/activate
```
仮想環境に入ったら(venv)が表示される
```
pip install -r requirements.txt
cd backend
python manage.py runserver
```
LocalHostに接続して、djangoの画面が表示されたら成功

# テストアプリの実行
```
cd sandbox/map_test
npm install
npm run dev
```
