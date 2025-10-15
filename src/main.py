# Entry point for Google App Engine
import subprocess
import sys
import os

if __name__ == "__main__":
    # Set environment variables
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '8080')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    
    # Run Streamlit
    subprocess.run([
        sys.executable, '-m', 'streamlit', 'run', 'src/app.py',
        '--server.port=8080',
        '--server.address=0.0.0.0'
    ])
