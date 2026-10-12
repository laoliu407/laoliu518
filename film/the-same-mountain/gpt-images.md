# ChatGPT 生图任务单｜《同一座山》

> **第 2 版：纪录片质感。** 第 1 版的提示词偏电影感，画出来像 AI 短剧。这一版全部按"观察式纪录片"重写。之前生成的图建议都不用，从 PART 0 重新开始。

## 给你看的用法

全部 53 张图，分 5 次做。每次都**开一个新的 ChatGPT 对话**，防止画风越跑越偏。

1. **第 0 部分（参考图）：** 新对话，上传本文件，发送：`按文件执行 PART 0`。四张参考图每张多出几版，挑最像真实照片的保存，文件名分别是 `REF-W-ELDER.png`、`REF-A-ELDER.png`、`REF-W-VILLAGE.png`、`REF-A-VILLAGE.png`。
2. **第 1 到 4 部分：** 每次新对话，上传本文件和四张参考图，发送：`按文件执行 PART 1`（2、3、4 同理）。
3. ChatGPT 每次出一张图，开头标着镜头编号。按编号保存，比如 `S04W.png`。
4. 满意就回复 `下一个`；不满意就回复 `重做 S04W`，并说明哪里不对。
5. 全部做完后，把图片和 `grok-videos.md` 一起拿去 Grok 生成视频。

**怎么判断一张图合不合格：** 盖住画面里的人，问自己"这像不像《舌尖上的中国》或 BBC 纪录片里随手截的一帧？"。如果它看起来像海报、广告或者短剧剧照，就重做。重做时可以直接回复：`太像电影/广告了，更普通、更像纪录片截图`。

> 带 A 的镜头是照着前一张 W 的构图画的。W 不满意要先重做 W，再做 A。

---

## INSTRUCTIONS FOR CHATGPT

You are generating still frames for a short **observational documentary** called **THE SAME MOUNTAIN**. Every image must look like a frame grab from real documentary footage shot on location. It must never look like a movie, an advertisement, a short drama or AI art. Follow these rules for every image in this conversation.

1. **Format.** One 16:9 landscape image per reply. Start every reply with the item ID in bold, for example **S04W**.
2. **Workflow.** The user tells you which PART to run. Generate that part's items strictly in order, one image per reply, then wait. "下一个" or "next" means continue to the next item. "重做 <ID>" or "redo <ID>" means regenerate that item, applying any feedback given.
3. **Documentary house style (always apply):**
   - **Camera:** a frame from a Sony FX6 documentary camera with a 35mm or 50mm prime at f/5.6 to f/8. Deep focus. Eye level, or the natural height of a camera operator. Framing slightly imperfect, like real tripod or handheld work, never perfectly symmetrical.
   - **Light:** only the light that is really there: flat overcast daylight, mist, a small window, a bare bulb, the glow of a stove. Slightly underexposed and low contrast. Shadows are allowed to go dark. No added lights.
   - **Color:** natural, slightly muted color straight from the camera (Rec.709), with no color grading. Clothing and props are plain and faded, so the red of the chilies stands out on its own.
   - **People:** real, ordinary, unglamorous rural people: uneven sun-damaged skin, sunspots, ruddy chapped cheeks, chapped lips, untidy hair, dirt under the nails. Wrinkles are normal, not exaggerated. They are busy with their work and unaware of the camera, with neutral expressions. They never pose or look dramatic.
   - **Clothes and places:** worn, faded, patched, mismatched everyday clothes. Real lived-in places with ordinary clutter, such as plastic basins, woven sacks, rubber boots, tarps, worn tools and electric wires. Nothing looks like a costume or a film set.
   - **Texture:** mild digital noise, slight softness, honest detail. Nothing hyper-sharp or polished.
   - **Never:** cinematic look, movie or studio lighting, rim light, artificial god rays, lens flare, teal-and-orange grading, HDR, bokeh balls, extremely shallow depth of field, glossy or airbrushed skin, beauty retouching, heroic low angles, selective color, epic or fantasy mood.
4. **Lighting tags.**
   - `[DAWN]` early morning in thick mountain mist, flat grey-blue light, no sunlight, slightly underexposed
   - `[DAY]` flat overcast daylight, soft shadows
   - `[INDOOR]` dim farmhouse interior lit by a small window, the glow of the stove and sometimes a bare bulb; mixed color temperatures; corners fall into darkness
   - `[NIGHT]` a historical reenactment filmed for a documentary at night: rain, real darkness, practical lantern light or lightning flashes only
5. **References.** From PART 1 onward the user uploads four reference images. **W-ELDER** and **A-ELDER** in prompts mean exactly the women in REF-W-ELDER and REF-A-ELDER. Villages follow REF-W-VILLAGE and REF-A-VILLAGE.
6. **MIRROR items.** An item marked `MIRROR OF <ID>` must recreate image <ID>, which you generated earlier in this conversation, with the identical camera position, lens, framing, horizon line, subject position and pose, lighting direction, time of day and color. Change ONLY what the item lists. If a person appears, she is A-ELDER.
7. **EDIT items.** An item marked `EDIT OF <ID>` keeps image <ID> exactly and changes only what is listed.
8. **Never** add text, captions, labels, logos, signatures or watermarks.

---

## PART 0｜参考图 REFERENCES（4 张）

**REF-W-ELDER** `[DAY]`
Documentary environmental portrait: a 68-year-old woman farmer standing in the doorway of her rammed-earth house in a mountain village in Weixin County, northeastern Yunnan, China. Full body, eye level. She looks toward the camera with a neutral, slightly guarded expression, hands hanging at her sides. Sun-damaged uneven skin, sunspots, ruddy chapped cheeks, ordinary wrinkles, grey hair wrapped in a long black cloth head wrap (common among older rural women in southwest China). She wears a faded navy cotton jacket over a cheap patterned sweater, a stained dark apron, worn dark trousers and dusty green canvas shoes. Large knotted hands with soil under the nails. Around the door: a plastic stool, a woven polypropylene sack, a hoe leaning on the wall.

**REF-A-ELDER** `[DAY]`
Documentary environmental portrait: a 68-year-old Quechua woman farmer standing in the doorway of her adobe house in a highland community near Cusco, Peru. Full body, eye level. She looks toward the camera with a neutral, slightly guarded expression, hands at her sides. Sun-damaged uneven skin, sunspots, ruddy chapped cheeks from the altitude, ordinary wrinkles, two long grey-black braids, a dusty dark brown felt hat. She wears a worn dark brown hand-woven shawl (lliclla) over a cheap acrylic cardigan, a layered dark wool skirt, and rubber-tire sandals (ojotas) on dusty feet. Large knotted hands with soil under the nails. Around the door: a plastic bucket, a woven sack of potatoes, a hand hoe leaning on the wall.

**REF-W-VILLAGE** `[DAY]`
Documentary location photo at eye level: a small farming hamlet on a steep slope in Weixin County, northeastern Yunnan, as it really looks today. Rammed-earth and brick houses with grey tile roofs, some bare concrete walls, a solar water heater on one roof, electric wires on wooden poles, strings of dried corn under the eaves, terraced potato fields on steep slopes, limestone mountains in low cloud. No people.

**REF-A-VILLAGE** `[DAY]`
Documentary location photo at eye level: a small Quechua farming community on a steep slope near Cusco, Peru, as it really looks today. Adobe and stone houses with clay tile and corrugated metal roofs, electric wires on wooden poles, old stone terraces planted with potatoes, high grassland, snow-capped peaks partly in cloud, a few llamas grazing. No people.

---

## PART 1｜序 + 第一幕（19 张）

Rule for PART 1: every A image before S12A must hide anything that reveals the Andes. No snow peaks, no llamas, no felt hats, no colorful potatoes, no visible faces.

**S02W** `[DAWN]`
Very wide shot from a hillside, tripod, plain and still: limestone mountain ridges in Weixin County, northeastern Yunnan, partly hidden in thick morning cloud that fills the valley; terraced fields faintly visible on the lower slopes.

**S03A** `MIRROR OF S02W`
Change only: the ridges are Andean mountains near Cusco, Peru, with grassy slopes and faint old stone terraces. Any snow peaks stay completely hidden in cloud.

**S04W** `[DAWN]`
High-angle view of steep earthen terraced potato fields on a Yunnan mountainside, mist drifting down across the terrace edges.

**S04A** `MIRROR OF S04W`
Change only: the terraces are old dry-stone terraces (andenes) on a steep Andean slope, planted with potatoes.

**S05W** `[DAWN]`
Inside a dark rammed-earth farmhouse, low on the earthen floor, looking toward an old wooden plank door being pushed open from inside. Grey-blue daylight and mist come in. A few ordinary things sit in the shadows: a plastic basin, a sack. Only one hand is visible on the edge of the door.

**S05A** `MIRROR OF S05W`
Change only: rough adobe brick walls of an Andean farmhouse; the door is old weathered wood with a simple wooden latch; the hand is A-ELDER's.

**S06W** `[DAWN]`
From behind, at a distance, tripod at eye level: W-ELDER walks up a narrow muddy path into thick mist carrying a bamboo back-basket. Her figure is soft and grey in the mist.

**S06A** `MIRROR OF S06W`
Change only: the woman is A-ELDER carrying a large bundle wrapped in a dark woven shawl (lliclla) tied across her shoulders, her head covered with a dark shawl against the cold so no hat is visible. Her outline in the mist must match S06W as closely as possible.

**S07W** `[DAWN]`
Close-up from slightly below: W-ELDER's weathered hands gripping a worn wooden hoe handle, raised to swing, grey misty sky behind.

**S07A** `[DAWN]` (not a mirror, generate directly)
Close-up at ground level in an Andean potato field: a hand hoe biting into dark wet soil, clods breaking apart, the wooden handle and A-ELDER's hands at the top of frame.

**S08W** `[DAWN]`
Close-up: W-ELDER's soil-caked hands pulling a cluster of small, uneven brown potatoes out of dark wet soil, roots and clumps of earth hanging off.

**S08A** `MIRROR OF S08W`
Change only: the hands are A-ELDER's. The potatoes stay plain brown.

**S09W** `[DAWN]`
A grey tile farmhouse roof in the mist, thin wood smoke rising from a short chimney pipe. Plain and still.

**S09A** `MIRROR OF S09W`
Change only: an Andean adobe farmhouse with a clay tile roof, keeping the same roofline shape and the same smoke position.

**S10W** `[DAWN]`
Top-down view: dried red chilies spread out on an old woven bamboo mat in a farmhouse yard, a few dead leaves and bits of dirt among them, a worn concrete edge visible.

**S10A** `MIRROR OF S10W`
Change only: an old woven reed mat on packed earth; the chilies are dried ají panca peppers, longer, darker red and wrinkled.

**S11W** `[DAWN]`
Wide shot from behind, tripod at eye level: W-ELDER stands near the center of frame at the edge of a terrace, stretching her back after work, looking out over a valley full of mist. Her bamboo basket sits on the ground beside her.

**S11A** `MIRROR OF S11W`
Change only: the woman is A-ELDER with her shawl-wrapped bundle on the ground beside her and her head covered with a dark shawl. The distant mountains stay completely hidden in mist.

**S12A** `EDIT OF S11A`
Change only: the mist has thinned, and snow-capped Andean peaks are visible in the far distance. A scruffy brown-and-white llama stands a few meters to her right, side-on to the camera. Keep everything else exactly the same.

---

## PART 2｜第二幕（15 张）

S14 and S19 will be shown in split screen: keep the subject in the center of frame.

**S14W** `[DAY]`
Close-up, subject centered: W-ELDER's dirty hands holding a few freshly dug yellow potatoes with soil stuck to them, field soil behind.

**S14A** `MIRROR OF S14W`
Change only: the hands are A-ELDER's, holding native Andean potatoes in mixed colors and odd shapes: purple, black, yellow, speckled. No red-skinned potatoes.

**S15W** `[INDOOR]`
Close-up inside a dark farmhouse: W-ELDER's hands pushing potatoes into hot ash and embers in a floor fire pit, a little smoke.

**S15A** `MIRROR OF S15W`, but outdoors in `[DAY]` light
Change only: an outdoor earth oven made of stacked dirt clods (huatia), hot embers inside, in a harvested field. The hands are A-ELDER's. Keep the same tight framing on the hands and embers.

**S16W** `[INDOOR]`
Close-up: dried red chilies being stirred in a blackened old iron wok over a wood fire with a wooden spatula, a little smoke.

**S16A** `MIRROR OF S16W`
Change only: a shallow unglazed clay pan (callana) over a small wood fire; the ají peppers are stirred with a short stick.

**S17a** `[INDOOR]`
Close-up: a wooden pestle pounding toasted dried chilies in a heavy, worn stone mortar, flakes jumping. Window light from the left.

**S17b** `[INDOOR]` (generate directly; same scale and light as S17a)
Close-up: A-ELDER's hands rocking a heavy curved stone on a flat grinding stone (batán), crushing red ají peppers into a rough paste. Window light from the left.

**S17c** `[INDOOR]`
Very close: coarse chili flakes and seeds in the bottom of a stone mortar, fine red dust in the air catching the window light.

**S17d** `[INDOOR]`
Very close: rough red chili paste under a grinding stone, seeds and skins visible.

**S17e** `[INDOOR]`
Fine red chili dust drifting in the window light of a dim room, dark background.

**S18W** `[INDOOR]`
Tight close-up of W-ELDER's eyes and upper face, squinting slightly in wood smoke, real sun-damaged skin, dim window light from the left.

**S18A** `MIRROR OF S18W`
Change only: the face is A-ELDER's, with the same framing, the same squint and the same light.

**S19W** `[INDOOR]`
Close-up, subject centered: W-ELDER's hands breaking open a roasted potato with charred, ash-covered skin, steam coming out.

**S19A** `MIRROR OF S19W`
Change only: the hands are A-ELDER's; the potato is a purple-skinned native potato from an earth oven, with pale yellow flesh.

---

## PART 3｜四百年前（5 张）

This part is a historical reenactment, but it must still look like a documentary reenactment, not a blockbuster.

**S21** `[NIGHT]`
Historical reenactment filmed for a documentary: a 16th-century Spanish galleon in a storm at night on the open sea, heavy rain, large dark waves, a lightning flash lighting up the ship. Realistic and unstylized.

**S22** `[NIGHT]`
Historical reenactment filmed for a documentary, floor-level close-up inside the dark hold of a wooden ship at night: a swinging oil lantern, wet planks, a torn burlap sack with brown potatoes spilling out, and one dried red chili pod among them.

**S23** (still image only)
An old hand-drawn parchment map of the Pacific Ocean, photographed flat like an archive scan. Pacific-centered projection with East Asia on the left edge and South America on the right edge, sepia ink coastlines, a faded compass rose, stains and creases. Absolutely no text, labels or lettering of any kind.

**S24a** `[NIGHT]`
A real photograph of a lightning bolt in a black night sky over the sea.

**S24b** `[INDOOR]`
Close-up at table height: charcoal catching fire in a small brazier under a shallow round cast-iron griddle (laoguo), flames flaring up around its rim, dark farmhouse interior.

---

## PART 4｜第三幕（10 张）

**S25W** `[INDOOR]`
Top-down view: a round shallow cast-iron griddle (laoguo) with a little oil on a charcoal brazier in the middle of a worn wooden table. Potato slices are being placed on it with chopsticks, sizzling and steaming. Around it sit a few everyday things: a small dish, a chipped bowl, a thermos.

**S25A** `MIRROR OF S25W`
Change only: a round shallow unglazed clay pan (callana) on a small clay stove; pieces of purple and yellow native potato are turned by A-ELDER's fingers instead of chopsticks; around it sit a plastic plate and a tin cup.

**S26W** `[INDOOR]`
Close-up: a small chipped white ceramic dish of coarse dark-red chili powder with visible flakes and seeds on a worn wooden table, the griddle slightly soft in the background.

**S26A** `MIRROR OF S26W`
Change only: a small rough stone bowl of coarse red chili sauce (uchucuta); the clay pan is slightly soft in the background.

**S27W** `[INDOOR]`
Close-up: chopsticks pressing a browned potato slice into the dish of coarse chili powder, granules sticking to it.

**S27A** `[INDOOR]` (not a mirror, generate directly)
Close-up: A-ELDER's fingers lifting a roasted potato piece out of a stone bowl of rough red chili sauce.

**S28W** `[INDOOR]`
Medium shot at seated eye level in a dim farmhouse: W-ELDER sits at the left end of a long worn wooden table, turned toward the right of the frame, the iron griddle in front of her. She pushes a small dish of chili powder toward the right. The table edge runs across the lower third and continues off the right edge of frame. Behind her, a small window shows misty limestone mountains at dusk; a bare bulb hangs above. Keep her in the left-center part of the frame.

**S28A** `MIRROR OF S28W`, flipped horizontally
Recreate S28W as a horizontal mirror image: A-ELDER sits at the RIGHT end of the table, turned toward the left. Replace the iron griddle with a clay pan, and the dish with a small stone bowl of chili sauce that she pushes toward the left. The walls are adobe; the window behind her shows snow-capped Andean peaks at dusk; a bare bulb hangs above. The table edge stays at exactly the same height as in S28W.

**S29** `[INDOOR]` (use S28W and S28A as references)
One continuous wide image at seated eye level: a single long worn wooden table runs across the whole frame. The left half of the room is the Yunnan farmhouse from S28W (rammed-earth wall, small window with misty limestone mountains); the right half is the Andean adobe room from S28A (adobe wall, small window with snow-capped peaks). The two halves join at the center with no visible line. W-ELDER sits at the left end and A-ELDER at the right end, facing each other along the table, an iron griddle on the left and a clay pan on the right, both steaming. A bare bulb hangs above each end.

**S30** `[DAY]`
Drone shot at dusk under an overcast sky: one continuous mountain ridge runs across the frame. The left half is the karst mountains of northeastern Yunnan, with terraced fields and small villages with rising smoke. It blends into the right half, the high Andes, with stone terraces, small adobe villages and snow peaks. Real-looking, muted colors, not fantasy.
