from app.database import run_query
def add_device(name):
    query = """
    CREATE (d:Device {name: $name})
    RETURN d
    """
    return run_query(query, {"name": name})
def connect_user_to_device(user, device):
    with get_session() as session:
        session.run("""
            MATCH (u:User {name: $user})
            MATCH (d:Device {name: $device})
            CREATE (u)-[:ACCESS]->(d)
        """, user=user, device=device)

def connect_device_to_server(device, server):
    with get_session() as session:
        session.run("""
            MATCH (d:Device {name: $device})
            MATCH (s:Server {name: $server})
            CREATE (d)-[:CONNECTED_TO]->(s)
        """, device=device, server=server)

def add_server(name):
    with get_session() as session:
        session.run(
            "CREATE (s:Server {name: $name})",
            name=name
        )

def add_vuln_to_device(device, cve):
    with get_session() as session:
        session.run("""
            MATCH (d:Device {name: $device})
            MATCH (v:Vulnerability {cve: $cve})
            CREATE (d)-[:HAS_VULN]->(v)
        """, device=device, cve=cve)