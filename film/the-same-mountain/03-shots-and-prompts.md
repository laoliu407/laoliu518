# 03 分镜与提示词

## 怎么用这份文件

> **注意：本文件里的提示词是第 1 版（电影感），已经过时，不要再用。** 生成时请用按纪录片质感重写的第 2 版任务单：[gpt-images.md](gpt-images.md)（ChatGPT 生图）和 [grok-videos.md](grok-videos.md)（Grok 生视频）。本文件只保留作分镜和剪辑说明的参考，比如 S13 画面裂开、S23 古地图动画、S24 闪电变成火的剪法。

**ChatGPT 生首帧：**
1. 开一个新会话，先粘贴下面的"会话设定"，并附上四张参考图（W-ELDER、A-ELDER、W-VILLAGE、A-VILLAGE，生成方法见 02 文件）。
2. 每个镜头先粘贴 **首帧 W**，生成 3 到 4 张，挑一张。
3. 把选中的 W 图片发回给 ChatGPT，粘贴"镜像模板"，并把 `{替换内容}` 换成该镜头的 **镜像 A** 内容。

**Grok 生视频：**
上传首帧，粘贴该镜头的 **视频**。同组的 W 和 A 用同一段提示词。生成的声音全部不用。

一个会话只做一幕，做完开新会话，重新粘贴设定。

---

## 会话设定（每个新会话先粘贴这段）

```
You are the image generator for a short film called THE SAME MOUNTAIN. For every image I request in this conversation:

1. Output a 16:9 landscape photograph.
2. House style: cinematic documentary realism, large-format digital cinema look, subtle anamorphic lens character, natural available light only, muted earthy palette of slate grey, moss green, ochre and charcoal. Chili red is the ONLY saturated color allowed in any image. Fine 35mm film grain, shallow depth of field. Keep all key elements inside the central horizontal band so the image survives a 2.39:1 crop. Authentic, dignified portrayal of rural mountain life, never touristic or staged.
3. Lighting tags:
   [DAWN] = pre-dawn blue hour, dense mountain fog, soft diffuse light, low contrast, cool tones
   [DAY] = overcast high-altitude daylight, soft even shadows, neutral tones
   [FIRE] = evening interior lit only by firelight and one small window, warm amber glow, deep soft shadows
   [NIGHT] = night storm, cold blue-black palette, lightning or a single lantern as the only strong light
4. W-ELDER must exactly match attached image 1. A-ELDER must exactly match attached image 2. W-VILLAGE matches image 3. A-VILLAGE matches image 4.
5. Never add text, captions, logos, signatures or watermarks.

Reply only with the image.
```

## 镜像模板（出 A 版时用）

```
Use the image I just sent as an exact layout reference. Create a new photograph with the identical camera position, lens, framing, horizon line, subject position and pose, motion direction, lighting direction, time of day and color grade. Change ONLY the following: {替换内容}. If a person appears, she must be A-ELDER. Keep everything else identical.
```

---

## 序

### S01｜黑场｜0:00–0:05
不需要生成。见 04 文件的声音设计。

### S02W / S03A｜山脊｜W 0:05–0:11 · A 0:11–0:19
云海里浮现的山脊。两个镜头之间是一个"看不见的剪辑"：剪辑时在切点叠一层雾素材，遮住切点。S03A 上叠字幕"一座山"。

首帧 W：
```
Extreme wide shot: a jagged limestone mountain ridge in the Wumeng Mountains of northeastern Yunnan slowly emerging from a sea of clouds, layered ridges fading into the fog behind it, faint terraced fields on the lower slopes. [DAWN]
```

镜像 A（替换内容）：
```
replace the limestone ridge with a rugged Andean mountain ridge near Cusco, Peru, with grassy slopes and faint ancient stone terraces; any snow peaks must stay completely hidden in the fog
```

视频（W/A 共用；S03A 生成后放慢到 75% 速度，得到 8 秒）：
```
Very slow push-in. Fog drifts steadily from right to left across the ridge, clouds roll gently below. Nothing else moves. Steady camera, realistic physics, no morphing, no text. 6 seconds.
```

---

## 第一幕 一座山

### S04｜雾流梯田｜W 0:19–0:22 · A 0:22–0:25

首帧 W：
```
High-angle wide shot of curved earthen terraced fields on a steep mountainside in northeastern Yunnan, rows of potato plants, a river of fog flowing slowly down over the terrace edges. [DAWN]
```

镜像 A：
```
replace the earthen terraces with ancient Inca dry-stone terraces (andenes) on a steep Andean slope with rows of potato plants; no snow peaks, no llamas visible
```

视频：
```
Locked-off camera. The fog flows slowly downhill from the top left to the bottom right over the terrace edges. Realistic physics, no morphing, no text. 5 seconds.
```

### S05｜推门｜W 0:25–0:27 · A 0:27–0:29

首帧 W：
```
Interior of a dark rammed-earth farmhouse, camera low on the earthen floor, looking toward an old wooden plank door being pushed open from inside. Cold blue dawn light and fog spill into the dark room. Only the silhouette of one weathered hand on the door edge is visible. [DAWN]
```

镜像 A：
```
replace the rammed-earth walls with rough adobe brick walls of an Andean farmhouse; the door is old weathered wood with a simple wooden latch; the hand belongs to A-ELDER
```

视频：
```
The door swings slowly outward, a wedge of blue light spreads across the earthen floor, dust motes float in the beam. Static camera, realistic physics, no morphing, no text. 4 seconds.
```

### S06｜背影入雾｜W 0:29–0:32 · A 0:32–0:35
两个剪影的轮廓必须几乎一样，观众才不会察觉换了地方。

首帧 W：
```
Wide shot from behind: W-ELDER carrying a cone-shaped bamboo back-basket walks up a narrow dirt path into dense fog. She is a soft dark silhouette; the path rises to the center of frame between dark potato fields. [DAWN]
```

镜像 A：
```
the woman is A-ELDER carrying a large bundle wrapped in a dark woven shawl (lliclla) tied across her shoulders, her head covered with a dark shawl against the cold so no hat is visible; her silhouette outline should match the original as closely as possible
```

视频：
```
Static camera. She walks slowly away up the path and gradually dissolves into the fog. Natural walking motion, realistic physics, no morphing, no text. 5 seconds.
```

### S07｜锄头（动作接动作）｜W 0:35–0:37 · A 0:37–0:39
这一组不是镜像，是动作衔接：W 挥下，A 落地。剪辑时，W 锄头离开画面下沿的那一帧，接 A 锄头从画面上沿进入的那一帧。A 直接用文字生成，不用镜像模板。

首帧 W：
```
Low-angle close-up against a foggy grey sky: two weathered hands (W-ELDER) gripping a long wooden hoe handle raised high overhead, the iron blade at the top of its swing, about to come down. [DAWN]
```

视频 W：
```
The hoe swings down powerfully and exits the bottom of frame, slow motion. Static camera, realistic physics, no warping hands, no text. 2 seconds.
```

首帧 A（直接生成）：
```
Ground-level extreme close-up in an Andean potato field: an iron hoe blade slamming into dark wet soil, clods of earth bursting toward the camera, the wooden handle and A-ELDER's hands entering from the top of frame. [DAWN]
```

视频 A：
```
The hoe blade enters from the top of frame and slams into the soil; dark earth and droplets explode upward in extreme slow motion. Static camera, realistic physics, no text. 3 seconds.
```

### S08｜拔洋芋｜W 0:39–0:41 · A 0:41–0:43

首帧 W：
```
Extreme close-up: two weathered, soil-stained hands (W-ELDER) pulling a cluster of brown-skinned potatoes out of dark moist soil, fine roots and crumbs of earth falling away. [DAWN]
```

镜像 A：
```
the hands belong to A-ELDER; the potatoes are also plain brown-skinned, no colorful varieties
```

视频：
```
The hands lift the potato cluster up out of the soil; earth falls away in slow motion. Static camera, realistic physics, no warping hands, no text. 4 seconds.
```

### S09｜炊烟｜W 0:43–0:46 · A 0:46–0:49

首帧 W：
```
Wide shot: the grey clay-tile roof of a mountain farmhouse half hidden in fog, a thin column of wood smoke rising straight up from the roof, a dark ridgeline behind. [DAWN]
```

镜像 A：
```
replace the house with an Andean adobe farmhouse with a clay-tile roof; keep the same roofline shape and the same smoke position
```

视频：
```
The smoke rises slowly and bends gently to the left; fog drifts behind the house. Static camera, realistic physics, no morphing, no text. 4 seconds.
```

### S10｜晒辣椒，全片第一抹红｜W 0:49–0:52 · A 0:52–0:55

首帧 W：
```
Overhead shot: hundreds of dried red chilies spread out to dry on a large woven bamboo mat in a farmhouse courtyard, thin morning fog, the edges of the mat and grey flagstones visible. The chili red is the only vivid color in the frame. [DAWN]
```

镜像 A：
```
replace the bamboo mat with a large woven reed mat on packed earth in an Andean courtyard; the chilies are dried red ají panca peppers, longer, deep red and wrinkled
```

视频：
```
Very slow overhead push-in; the fog thins slightly; a faint breeze lifts one edge of the mat. Realistic physics, no morphing, no text. 4 seconds.
```

### S11｜望山谷｜W 0:55–0:58 · A 0:58–1:01
S11A 的首帧还要留着，S12 揭示要用。

首帧 W：
```
Wide shot from behind: W-ELDER stands at the edge of a terrace, straightening her back and looking out over a valley filled with fog, her bamboo back-basket on the ground beside her, layered dark ridges beyond. She stands in the exact center of frame. [DAWN]
```

镜像 A：
```
the woman is A-ELDER with her shawl-wrapped bundle on the ground beside her and her head covered with a dark shawl; the distant mountains remain completely hidden in fog, no snow peaks
```

视频：
```
Static camera. She slowly straightens up and rests one hand on her lower back; fog drifts through the valley. Natural movement, realistic physics, no morphing, no text. 4 seconds.
```

---

## 揭示

### S12A｜羊驼转头｜1:01–1:07
把 S11A 的首帧发给 ChatGPT，用下面这段修改（不用镜像模板）。

首帧（在 S11A 上修改）：
```
Keep this exact image and composition. Change only: the fog has begun to clear, revealing massive snow-capped Andean peaks in the far distance, and a brown-and-white llama stands a few meters to the right of the woman, side-on to the camera. Keep the woman exactly as she is.
```

视频：
```
Wind sweeps through and clears the remaining fog, revealing the snow peaks. The llama slowly turns its head to look directly at the camera. The woman stays completely still. Static camera, realistic physics, no morphing, no text. 6 seconds.
```

### S13｜画面裂开｜1:07–1:11
不需要生成，剪辑完成：
1. S12A 播到最后，画面正中出现一条细竖线；
2. A 画面向右滑，变成右半屏（裁取中间一半）；
3. 左半屏滑进 S11W 的画面（同样裁取中间一半）；
4. 1:08 淡入"两座山"，坐标逐字打出（规格见 02 文件）。

---

## 第二幕 两座山

### S14｜分屏·两捧洋芋｜1:11–1:16
主体居中，剪辑时裁中间一半放进分屏。

首帧 W：
```
Close-up, subject centered: two weathered hands (W-ELDER) cupping a pile of freshly dug yellow-skinned potatoes, soil on the fingers, dark earth background. [DAY]
```

镜像 A：
```
the hands belong to A-ELDER, cupping native Andean potatoes of many colors and shapes: deep purple, black, yellow, speckled, knobby and twisted; no red-skinned potatoes
```

视频：
```
The hands slowly raise the potatoes toward the camera with a slight turn. Static camera, realistic physics, no warping hands, no text. 5 seconds.
```

### S15｜埋进火里｜W 1:16–1:19 · A 1:19–1:22

首帧 W：
```
Close-up inside a dim farmhouse: weathered hands (W-ELDER) burying potatoes into glowing embers and grey ash in a sunken indoor fire pit, wisps of smoke, firelight on the fingers, background dark and out of focus. [FIRE]
```

镜像 A：
```
replace the indoor fire pit with an outdoor Andean earth oven (huatia): a small dome of stacked dirt clods glowing orange-hot inside; the hands are A-ELDER's; keep the same tight framing so the background stays dark and out of focus
```

视频：
```
The hands push the potatoes deep into the glowing embers; sparks and ash lift into the air. Static camera, realistic physics, no warping hands, no text. 3 seconds.
```

### S16｜焙辣椒｜W 1:22–1:24 · A 1:24–1:26

首帧 W：
```
Close-up: dried red chilies being stirred with a wooden spatula in a wide black iron wok over a wood fire, thin smoke rising, the chilies beginning to darken. [DAY]
```

镜像 A：
```
replace the iron wok with a shallow unglazed clay pan (callana) over a small open fire; the chilies are dried red ají peppers stirred with a short wooden stick
```

视频：
```
The chilies are stirred and tossed; thin smoke curls upward. Static camera, realistic physics, no morphing, no text. 3 seconds.
```

### S17｜石头的鼓点（蒙太奇）｜1:26–1:40
a 和 b 必须是同样的景别（大特写），光都从左边打来。剪辑节奏见 01 文件。

S17a W 首帧：
```
Extreme close-up: a heavy wooden pestle striking down into toasted dried red chilies in a thick stone mortar, red flakes jumping on impact, dark background, hard side light from the left. [DAY]
```
S17a 视频：
```
The pestle strikes down hard twice; flakes leap and fall in slow motion. Static camera, realistic physics, no text. 3 seconds.
```

S17b A 首帧（直接生成）：
```
Extreme close-up: weathered hands (A-ELDER) rocking a heavy curved stone back and forth on a flat grinding stone (batán), crushing red ají peppers into a coarse paste, dark background, hard side light from the left. [DAY]
```
S17b 视频：
```
The curved stone rocks left and right twice, crushing the peppers; paste squeezes out at the edges. Static camera, realistic physics, no warping hands, no text. 3 seconds.
```

S17c W 首帧：
```
Macro shot: coarse chili flakes and seeds inside a stone mortar, every granule visible, a cloud of fine red dust hanging in a beam of side light. [DAY]
```
S17c 视频：
```
The red dust slowly swirls and settles; very slow push-in. Realistic physics, no text. 3 seconds.
```

S17d A 首帧（直接生成）：
```
Macro shot: bright red chili paste being pressed under a grinding stone, seeds and fibers visible, glistening texture, hard side light from the left. [DAY]
```
S17d 视频：
```
The stone slides slowly across and the paste spreads. Realistic physics, no text. 3 seconds.
```

S17e 首帧：
```
Macro shot: fine red chili dust particles floating in a single shaft of light in a completely dark room, black background.
```
S17e 视频：
```
The particles drift and glitter in the light beam, extremely slow motion. Static camera, no text. 4 seconds.
```

### S18｜第一次露脸｜W 1:40–1:43 · A 1:43–1:46

首帧 W：
```
Extreme close-up of the eyes of W-ELDER: deep wrinkles, squinting through drifting wood smoke, warm side light from the left, dark background. [DAY]
```

镜像 A：
```
the eyes are A-ELDER's, with the same framing, the same squint and the same light
```

视频：
```
She blinks once, slowly, as a wisp of smoke drifts across her face. Static camera, realistic skin, no morphing, no text. 3 seconds.
```

### S19｜分屏·掰开洋芋｜1:46–1:50

首帧 W：
```
Close-up, subject centered: weathered hands (W-ELDER) breaking open a charred roasted potato, fluffy white interior, ash on the skin, dark background. [DAY]
```

镜像 A：
```
the hands are A-ELDER's; the potato is a purple-skinned native potato roasted in an earth oven, with pale yellow flesh
```

视频：
```
The potato splits open and a burst of steam rises in slow motion. Static camera, realistic physics, no warping hands, no text. 3 seconds.
```

---

## 四百年前

> S21 和 S22 场面复杂。如果你的 ChatGPT 能用 Sora，这两个镜头建议用 Sora 生成，效果更稳。

### S20｜字幕卡｜1:51–1:54
黑场，字幕"四百年前"。不需要生成。

### S21｜风暴中的帆船｜1:54–1:59

首帧：
```
Extreme wide shot at night: a 16th-century Spanish galleon with torn sails pitching in a violent storm on the open Pacific Ocean, enormous black waves, a lightning bolt illuminating the whole sea and the ship's silhouette, sheets of rain. Epic scale. [NIGHT]
```

视频：
```
The galleon climbs a huge wave and pitches forward; lightning flashes twice; rain blows sideways. Slow push-in, realistic ocean physics, no morphing, no text. 5 seconds.
```

### S22｜船舱里的洋芋和辣椒｜1:59–2:03

首帧：
```
Inside the dark hold of a wooden galleon at night, camera at floor level: a swinging oil lantern, wet wooden planks, a burlap sack split open with brown potatoes spilling across the planks, and a single dried red chili pod lying among them. Warm lantern light against cold darkness. [NIGHT]
```

视频：
```
The ship rolls; the lantern swings and shadows sweep across the planks; the potatoes roll to the left; the chili pod tumbles and settles among them in slow motion. Realistic physics, no morphing, no text. 4 seconds.
```

### S23｜古地图航线｜2:03–2:09
只生成一张静态地图，航线和文字在剪辑软件里做（AI 生成的文字会乱码）。

首帧：
```
An antique hand-drawn parchment map of the Pacific Ocean in a Pacific-centered projection, East Asia on the left edge and South America on the right edge, sepia ink coastlines, a faded compass rose, aged paper with stains and creases, flat top-down view, even soft light. No text, no labels, no lettering of any kind.
```

剪辑：
1. 地图缓缓推近；
2. 一条墨线从南美安第斯山出发，向左划过太平洋，抵达中国西南，用 4 秒画完，线条像毛笔或钢笔手写；
3. 起点打出 `13°31′S 71°58′W`，终点打出 `27°50′N 105°03′E`，墨线中段浮出 `18,000 KM`。

### S24｜闪电变成火｜2:09–2:13

S24a 首帧：
```
Close-up: a blinding white lightning bolt striking down through black storm clouds. [NIGHT]
```
S24a 视频：
```
The bolt strikes, flashes the frame to white, then fades. No text. 2 seconds.
```

S24b 首帧（W）：
```
Close-up at table height: flames bursting to life in a charcoal brazier beneath a shallow round cast-iron griddle (laoguo), fire flaring up around its dark rim, dark farmhouse interior. [FIRE]
```
S24b 视频：
```
The flames ignite in a sudden burst, flare up around the griddle, then settle into a steady glow. Static camera, realistic fire, no text. 3 seconds.
```

剪辑：在闪电最白的那一帧，切到火苗最亮的那一帧。

---

## 第三幕 同一座山

### S25｜顶拍·烙锅｜W 2:13–2:17 · A 2:17–2:21

首帧 W：
```
Overhead shot: a round shallow cast-iron griddle (laoguo) glistening with hot oil on a charcoal brazier in the middle of a dark wooden table, slices of potato being laid onto it with chopsticks, oil sizzling and steaming. [FIRE]
```

镜像 A：
```
replace the cast-iron griddle with a round shallow unglazed clay pan (callana) on a small clay stove; chunks of purple and yellow native potato are being turned by A-ELDER's fingers instead of chopsticks
```

视频：
```
The potatoes sizzle, oil bubbles at the edges, steam rises toward the camera, a hand turns one piece. Static overhead camera, realistic physics, no warping hands, no text. 4 seconds.
```

### S26｜蘸料特写｜W 2:21–2:24 · A 2:24–2:27

首帧 W：
```
Close-up: a small white ceramic dish filled with coarse dark-red chili powder on a dark wooden table, flakes, seeds and granules clearly visible, side-lit by firelight, the glowing griddle softly out of focus behind. [FIRE]
```

镜像 A：
```
replace the ceramic dish with a small hand-carved stone bowl filled with coarse red chili sauce (uchucuta); the clay pan softly out of focus behind
```

视频：
```
Very slow push-in; steam from the griddle drifts across the frame. Realistic physics, no text. 3 seconds.
```

### S27｜蘸（动作接动作）｜W 2:27–2:29 · A 2:29–2:31
W 往下按，A 往上提。A 直接用文字生成，不用镜像模板。

首帧 W：
```
Close-up: chopsticks pressing a golden griddled potato slice into a small dish of coarse red chili powder, the granules clinging to the potato. [FIRE]
```
视频 W：
```
The chopsticks press the potato down into the chili powder, then begin to lift it, slow motion. Static camera, realistic physics, no text. 2 seconds.
```

首帧 A（直接生成）：
```
Close-up: weathered fingers (A-ELDER) lifting a roasted potato piece out of a stone bowl of red chili sauce, a drop of sauce falling. [FIRE]
```
视频 A：
```
The potato is lifted out of the sauce toward the top of frame; a drop of sauce falls back into the bowl, slow motion. Static camera, realistic physics, no warping fingers, no text. 2 seconds.
```

### S28｜分屏·来，吃｜2:31–2:38
关键镜头。两张桌子的桌沿必须在同一高度，S29 才能合成一张。

**出 A 版之前，先用手机修图把 W 首帧水平翻转**，再把翻转后的图发给 ChatGPT，套镜像模板。这样 A 版的构图天然是 W 的镜像。

首帧 W：
```
Medium shot at seated eye level in a firelit farmhouse: W-ELDER sits at the left end of a long dark wooden table, her body angled toward the right side of the frame, an iron griddle glowing in front of her. She slides a small dish of chili powder toward the right. The table edge runs horizontally across the lower third and continues off the right edge of frame. A small window behind her shows misty limestone peaks at dusk. Keep her within the left-center part of the frame. [FIRE]
```

镜像 A（发翻转后的 W 图）：
```
the woman is A-ELDER sitting at the right end of the table, angled toward the left; replace the iron griddle with a clay pan and the dish with a small stone bowl of chili sauce that she slides toward the left; replace the walls with adobe; the window behind her shows snow-capped Andean peaks at dusk; the table edge must stay at exactly the same height
```

视频 W：
```
She slides the dish forward with one hand, says softly "Lai ma, chi", and nods once. Static camera, natural movement, subtle mouth movement, no text. 4 seconds.
```

视频 A：
```
She slides the bowl forward with one hand, says softly "Hamuy, mikhuy", and nods once. Static camera, natural movement, subtle mouth movement, no text. 4 seconds.
```

> 台词声音用真人录音替换（见 04 文件）。中景画面里口型不明显，对不齐也不影响观感。

### S29｜合成一张桌子｜2:38–2:44
附上 S28 的 W、A 两张首帧作为参考。

首帧：
```
One continuous wide image at seated eye level: a single long wooden table runs across the whole frame. The left half of the room is a Yunnan farmhouse interior (rammed-earth wall, small window showing misty limestone peaks); the right half is an Andean adobe interior (adobe wall, small window showing snow-capped peaks). The two halves blend seamlessly at the center with no visible line. W-ELDER sits at the left end and A-ELDER at the right end, facing each other along the table; an iron griddle on the left and a clay pan on the right, both steaming. [FIRE]
```

视频：
```
Very slow push-in toward the center of the table. Both women stay still and look at each other. Firelight flickers; steam rises from both pans and drifts upward. Realistic physics, no morphing, no text. 6 seconds.
```

剪辑：2:38 到 2:40，S28 的中缝细线淡出，同时交叉溶解到 S29。

### S30｜同一座山（航拍）｜2:44–2:52
用 S29 结尾的热气上升填满画面，溶解进这个镜头。

首帧：
```
Aerial view at dusk: one continuous mountain ridge runs across the frame. The left half is green karst mountains of northeastern Yunnan with terraced fields and small grey-roofed villages with rising smoke; it blends seamlessly into the right half, the high Andes with stone terraces, small adobe villages and snow peaks. One unbroken ridgeline, warm golden sky, mist in the valleys. Cinematic realism, fine film grain, no text.
```

视频：
```
Slow aerial rise and pull-back; mist flows through the valleys; tiny columns of smoke rise from the villages on both sides. Smooth drone movement, realistic physics, no morphing, no text. 6 seconds.
```

---

## 尾声

### S31｜黑场字幕｜2:52–3:03
不需要生成。字幕内容和时间见 01 文件，旁白见 04 文件。

### S32｜真实产品｜3:03–3:07
**不用 AI 生成。** 用雷大卷的实拍：
- 最好：实拍视频。暗色木桌，火光侧照，一勺辣椒面倒进碗里，或热油泼下去的瞬间。
- 其次：一张高清产品照，加一个极缓的推近。

### S33｜片尾｜3:07–3:10
黑场，字幕"由雷大卷辣椒面制作"。

---

## 生成清单

| 类型 | 镜头 | 数量 |
|---|---|---|
| 镜像对 | S02/S03、S04–S06、S08–S11、S14–S16、S18、S19、S25、S26、S28 | 16 组，共 32 个 |
| 动作衔接对 | S07、S27 | 2 组，共 4 个 |
| 单镜头 | S12A、S17a–e、S21、S22、S24a、S24b、S29、S30 | 12 个 |
| 静态图 | S23 地图 | 1 张 |
| 剪辑完成 | S01、S13、S20、S31、S33 | 不需要生成 |
| 实拍 | S32 | 你来准备 |
