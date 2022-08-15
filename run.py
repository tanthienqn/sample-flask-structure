import os
from server.app import create_app

if __name__ == '__main__':
    env_name = os.getenv('SERVER_ENV', 'development')
    host_env = os.getenv('HOST_NAME', '0.0.0.0')
    port_env = os.getenv('PORT_NAME', '5000')
    app = create_app(env_name)
    app.run(host=host_env, threaded=True, port=port_env, debug=app.config['DEBUG'], use_reloader=False)
