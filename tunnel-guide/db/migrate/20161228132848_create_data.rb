class CreateData < ActiveRecord::Migration[5.0]
  def change
    create_table :data do |t|
      t.string :mac
      t.float :speed
      t.float :distance
      t.string :ip

      t.timestamps
    end
  end
end
