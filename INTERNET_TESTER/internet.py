#internet speed test
import speedtest
st = speedtest.Speedtest()
print(f"Download: {st.download()/1_000_000:.2f} Mbps")
print(f"Upload: {st.upload()/1_000_000:.2f} Mbps")
