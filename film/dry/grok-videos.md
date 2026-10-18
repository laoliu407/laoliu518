# 《干》Grok 视频任务单

## 给你看的用法

全片要用 Grok Imagine 生成 23 个视频镜头。每条的做法都一样：**上传对应的首帧图片，粘贴下面的英文提示词**。

- **首帧图片用处理过的版本。** ChatGPT 出的图是 3:2，先交给我，我用 `doc_look.py` 处理成 16:9 的纪录片底片（`film/dry/keyframes/` 里的 `.jpg`），再拿去 Grok。处理好的图已经裁成 16:9，Grok 出来的视频也是 16:9。
- **每条生成 3 到 4 次**，挑动作最自然、没有变形、物体没有穿插的一条。动作夸张、镜头乱动的版本直接淘汰。
- **生成的声音全部不用**，声音后期统一重做（见 `04-sound.md`）。
- **视频按镜头编号保存**，比如 `S04.mp4`；同一条的多个版本加后缀：`S04-2.mp4`。
- **时长**：Grok 默认长度就够的镜头直接生成。标着"需要 10 秒以上"的，有两种做法：用 Grok 的"延长"功能接着生成；或者拆成两条，在动作经过的时候接上（每条都写了接点）。
- **"剪后"** 是剪辑时实际用的长度，生成的片段比它长没关系。

**现在就能做的 4 条**：S04（BALCONY-MASTER.jpg）、S10、S12、S18。

---

## INSTRUCTIONS FOR GROK

This is the shot list for an observational documentary called DRY, about a rainy mountain county town in northeast Yunnan. The user uploads a first-frame image whose file name starts with a shot ID (for example S04). Find that ID below and animate the image using exactly that prompt. Keep the image's composition, objects, people and light unchanged.

Every clip must look like real documentary footage: a locked-off tripod camera unless the prompt says otherwise, real-time speed with no slow motion, natural unhurried movement, people unaware of the camera and not acting, no cinematic camera moves, no zoom, no cuts. Do not add music, captions, text or logos.

---

## 序与一月

### S03｜穿云（片中 0:10.5–0:15）｜剪后 4.5 秒
上传：`S03.jpg`
```
Slow, steady drone descent straight down into a flat layer of grey-white cloud, real-time, no speed ramp. The cloud texture drifts slowly; after about two seconds the frame becomes a uniform pale grey-white inside the cloud. No sunlight, no lens flare, no text.
```

### S04｜一月·衬衫滴水（0:15–0:24）｜剪后 9 秒
上传：`BALCONY-MASTER.jpg`
```
Locked-off tripod shot, completely still camera. Real-time speed, no slow motion. Only this happens: a single water drop slowly forms on the hem of the pale blue shirt and falls into the red basin below; about two seconds later a second drop forms and falls. Light drizzle beyond the railing, fog drifting slightly over the town and the hills. The shirt does not move. No camera movement, no zoom, no cuts, no text.
```
> 剪辑时，第一滴落盆的那一帧对准片中 0:16.2（片名出现），第二滴对准 0:18.6。

### S05｜一月·雾城（0:24–0:31）｜剪后 7 秒
上传：`S05.jpg`（重做蜂窝煤之后的版本）
```
Locked-off tripod shot, completely still camera. Real-time speed. Light drizzle; water drips from the eave onto the stack of coal briquettes in the foreground; steam rises from the breakfast stall's bamboo steamers; a motorcycle with a full rain cape rides slowly down the wet street; people with umbrellas walk at a normal pace; fog drifts across the far buildings and hills. No camera movement, no zoom, no cuts, no text.
```

## 二月到六月

### S06｜二月·四秒太阳（0:31–0:40）｜剪后 9 秒
上传：`S06.jpg`（阳台改图 E1）
```
Locked-off tripod shot, completely still camera. Real-time speed. Only this happens: the fog thins; after about two seconds a low beam of pale sunlight slides in from the left and falls on the pale blue shirt; thin white steam rises from the shirt; across the street two or three people open their windows and push laundry poles out; after about four seconds the fog closes in again, the sunlight goes, the steam stops and the poles are pulled back in. No camera movement, no zoom, no cuts, no text.
```
> 太难一次成功时，拆成两条：第一条"雾散、阳光照上衬衫、冒白汽"，第二条从白汽最浓的那一刻开始"雾合上、白汽停"，在白汽最浓处接上。邻居推晾衣杆这个动作做不好，可以只让邻居推开窗探头。

### S07｜春天·云瀑（0:40–0:48）｜剪后 8 秒
上传：`S07.jpg`
```
Locked-off tripod time-lapse of a mountainside: low cloud pours slowly over the ridge and flows down the slope like a waterfall; for about one and a half seconds a patch of pale sunlight sweeps across the slope and is swallowed again by cloud; plastic mulch film on the fields shimmers slightly. Natural time-lapse, no camera movement, no zoom, no text.
```

### S08｜六月·菜市场泻水（0:48–0:56）｜剪后 8 秒
上传：`S08.jpg`
```
Locked-off tripod shot, real-time speed. Heavy rain on a covered street market. In the foreground a stall keeper pushes up the sagging plastic awning with a bamboo pole and a sheet of water pours off its edge onto the street; passers-by with umbrellas keep walking and step around the puddle; about three seconds later, further down the same row, another stall keeper does the same and another sheet of water pours down. Nobody reacts dramatically. No camera movement, no zoom, no cuts, no text.
```
> 液体最容易出错，多生成几次挑最好的 8 秒。实在不行用备选：只拍两处棚边持续往下泻水，不出现顶棚的动作。

### S09｜六月·雾进堂屋（0:56–1:04）｜剪后 8 秒
上传：`S09.jpg`
```
Locked-off tripod shot, real-time speed. Fog flows slowly in through the open double doors, low along the concrete floor, over the threshold, around the legs of the small square table and the thermos flask. The old man stays asleep on the bamboo recliner and barely moves; the television flickers. No camera movement, no zoom, no cuts, no text.
```

## 七月底到八月

### S10｜辣椒坡（1:04–1:12）｜剪后 8 秒
上传：`S10.jpg`
```
Locked-off tripod shot, real-time speed. Cloud shadows drift slowly across the chili slopes; the pickers bend and pick at a normal working pace, each moving a little; leaves stir in a light breeze. No camera movement, no zoom, no cuts, no text.
```

### S11｜八月·衬衫干了（1:12–1:21）｜剪后 9 秒
上传：`S11.jpg`（阳台改图 E2）
```
Locked-off tripod shot, completely still camera. Real-time speed. Only this happens: a warm breeze lifts the dry pale blue shirt so it sways gently on its hanger for the first time; the red chilies on the bamboo tray stay still; on the opposite roofs two or three small people turn over quilts and trays; far behind the roofs the dark towering cloud grows slowly taller. No camera movement, no zoom, no cuts, no text.
```

### S12｜雨墙推过坝子（1:21–1:31）｜剪后 10 秒｜需要 10 秒以上
上传：`S12.jpg`
```
Locked-off tripod shot on a hilltop, real-time speed. The dark storm cloud presses forward over the basin and the grey wall of rain advances steadily toward the camera, swallowing the far part of the town; the sunlit area in the foreground shrinks as the cloud shadow moves across the roofs; the corn leaves in the foreground start to move in the rising wind. No lightning. No camera movement, no zoom, no cuts, no text.
```
> 只有一条 6–8 秒时，用"延长"接到 10 秒；或者拆成两条，第二条从雨幕盖住城中心的那一刻开始，在雨幕边缘经过画面中线时接上。

### S13｜航拍全城抢收（1:31–1:43）｜剪后 12 秒｜需要 10 秒以上
上传：`S13.jpg`
```
Slow, steady drone drift from left to right at about 60 degrees down over the town roofs, real-time, no speed ramp. Dozens of tiny people hurry to fold quilts and carry bamboo trays of chilies and heaps of corn into the stairwell huts on the roofs. From the left edge a grey curtain of heavy rain advances across the roofs; behind it the roofs are dark, wet and empty; ahead of it people are still gathering things. No cuts, no text.
```
> 备选 A：拆成两条硬切，"抢收"7 秒 + "雨后空屋顶"5 秒（第二条用同一张图，提示词改成 `The roofs are now empty, dark and wet under heavy rain; the drone keeps drifting slowly to the right.`）。备选 B：只生成抢收，雨线在剪辑时用雨幕素材叠上去。

### S14｜八月·先抢辣椒（1:43–1:53）｜剪后 10 秒｜全片最重要的笑点
上传：`S14.jpg`（阳台改图 E3）
```
Locked-off tripod shot, completely still camera. Real-time speed. Only this happens: a gust makes the dry shirt flap; a woman in a short-sleeved floral blouse comes out of the doorway on the right, walks past the shirt to the railing ledge, lifts the bamboo tray of red chilies with both hands and carries it back past the shirt into the house without touching the shirt; then heavy rain sweeps across the street, hits the building opposite first, then the balcony; within two seconds the shirt is soaked, dark and clinging. Rain keeps falling. No camera movement, no zoom, no cuts, no text.
```
> 这条一次很难成功。备选写法（更容易生成）：女人一进画面就已经端着竹匾，拿起来的动作发生在画外，只从衬衫旁边走过一次：
> ```
> Locked-off tripod shot, completely still camera. Real-time speed. A gust makes the dry shirt flap; a woman in a short-sleeved floral blouse, already holding a bamboo tray of red chilies with both hands, walks quickly from the railing past the shirt and through the doorway into the house, without touching the shirt; heavy rain then sweeps across the street, hits the building opposite, then the balcony; within two seconds the shirt is soaked, dark and clinging. No camera movement, no cuts, no text.
> ```
> 还不行就拆成两条：第一条只做"女人端着竹匾走进屋"，第二条用同一张图（竹匾已经不在台面上）只做"大雨扫过来、衬衫湿透"。

## 十月到十二月

### S15｜十月·吹风机（1:53–2:01）｜剪后 8 秒
上传：`S15.jpg`（阳台改图 E4）
```
Locked-off tripod shot, completely still camera. Real-time speed. Only this happens: the man sitting on the blue plastic stool keeps the hair dryer pointed at the shirt the whole time; the shirt hem and the string of chilies beside it flutter in its airflow; steady rain falls beyond the railing; drops fall from the shirt into the red basin. The man does not move otherwise. No camera movement, no zoom, no cuts, no text.
```

### S16｜十二月·凝冻（2:01–2:12）｜剪后 11 秒｜需要 10 秒以上
上传：`S16.jpg`
```
Slow, steady drone push forward over a frozen mountain landscape, real-time, no speed ramp. Every branch, blade of grass and power line is coated in ice; a winding road runs through the white; one car with its headlights on drives slowly along it. Flat grey light, a little freezing drizzle. No cuts, no text.
```
> 延长到 11 秒，或拆成两条在车灯经过树后的时候接上。

### S17｜十二月·冻成板（2:12–2:18）｜剪后 6 秒
上传：`S17.jpg`（阳台改图 E5）
```
Locked-off tripod shot, completely still camera. Real-time speed. Almost nothing moves: a few grains of freezing rain bounce on the awning and the railing; the frozen shirt stays rigid; a breath of wind does not move it. No camera movement, no zoom, no cuts, no text.
```

### S18｜冬夜·炉子上方的辣椒串（2:18–2:25）｜剪后 7 秒
上传：`S18.jpg`
```
Locked-off tripod shot, real-time speed. The blue flame flickers in the stove's fire hole; steam rises from the kettle spout; warm air from the stove makes the string of dried chilies sway very slightly; condensation runs slowly down the window. No people. No camera movement, no zoom, no cuts, no text.
```

## 第 218 个雨日的夜

### S19｜烙烤店外（2:25–2:31）｜剪后 6 秒
上传：`S19.jpg`
```
Locked-off tripod shot, real-time speed, night, rain. Rainwater runs off the tile eave in the foreground as thin streams; a person in a raincoat, seen from behind, lifts the plastic strip curtain of the shop and goes in; warm light and steam spill out; a motorcycle passes on the wet street behind. No camera movement, no zoom, no cuts, no text.
```

### S20｜瓦沟流水（2:31–2:35）｜剪后 4 秒
上传：`S20.jpg`
```
Locked-off tripod shot, real-time speed, night. Rainwater runs down the curved grey roof tiles in thin streams and drips from the eave edge. Nothing else moves. No camera movement, no zoom, no cuts, no text.
```
> 和 S21 是匹配剪辑：瓦的弧线接锅背的弧线，剪辑点放在一股水线流到边缘的那一刻。

### S21｜拱背背（2:35–2:42）｜剪后 7 秒
上传：`S21.jpg`
```
Locked-off tripod shot, real-time speed. A brush enters from the edge of the frame, wipes a circle of rapeseed oil around the top of the black dome and leaves; thin streams of oil run down the curve of the dome into the gutter; the potato slices sizzle with small bubbles; a little smoke drifts across the top. No camera movement, no zoom, no cuts, no text.
```
> 刷子的动作做不好，就去掉刷子，只保留"油顺着锅背往下流、洋芋片冒小泡"。

### S22｜雨停了（2:42–2:45）｜剪后 3 秒
上传：`S22.jpg`
```
Locked-off tripod shot, real-time speed, night. Looking out through the half-open doorway: the rain thins out; the last two or three drops fall from the eave; the puddle under the street lamp stops showing new ripples and goes still. No camera movement, no zoom, no cuts, no text.
```
> 备选：只拍瓦檐最后两滴水，两滴之间的间隔越来越长。

### S23｜干（2:45–2:49）｜剪后 4 秒｜高潮
上传：`S23.jpg`
```
Locked-off tripod shot, real-time speed. Only this happens: the owner pours one spoonful of coarse chili flakes from the steel basin into a small white dish and pauses; a faint haze of red dust hangs in the bulb light. Everything is dry: no steam, no smoke, no rain. No camera movement, no zoom, no cuts, no text.
```

### S24｜蘸（2:49–2:53）｜剪后 4 秒
上传：`S24.jpg`
```
Locked-off overhead shot, real-time speed. A pair of chopsticks picks up one browned potato slice from the griddle, presses it into the dish of coarse chili flakes so it is coated red, and lifts it out of the frame. Steam rises from the griddle. No camera movement, no zoom, no cuts, no text.
```

### S25｜阳台·夜（2:53–2:59）｜剪后 6 秒
上传：`S25.jpg`（阳台改图 E6）
```
Locked-off tripod shot, completely still camera. Real-time speed. Night rain falls through the light of the street lamp across the street; the shirt hangs limp and wet; about two seconds in, one drop forms at the hem and falls into the red basin. No camera movement, no zoom, no cuts, no text.
```
> 落盆的那一帧对准片中 2:55.0（计数器跳到 218）。

---

## 镜头清单

| 镜头 | 首帧 | 状态 |
|---|---|---|
| S03 | S03.jpg | 等生图 |
| S04 | BALCONY-MASTER.jpg | **可以开始** |
| S05 | S05.jpg | 等重做蜂窝煤 |
| S06 | S06.jpg（E1） | 等生图 |
| S07、S08、S09 | 各自首帧 | 等生图 |
| S10 | S10.jpg | **可以开始** |
| S11 | S11.jpg（E2） | 等生图 |
| S12 | S12.jpg | **可以开始** |
| S13 | S13.jpg | 等生图 |
| S14 | S14.jpg（E3） | 等生图 |
| S15 | S15.jpg（E4） | 等生图 |
| S16 | S16.jpg | 等生图 |
| S17 | S17.jpg（E5） | 等生图 |
| S18 | S18.jpg | **可以开始** |
| S19–S24 | 各自首帧 | 等生图（S21、S23 在风格测试里，还没收到） |
| S25 | S25.jpg（E6） | 等生图 |

不用 Grok 的镜头：S01 黑场、S02 卫星（已做好）、S26 事实卡、S27 产品实拍、S28 品牌卡。
