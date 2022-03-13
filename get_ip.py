from pymongo import MongoClient
import socket
client = MongoClient()
db = client['iot_project']


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


db.ip_address.insert_one({"name": extract_ip()})
