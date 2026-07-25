from app.config.supabase import supabase

class Database:
  def __init__(self):
    self.client=supabase

db=Database()