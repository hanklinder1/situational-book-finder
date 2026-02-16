from src.db.supabase_client import get_supabase

sb = get_supabase()

# Insert a test user
resp = sb.table("users_anon").upsert(
    {"user_id": "00000000-0000-0000-0000-000000000001"}
).execute()
print("Upsert user OK:", resp.data)

# Read users
resp2 = sb.table("users_anon").select("*").limit(5).execute()
print("Read users OK:", resp2.data)
