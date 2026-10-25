import os,sys,time,socket,subprocess
import pytest,requests
@pytest.fixture(scope="session")
def base_url():
 external=os.getenv("TARGET_URL")
 if external:yield external;return
 with socket.socket() as sock:sock.bind(("127.0.0.1",0));port=sock.getsockname()[1]
 process=subprocess.Popen([sys.executable,"-m","uvicorn","demo:app","--host","127.0.0.1","--port",str(port)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 base=f"http://127.0.0.1:{port}"
 try:
  for _ in range(100):
   try:
    if requests.get(base+"/health",timeout=.2).ok:break
   except requests.RequestException:pass
   time.sleep(.1)
  else:raise RuntimeError("demo did not start")
  yield base
 finally:
  process.terminate();process.wait(timeout=10)
@pytest.fixture
def api(base_url):
 session=requests.Session();session.headers["Authorization"]="Bearer "+os.getenv("TEST_TOKEN","local-test-token")
 yield session,base_url
 session.close()
