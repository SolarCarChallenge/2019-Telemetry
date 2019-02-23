import QtQuick 2.0
import QtQuick.Controls 1.0
import QtQuick.Dialogs 1.2




ApplicationWindow {
    id: applicationWindow
    visible: true
    width: 1271
    height: 800
    color: "#000000"
    property alias connections: connections
    title: qsTr("Solar Car Challenge")




    Image {
        id: background1
        x: -212
        y: 4
        width: 936
        height: 791
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: speedimage.horizontalCenter
        anchors.verticalCenter: speedimage.verticalCenter
        z: 0
        source: "images/background.png"
    }


    Image {
        id: background2
        x: 232
        y: 32
        width: 842
        height: 771
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: currentimage.horizontalCenter
        anchors.verticalCenter: currentimage.verticalCenter
        z: 0
        source: "images/background.png"
    }


    Image {
        id: background3
        x: 642
        y: -51
        width: 725
        height: 624
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: mainbattery.horizontalCenter
        anchors.verticalCenterOffset: 0
        anchors.verticalCenter: mainbattery.verticalCenter
        z: 0
        source: "images/background.png"
    }


    Image {
        id: backgound4
        x: 642
        y: 196
        width: 725
        height: 624
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: imagetemp.horizontalCenter
        anchors.verticalCenterOffset: 0
        anchors.verticalCenter: imagetemp.verticalCenter
        z: 0
        source: "images/background.png"
    }

    Image {
        id: motortempwarning
        x: 37
        y: 685
        width: 79
        height: 61
        z: 1
        visible: false
        source: "images/MotorTempWarning.png"
    }




    Image {
        id: speedimage
        width: 456
        height: 350
        z: 5
        anchors.verticalCenterOffset: -127
        anchors.horizontalCenterOffset: -189
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.PreserveAspectFit
        source: "images/Speedometer.png"
        Image {
            id: speedneedle
            width: 350
            height: 350
            z: 3
            anchors.verticalCenterOffset: -1
            anchors.horizontalCenterOffset: 1
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            rotation: -38
            fillMode: Image.PreserveAspectFit
            source: "images/largeneedle.png"

            Behavior on rotation { SmoothedAnimation { velocity: 30 } }
        }

        Text {
            id: speedtext
            x: 164
            y: 258
            width: 45
            height: 40
            color: "#ffffff"
            text: qsTr("0")
            renderType: Text.NativeRendering
            horizontalAlignment: Text.AlignHCenter
            anchors.verticalCenterOffset: 75
            anchors.horizontalCenterOffset: 1
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 40
        }

    }



    Image {
        id: currentimage
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        width: 350
        height: 350
        anchors.verticalCenterOffset: -127
        anchors.horizontalCenterOffset: 182
        z: 6
        source: "images/CurreentGuage.png"

        Image {
            id: currentneede
            x: 125
            y: 125
            width: 350
            height: 350
            z: 2
            rotation: -39
            anchors.verticalCenterOffset: -1
            anchors.horizontalCenterOffset: 1
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            fillMode: Image.PreserveAspectFit
            source: "images/largeneedle.png"

            Behavior on rotation { SmoothedAnimation { velocity: 30 } }
        }

        Text {
            id: currenttext
            x: 164
            y: 245
            color: "#ffffff"
            text: qsTr("0")
            anchors.verticalCenterOffset: 75
            anchors.horizontalCenterOffset: 1
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 40
        }
    }



    Image {
        id: auximage
        x: 879
        y: 136
        width: 250
        height: 250
        z: 3
        anchors.horizontalCenterOffset: -313
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenterOffset: 179
        anchors.verticalCenter: parent.verticalCenter
        source: "images/AuxBatteryGuage.png"

        Image {
            id: auxneedle
            x: 0
            y: 0
            width: 225
            height: 225
            z: 2
            rotation: -48
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            fillMode: Image.PreserveAspectFit
            source: "images/newnwwdle.png"

            Behavior on rotation { SmoothedAnimation { velocity: 30 } }
        }

        Text {
            id: auxtext
            x: 101
            y: 163
            color: "#ffffff"
            text: qsTr("0")
            anchors.verticalCenterOffset: 54
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 25
        }
        
    }

    Image {
        id: imagetemp
        x: 0
        y: 0
        width: 250
        height: 250
        z: 2
        anchors.horizontalCenterOffset: 319
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenterOffset: 179
        anchors.verticalCenter: parent.verticalCenter
        source: "images/MotorTemp.png"

        Image {
            id: tempneedle
            x: 0
            y: 0
            width: 225
            height: 225
            z: 2
            rotation: -48
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            fillMode: Image.PreserveAspectFit
            source: "images/newnwwdle.png"

            Behavior on rotation { SmoothedAnimation { velocity: 30 } }
        }

        Text {
            id: temptext
            x: 101
            y: 163
            color: "#ffffff"
            text: qsTr("0")
            font.family: "Tahoma"
            fontSizeMode: Text.HorizontalFit
            renderType: Text.NativeRendering
            anchors.verticalCenterOffset: 54
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 24
        }

    }



    Image {
        id: mainbattery
        x: 707
        y: 383
        width: 246
        height: 250
        z: 7
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenterOffset: 179
        anchors.verticalCenter: parent.verticalCenter
        source: "images/MainBatteryGuage.png"

        Image {
            id: mainneedle
            x: 75
            y: 75
            width: 225
            height: 225
            rotation: -48
            z: 2
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            fillMode: Image.PreserveAspectFit
            source: "images/newnwwdle.png"

            Behavior on rotation { SmoothedAnimation { velocity: 30 } }
        }

        Text {
            id: maintext
            x: 101
            y: 153
            color: "#ffffff"
            text: qsTr("0")
            anchors.verticalCenterOffset: 49
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 24
        }
        
    }


    Image {
        id: amphour
        x: 1087
        y: 149
        width: 112
        height: 396
        anchors.verticalCenterOffset: -175
        anchors.horizontalCenterOffset: 486
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        fillMode: Image.PreserveAspectFit
        source: "images/battery_low.png"

        Text {
            id: amphourvalue
            x: 45
            y: 314
            color: "#ffffff"
            text: qsTr("0")
            anchors.horizontalCenterOffset: 1
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 28
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 45
        }

        Text {
            id: text2
            x: 46
            y: 382
            color: "#ffffff"
            text: qsTr("AmpHour")
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 25
        }
    }

    Connections {
        id: connections
        target: dashboard
        ignoreUnknownSignals: true

        onAuxVoltage: {
            auxtext.text = auxvolt
            auxneedle.rotation=auxangle(auxvolt)
            idiotlightauxvolt(auxvolt)
        }
        onMainVoltage: {
            maintext.text = mainvolt
            mainneedle.rotation=mainangle(mainvolt)
        }
        onMainCurrent: {
            currenttext.text = maincur
            currentneede.rotation=currentangle(maincur)
        }
        onCarSpeed: {
            speedtext.text = speedmph
            speedneedle.rotation=speedangle(speedmph)
        }
        onMotorTemp: {
            temptext.text=tempval
            tempneedle.rotation=motortempangle(tempval)
            idiotlighttemp(tempval)


        }
        onAmpHour: {
            amphourvalue.text=amphr
            amphour.source=amphourpicture(amphr)


        }


    }


    function auxangle(value)
    {
        if (value <= 7){
            return -48
        }

        if (value >= 17){
            return 229
        }
        return ((value*27.7)-241.9)
        
    }
    function mainangle(value)
    {
        if (value <= 38){
            return -48
        }

        if (value >= 58){
            return 229
        }
        return ((value*13.85)-574.3)
        
    }
    function currentangle(value)
    {
        if (value <= -50){
            return -39
        }

        if (value >= 50){
            return 219
        }
        return ((value*2.59)+90)
        
    }
    function speedangle(value)
    {
        if (value <= 0){
            return -39
        }

        if (value >= 60){
            return 219
        }
        return ((value*4.35)-39)
        
    }
    function amphourpicture(value)
    {

        if (value <= 25){
            return "images/battery_low.png"
        }
        else if (value <=50){
            return "images/battery_low1.png"
        }
        else if (value <75){
            return "images/battery_med.png"
        }
        else {
            return "images/battery_full.png"
        }
    }
    function motortempangle(value)
    {
        if (value <= 15){
            return -48
        }

        if (value >= 65){
            return 229
        }
        return ((value*5.43137)-124.039)

    }
    function idiotlighttemp(value){
        if (value > 28)
        {
            motortempwarning.visible=true
            imagetemp.source="images/MotorTempRed.png"
            temptext.color="#ff1b1b"
            return
        }
        else{
            motortempwarning.visible=false
            temptext.color="#ffffff"
            imagetemp.source="images/MotorTemp.png"
            return
        }
    }
    function idiotlightauxvolt(value){
        if (value > 14.3)
        {
            auximage.source="images/AuxBatteryGuageRed.png"
            auxtext.color="#ff1b1b"
            auxidiot.visible=true
            return
        }
        else if (value < 11.5){
            auximage.source="images/AuxBatteryGuageRed.png"
            auxtext.color="#ff1b1b"
            auxidiot.visible=true
            return
        }

        else{
            motortempwarning.visible=false
            auxtext.color="#ffffff"
            auximage.source="images/AuxBatteryGuage.png"
            auxidiot.visible=false

            return
        }

    }


    


    Image {
        id: challenglogo
        x: 452
        y: 615
        width: 307
        height: 139
        anchors.verticalCenterOffset: -330
        anchors.horizontalCenterOffset: -482
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        source: "images/Challengelogo.png"
    }





    Image {
        id: backgound5
        x: 638
        y: 197
        width: 725
        height: 624
        visible: true
        z: 0
        anchors.horizontalCenter: auximage.horizontalCenter
        anchors.verticalCenter: auximage.verticalCenter
        anchors.verticalCenterOffset: 0
        source: "images/background.png"
        anchors.horizontalCenterOffset: 0
    }

    Image {
        id: auxidiot
        x: 39
        y: 604
        width: 81
        height: 73
        visible: false
        source: "images/AuxWarning.png.png"
    }



}
