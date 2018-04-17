PASSWORD="codetu"
security unlock-keychain -p $PASSWORD ~/Library/Keychains/login.keychain

UDID=$(idevice_id -l | head -n1)

xcodebuild -project WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test

