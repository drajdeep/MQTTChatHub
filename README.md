# MQTTChatHub

**MQTTChatHub** is a lightweight command-line chat application powered by MQTT, designed for seamless communication. Connect to the HiveMQ broker, engage in real-time conversations, and enjoy a simple yet effective chat experience.
**Security Highlights:**
MQTTChatHub boasts a high level of security, thanks to its lightweight and untraceable message packets exchanged between users. This makes it an ideal choice for secure communication. In comparison to widely-used alternatives like socket.io, MQTTChatHub provides a robust and secure messaging platform. The decentralized nature of MQTT ensures that messages are transmitted efficiently while maintaining a high level of confidentiality.

## Setup

1. **Install Dependencies:**
    ```bash
    pip install paho-mqtt
    ```

2. **Configure the Application:**
    Open the `chat_application.py` script and update the following variables:
    - `broker_address`: Your HiveMQ broker address.
    - `broker_port`: Port number for MQTT communication.
    - `client_id`: Unique client ID for your MQTT client.
    - `username`: Your desired username.
    - `topic`: MQTT topic for chat communication.

## Usage

Run the script:
```bash
python chat_application.py 
```
## Configuration

- `broker_port`: Port number for MQTT communication.
- `client_id`: Unique client ID for your MQTT client.
- `username`: Your desired username.
- `topic`: MQTT topic for chat communication.

Handle user authentication and security if your HiveMQ broker requires it. Customize the topic, client ID, and username according to your preferences.

**Important Note:** Ensure that the MQTT topic you choose is unique to avoid conflicts with other users. The `topic` variable in the `chat_application.py` script determines the MQTT topic for chat communication. Set your own topic name in this variable. It is crucial that the topic is not a common term, as it might be used by other users worldwide. Each user in the chat group should use the same topic, but unique `client_id` and `username` values.


## Contributing

Contributions are welcome! 

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
