# MQTTChatHub

**MQTTChatHub** is a lightweight command-line chat application powered by MQTT, designed for seamless communication. Connect to the HiveMQ broker, engage in real-time conversations, and enjoy a simple yet effective chat experience.

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
python chat_application.py

## Configuration

- `broker_address`: Your HiveMQ broker address.
- `broker_port`: Port number for MQTT communication.
- `client_id`: Unique client ID for your MQTT client.
- `username`: Your desired username.
- `topic`: MQTT topic for chat communication.

Handle user authentication and security if your HiveMQ broker requires it. Customize the topic, client ID, and username according to your preferences.

## Contributing

Contributions are welcome! To create additional instances with different client IDs and usernames for global messaging, follow these steps:

1. Duplicate the `chat_application.py` script.
2. Update the duplicated script with a unique `client_id` and `username`.
3. Run the new script to join the chat.

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
