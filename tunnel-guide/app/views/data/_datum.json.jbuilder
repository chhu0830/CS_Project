json.extract! datum, :id, :mac, :speed, :distance, :ip, :created_at, :updated_at
json.url datum_url(datum, format: :json)