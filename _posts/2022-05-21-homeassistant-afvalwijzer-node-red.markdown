---
classes: wide
title:  "Home Assistant Afvalwijzer integration with Node-RED"
date:   2022-05-21
categories: Tech
tags: homeassistant afvalwijzer node-red
---

Some time ago I added the [Afvalwijzer component](https://github.com/xirixiz/homeassistant-afvalwijzer) to my Home Assistant to integrate with my dutch waste collector's schedule. The component is easy to configure and provides usable sensors. In the readme and on the [community topic](https://community.home-assistant.io/t/garbage-pickup-date-mijnafvalwijzer-nl-custom-component/34631/664) more information can be found on how to nicely present this information on the dashboard.

I noticed that many users struggle with template sensors and stuff to get this done. I myself find it much easier and, at least as important, more fun to use [Node-RED](https://nodered.org/) for the automation and custom sensors. Therefore I decided to share and explain my setup.

Even though this post is specific for the Afvalwijzer integration the mechanisms shown here can be used for other components also.

# The goal

My goal was to have a simple overview on my HA dashboard showing the upcoming pickup dates for the waste types. Extra emphasis should be given for pickup dates the next day so I wouldn't need an extra item on the dashboard for that.

![afvalwijzer card](/assets/afvalwijzer_img_1.png "Sorted glance card"){: .align-center .max-width-500}

In addition Node-RED will send a notification at a given timestamp if waste will be collected the next day.

# Prerequisites

* [The Afvalwijzer integration](https://github.com/xirixiz/homeassistant-afvalwijzer)
* [The Node-RED add-on](https://github.com/hassio-addons/addon-node-red/blob/main/node-red/DOCS.md)
* [The Node-RED companion integration](https://github.com/zachowj/hass-node-red). This is needed for the entity nodes, effectively replacing Template Sensors
* [Lovelace auto-entities component](https://github.com/thomasloven/lovelace-auto-entities). This is used to sort the items in the glance card

If you are new to Node RED you may want to read or watch some tutorial, for example [this video](https://www.youtube.com/watch?v=hBEb_FCLRU8). You may try to skip this and try to follow my instructions in this post but apart from some tips I won't go too much into detail. 

**TIP** If you are new to Node-RED: *use the debug node and set it to output the complete message object*<br>
Messages show up in the right side-bar under the 'bug' icon.
{: .notice--info}


# Pickup notification

This is the easiest part. Sending a notification can be done in many different ways. The afvalwijzer provides sensors `_next_date`, `_next_in_days` and `_next_type`. I decided to use the attribute `is_collection_date_tomorrow` on the on each waste type sensor. This is how the sequence looks:

![notification sequence](/assets/afvalwijzer_img_2.png "Notification sequence"){: .align-center .max-width-500}

You can load this sequence in Node-RED by importing the following JSON. Tip: use the copy button!
```json
[{"id":"8f9adbb825d0f118","type":"inject","z":"0996cefd2319036b","name":"19:15","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"15 19 * * *","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":90,"y":780,"wires":[["99aba30cd16bbe53","3b624f11cf567449","fb6e12092b3a07d7"]]},{"id":"99aba30cd16bbe53","type":"api-current-state","z":"0996cefd2319036b","name":"GFT morgen?","server":"cd12362b.2d1aa8","version":3,"outputs":2,"halt_if":"$entity().attributes.is_collection_date_tomorrow","halt_if_type":"jsonata","halt_if_compare":"jsonata","entity_id":"sensor.afvalwijzer_gft","state_type":"str","blockInputOverrides":false,"outputProperties":[{"property":"payload","propertyType":"msg","value":"GFT","valueType":"str"},{"property":"data","propertyType":"msg","value":"","valueType":"entity"}],"for":"0","forType":"num","forUnits":"minutes","override_topic":false,"state_location":"payload","override_payload":"msg","entity_location":"data","override_data":"msg","x":260,"y":780,"wires":[["f4adac6b9d78c788"],[]]},{"id":"f4adac6b9d78c788","type":"api-call-service","z":"0996cefd2319036b","name":"Notify Bert","server":"cd12362b.2d1aa8","version":5,"debugenabled":false,"domain":"notify","service":"mobile_app_ane_lx1","areaId":[],"deviceId":[],"entityId":[],"data":"{ \"message\": payload & ' mag bij de straat' }","dataType":"jsonata","mergeContext":"","mustacheAltTags":false,"outputProperties":[],"queue":"none","x":470,"y":780,"wires":[[]]},{"id":"3b624f11cf567449","type":"api-current-state","z":"0996cefd2319036b","name":"Restafval morgen?","server":"cd12362b.2d1aa8","version":3,"outputs":2,"halt_if":"$entity().attributes.is_collection_date_tomorrow","halt_if_type":"jsonata","halt_if_compare":"jsonata","entity_id":"sensor.afvalwijzer_restafval","state_type":"str","blockInputOverrides":false,"outputProperties":[{"property":"payload","propertyType":"msg","value":"Restafval","valueType":"str"},{"property":"data","propertyType":"msg","value":"","valueType":"entity"}],"for":"0","forType":"num","forUnits":"minutes","override_topic":false,"state_location":"payload","override_payload":"msg","entity_location":"data","override_data":"msg","x":270,"y":720,"wires":[["f4adac6b9d78c788"],[]]},{"id":"fb6e12092b3a07d7","type":"api-current-state","z":"0996cefd2319036b","name":"Papier morgen?","server":"cd12362b.2d1aa8","version":3,"outputs":2,"halt_if":"$entity().attributes.is_collection_date_tomorrow","halt_if_type":"jsonata","halt_if_compare":"jsonata","entity_id":"sensor.afvalwijzer_papier","state_type":"str","blockInputOverrides":false,"outputProperties":[{"property":"payload","propertyType":"msg","value":"Papier","valueType":"str"},{"property":"data","propertyType":"msg","value":"","valueType":"entity"}],"for":"0","forType":"num","forUnits":"minutes","override_topic":false,"state_location":"payload","override_payload":"msg","entity_location":"data","override_data":"msg","x":260,"y":840,"wires":[["f4adac6b9d78c788"],[]]},{"id":"cd12362b.2d1aa8","type":"server","name":"Home Assistant","version":2,"addon":true,"rejectUnauthorizedCerts":true,"ha_boolean":"y|yes|true|on|home|open","connectionDelay":true,"cacheJson":true,"heartbeat":false,"heartbeatInterval":"30"}]
```

On the left we have an inject node, which I configured to send a message each day at a given time.

In the middle we have current state nodes which we use to filter on an entity attribute and pass a custom payload:

| **Entity ID** | `sensor.afvalwijzer_restafval`
| **If State**  | JSONata `$entity().attributes.is_collection_date_tomorrow`
| **msg.payload** | Restafval

**NOTE** Your entities may be named differently. Use the developer tools in Home Assistant to find out which entities are provided for your waste collector. You can filter on `afvalwijzer`.
{: .notice--info}

On the right the notification node. As data I use JSONata again to construct a nice message:
```
{ "message": payload & ' mag bij de straat' }
```


# Changing state and pictures

The afvalwijzer sensors just provide a date, like '22-05-2022'. I want to translate those to weekdays if they are in the next few days, and I want to change the picture when de pickup date is tomorrow. To achieve this we can create 'dummy' sensors with the `entity` node. An entity node will create an entity in Home Assistant, similar to a template sensor or a helper.

![sensor sequence](/assets/afvalwijzer_img_3.png "Sensor sequence"){: .align-center .max-width-600}

In short, any change to the different afvalwijzer entities will trigger a message. In the function node the date will be replaced by a weekday if appropriate and a picture location will be included to the message depending on the waste type and days left. The switch will direct the messages to the correct entity nodes, which will be updated with the new picture and state.

Again you can import this sequence to have a better look into it, which saves me from adding lots of screenshots and information:
```json
[{"id":"aecc3f915aab441e","type":"inject","z":"0dca8d4ce2426def","name":"Test papier","props":[{"p":"payload"},{"p":"data","v":"{\"new_state\":{\"attributes\":{\"days_until_collection_date\":1}}}","vt":"json"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"sensor.afvalwijzer_papier","payload":"09-09-9999","payloadType":"str","x":140,"y":760,"wires":[["cf2e6a48346325d0"]]},{"id":"258318bc40fc1fa1","type":"server-state-changed","z":"0dca8d4ce2426def","name":"Afvalwijzer","server":"cd12362b.2d1aa8","version":4,"exposeToHomeAssistant":false,"haConfig":[{"property":"name","value":""},{"property":"icon","value":""}],"entityidfilter":"sensor.afvalwijzer_(restafval|papier|gft)","entityidfiltertype":"regex","outputinitially":true,"state_type":"str","haltifstate":"","halt_if_type":"str","halt_if_compare":"is","outputs":1,"output_only_on_state_change":false,"for":"0","forType":"num","forUnits":"minutes","ignorePrevStateNull":false,"ignorePrevStateUnknown":false,"ignorePrevStateUnavailable":false,"ignoreCurrentStateUnknown":true,"ignoreCurrentStateUnavailable":true,"outputProperties":[{"property":"payload","propertyType":"msg","value":"","valueType":"entityState"},{"property":"data","propertyType":"msg","value":"","valueType":"eventData"},{"property":"topic","propertyType":"msg","value":"","valueType":"triggerId"}],"x":140,"y":620,"wires":[["cf2e6a48346325d0"]]},{"id":"cf2e6a48346325d0","type":"function","z":"0dca8d4ce2426def","name":"Afval","func":"let weekdays = [\n    \"Zondag\",\n    \"Maandag\",\n    \"Dinsdag\",\n    \"Woensdag\",\n    \"Donderdag\",\n    \"Vrijdag\",\n    \"Zaterdag\"\n]\n\nlet pattern = /sensor.afvalwijzer_(.*)/\nlet type = msg.topic.match(pattern)[1]\nlet days = msg.data.new_state.attributes.days_until_collection_date\n\nlet suffix = days < 2 ? '_alert' : ''\nlet picture = `/local/afvalwijzer/${type}${suffix}.png`\n\nlet state = msg.payload\nif (days == 0) {\n    state = 'Vandaag!'\n} else if (days == 1) {\n    state = 'Morgen!'\n} else if (days < 7) {\n    let collectionDate = new Date()\n    collectionDate.setDate(collectionDate.getDate()+days)\n    state = weekdays[collectionDate.getDay()]\n}\n\nreturn {\n    topic: type,\n    payload: state,\n    picture: picture,\n    days: days\n}","outputs":1,"noerr":0,"initialize":"","finalize":"","libs":[],"x":290,"y":620,"wires":[["67a8d1cb53d329e7"]]},{"id":"67a8d1cb53d329e7","type":"switch","z":"0dca8d4ce2426def","name":"soort","property":"topic","propertyType":"msg","rules":[{"t":"eq","v":"restafval","vt":"str"},{"t":"eq","v":"gft","vt":"str"},{"t":"eq","v":"papier","vt":"str"}],"checkall":"true","repair":false,"outputs":3,"x":430,"y":620,"wires":[["cebc7034cff034cc"],["70b841e83b555d0e"],["3cd577e34febcaa2"]],"outputLabels":["Restafval","GFT","Papier"]},{"id":"2c9c1acdbbbbe5b6","type":"inject","z":"0dca8d4ce2426def","name":"Test restafval","props":[{"p":"payload"},{"p":"data","v":"{\"new_state\":{\"attributes\":{\"days_until_collection_date\":1}}}","vt":"json"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"sensor.afvalwijzer_restafval","payload":"09-09-9999","payloadType":"str","x":130,"y":680,"wires":[["cf2e6a48346325d0"]]},{"id":"3d7ebd6992df5c06","type":"inject","z":"0dca8d4ce2426def","name":"Test gft","props":[{"p":"payload"},{"p":"data","v":"{\"new_state\":{\"attributes\":{\"days_until_collection_date\":1}}}","vt":"json"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"sensor.afvalwijzer_gft","payload":"09-09-9999","payloadType":"str","x":150,"y":720,"wires":[["cf2e6a48346325d0"]]},{"id":"cebc7034cff034cc","type":"ha-entity","z":"0dca8d4ce2426def","name":"Restafval","server":"cd12362b.2d1aa8","version":2,"debugenabled":false,"outputs":1,"entityType":"sensor","config":[{"property":"name","value":"Restafval"},{"property":"device_class","value":""},{"property":"icon","value":""},{"property":"unit_of_measurement","value":""},{"property":"state_class","value":""},{"property":"last_reset","value":""}],"state":"payload","stateType":"msg","attributes":[{"property":"entity_picture","value":"picture","valueType":"msg"},{"property":"days","value":"days","valueType":"msg"}],"resend":true,"outputLocation":"payload","outputLocationType":"none","inputOverride":"allow","outputOnStateChange":false,"outputPayload":"","outputPayloadType":"str","x":600,"y":580,"wires":[[]]},{"id":"70b841e83b555d0e","type":"ha-entity","z":"0dca8d4ce2426def","name":"GFT","server":"cd12362b.2d1aa8","version":2,"debugenabled":false,"outputs":1,"entityType":"sensor","config":[{"property":"name","value":"GFT"},{"property":"device_class","value":""},{"property":"icon","value":""},{"property":"unit_of_measurement","value":""},{"property":"state_class","value":""},{"property":"last_reset","value":""}],"state":"payload","stateType":"msg","attributes":[{"property":"entity_picture","value":"picture","valueType":"msg"},{"property":"days","value":"days","valueType":"msg"}],"resend":true,"outputLocation":"payload","outputLocationType":"none","inputOverride":"allow","outputOnStateChange":false,"outputPayload":"","outputPayloadType":"str","x":590,"y":620,"wires":[[]]},{"id":"3cd577e34febcaa2","type":"ha-entity","z":"0dca8d4ce2426def","name":"Papier","server":"cd12362b.2d1aa8","version":2,"debugenabled":false,"outputs":1,"entityType":"sensor","config":[{"property":"name","value":"Papier"},{"property":"device_class","value":""},{"property":"icon","value":""},{"property":"unit_of_measurement","value":""},{"property":"state_class","value":""},{"property":"last_reset","value":""}],"state":"payload","stateType":"msg","attributes":[{"property":"entity_picture","value":"picture","valueType":"msg"},{"property":"days","value":"days","valueType":"msg"}],"resend":true,"outputLocation":"payload","outputLocationType":"none","inputOverride":"allow","outputOnStateChange":false,"outputPayload":"","outputPayloadType":"str","x":590,"y":660,"wires":[[]]},{"id":"cd12362b.2d1aa8","type":"server","name":"Home Assistant","version":2,"addon":true,"rejectUnauthorizedCerts":true,"ha_boolean":"y|yes|true|on|home|open","connectionDelay":true,"cacheJson":true,"heartbeat":false,"heartbeatInterval":"30"}]
```

I will give a short description of the different nodes

## Events: state node

I use the regex `sensor.afvalwijzer_(restafval|papier|gft)` to select the right entities in a single node. If this seems too advanced you can simply create an `events: state` node for each sensor.

**NOTE** I leave `Current state equals previous state` unchecked. This is because the state (pickup date) typically stays the same between updates, but we want to react on the attribute `days_until_collection_date` which changes every day.
{: .notice--info }

## Function node

[Function](https://nodered.org/docs/user-guide/writing-functions) nodes are the most powerful nodes in Node-RED, but they should be used with care. If no other node is suitable a function node can be used, but try to keep its logic as simple as possible. It's often better to have two nodes performing simple functions than one node that combines multiple functions (*"do one thing and do it well"*). I must admit that this is one is already on the edge. The fact that I couldn't come up with a better name than 'Afval' (Waste) already indicates that.

It's not necessary to use a function node for all this stuff, if you prefer you can probably use other nodes (like `switch` and `change` nodes) to filter and adjust messages. But for this sequence I decided that this would make it more complicated rather than simple. The fact that I'm an experienced developer probably also influenced that decision :wink:.

In the function I use a regex to extract the waste type (`type`) from the entity id (`msg.topic`). The number of days left is obtained from the attribute `days_until_collection_date`. I simply used a debug node printing the full message object to find out about the structure.


```javascript
let weekdays = [
    "Zondag",
    "Maandag",
    "Dinsdag",
    "Woensdag",
    "Donderdag",
    "Vrijdag",
    "Zaterdag"
]

let pattern = /sensor.afvalwijzer_(.*)/
let type = msg.topic.match(pattern)[1]
let days = msg.data.new_state.attributes.days_until_collection_date

let suffix = days < 2 ? '_alert' : ''
let picture = `/local/afvalwijzer/${type}${suffix}.png`

let state = msg.payload
if (days == 0) {
    state = 'Vandaag!'
} else if (days == 1) {
    state = 'Morgen!'
} else if (days < 7) {
    let collectionDate = new Date()
    collectionDate.setDate(collectionDate.getDate()+days)
    state = weekdays[collectionDate.getDay()]
}

return {
    topic: type,
    payload: state,
    picture: picture,
    days: days
}
```

A resulting message will ook something like:
```json
{
  "topic": "restafval",
  "payload": "14-06-2022",
  "picture": "/local/afvalwijzer/restafval.png",
  "days": 25
}
```

You can find my icons here: TODO
The images have to be put in the homeassistant folder `www/afvalwijzer`. I took the original images from [xirix/my-hass-config](https://github.com/xirixiz/my-hass-config/tree/master/www/afvalwijzer) and colored the alert versions myself. They aren't too pretty I'm afraid but it does the job.


## Switch node

This node quite trivially forwards each message to a given output based on its topic.

## Entity node

As mentioned earlier, an entity node will create a Home Assistant Entity (limited to 'Binary Sensor', 'Sensor' and 'Switch'). I configured those as follows:

![entity node](/assets/afvalwijzer_img_4.png "Entity node"){: .align-center .max-width-500}

As you can see we added two attributes which will be updated by the incoming messages. The `entity_picture` is used in lovelace instead of the icon if present. The `days` attribute is custom and will be used later on to sort the items.

The state is also updated. Unfortunately it is not easily possible to update the name of an `entity` node.

**NOTE** When first deployed, the name will be used as entity id. After that the name can be changed without affecting the entity id. Because I wanted entity id's like `sensor.pickupdate_restafval` I had to set the name to `Pickupdate restafval` on first deployment and change it to `Restafval` later on.<br>
If you are not satisfied with your entity id, simply delete the entity node and deploy (this will delete the entity also!), then create and deploy a new entity node with another name.
{: .notice--warning}

## Test trigger nodes

To test if state and picture are updated as expected I added some `inject` nodes for testing.

Because the `Events: state` node is configured to `output on connect` the test state will be reset after a redeploy.

# Sorted glance card

I learnt about the auto-entities card from the Afvalwijzer Integration documentation and found it very useful. With our custom sensors it's quite easy to use. Simply edit your lovelace dashboard, choose `Add Card ➔ Custom: Auto Entities ➔ Show code editor` and paste the following yaml:

```yaml
type: custom:auto-entities
card:
  show_name: true
  show_icon: true
  show_state: true
  type: glance
filter:
  include:
    - entity_id: sensor.pickupdate_*
sort:
  attribute: days
  method: attribute
  numeric: true
```

If you can't find the 'Auto Entities' card you probably didn't (correctly) install it. Please try to follow the documentation to install it, but I remember that I struggled a bit with it to get it properly installed.

If everything is working you can now play with the test nodes and observe that the icons will be reordered and colored as required.

# Possible improvements

One improvement I'm thinking about is to put a `tap-action` on the pictures to toggle a sensor, indicating that the waste has already be placed next to the street. Tapping the picture for the next day would then render the normal (not red) picture and no notification should go out if not send already.

Maybe I'll once do this and update this post.

# Conclusion

As said earlier, for me Node-RED is much easier for automation and much more fun than using the default Home Assistant automations. In addition, for me at least, the `entity` node is much easier to use than template sensors, although only few entity types are supported. The `debug` and `inject` nodes make it also quite easy to debug and test sequences. And the import/export functionality is very handy when it comes to sharing ideas on the internet.

It does require some time to get to know to the different types of nodes and I must admit that I have spend hours on some sequences just to get them as nice and clean as possible, but that's also a lot of fun and quite rewarding. Especially when you finally sit back and look at this simple sequence of nicely colored nodes describing your automation.

