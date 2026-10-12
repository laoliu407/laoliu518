# ChatGPT 生图任务单｜《同一座山》

## 给你看的用法

全部 53 张图，分 5 次做。每次都**开一个新的 ChatGPT 对话**，防止画风越跑越偏。

1. **第 0 部分（参考图）：** 新对话，上传本文件，发送：`按文件执行 PART 0`。四张参考图每张多出几版，挑最好的保存，文件名分别是 `REF-W-ELDER.png`、`REF-A-ELDER.png`、`REF-W-VILLAGE.png`、`REF-A-VILLAGE.png`。
2. **第 1 到 4 部分：** 每次新对话，上传本文件和四张参考图，发送：`按文件执行 PART 1`（2、3、4 同理）。
3. ChatGPT 每次出一张图，开头标着镜头编号。按编号保存，比如 `S04W.png`。
4. 满意就回复 `下一个`；不满意就回复 `重做 S04W`，也可以说明哪里不对。
5. 全部做完后，把图片和 `grok-videos.md` 一起拿去 Grok 生成视频。

> 带 A 的镜头是照着前一张 W 的构图画的。所以 W 不满意要先重做 W，再做 A。

---

## INSTRUCTIONS FOR CHATGPT

You are the image generator for a short film called **THE SAME MOUNTAIN**. Follow these rules for every image in this conversation.

1. **Format.** One 16:9 landscape photograph per reply. Start every reply with the item ID in bold, for example **S04W**.
2. **Workflow.** The user tells you which PART to run. Generate that part's items strictly in order, one image per reply, then wait. "下一个" or "next" means continue to the next item. "重做 <ID>" or "redo <ID>" means regenerate that item, applying any feedback given.
3. **House style (always apply).** Cinematic documentary realism, large-format digital cinema look, subtle anamorphic lens character, natural available light only, muted earthy palette of slate grey, moss green, ochre and charcoal. **Chili red is the ONLY saturated color allowed in any image**: no red or pink clothing, props or backgrounds. Fine 35mm film grain, shallow depth of field. Keep all key elements inside the central horizontal band so the image survives a 2.39:1 crop. Authentic, dignified portrayal of rural mountain life, never touristic or staged.
4. **Lighting tags.**
   - `[DAWN]` pre-dawn blue hour, dense mountain fog, soft diffuse light, low contrast, cool tones
   - `[DAY]` overcast high-altitude daylight, soft even shadows, neutral tones
   - `[FIRE]` evening interior lit only by firelight and one small window, warm amber glow, deep soft shadows
   - `[NIGHT]` night storm, cold blue-black palette, lightning or a single lantern as the only strong light
5. **References.** From PART 1 onward the user uploads four reference images. **W-ELDER** and **A-ELDER** in prompts mean exactly the women in REF-W-ELDER and REF-A-ELDER. W-VILLAGE and A-VILLAGE scenes follow REF-W-VILLAGE and REF-A-VILLAGE.
6. **MIRROR items.** An item marked `MIRROR OF <ID>` must recreate image <ID>, which you generated earlier in this conversation, with the identical camera position, lens, framing, horizon line, subject position and pose, motion direction, lighting direction, time of day and color grade. Change ONLY what the item lists. If a person appears, she is A-ELDER.
7. **EDIT items.** An item marked `EDIT OF <ID>` keeps image <ID> exactly and changes only what is listed.
8. **Never** add text, captions, labels, logos, signatures or watermarks.

---

## PART 0｜参考图 REFERENCES（4 张）

For PART 0 only, ignore rule 5 and use a neutral grey studio background.

**REF-W-ELDER**
Character reference sheet, photorealistic: a 68-year-old woman farmer from the Wumeng Mountains of northeastern Yunnan, China. Sun-darkened skin, deep wrinkles, high cheekbones, calm tired eyes, grey hair wrapped in a long black cloth head wrap wound like a turban (common in rural southwest China), faded navy-blue cotton jacket with cloth knot buttons, dark apron, dark trousers, worn green canvas shoes. Large knotted soil-stained hands. Five panels on a neutral grey background: front view, three-quarter view, profile, back view, and a close-up of her hands. Soft natural light, documentary realism.

**REF-A-ELDER**
Character reference sheet, photorealistic: a 68-year-old Quechua woman farmer from the highlands near Cusco, Peru. Sun-darkened skin, deep wrinkles, high cheekbones, calm tired eyes, two long grey-black braids, a dark brown wide-brimmed felt hat, a dark brown hand-woven wool shawl (lliclla) with a subtle muted pattern, layered dark wool skirt (pollera), worn rubber-tire sandals (ojotas). Large knotted soil-stained hands. Five panels on a neutral grey background: front view, three-quarter view, profile, back view, and a close-up of her hands. Soft natural light, documentary realism, muted colors only.

**REF-W-VILLAGE**
Establishing reference photo: a small farming hamlet in the Wumeng Mountains of northeastern Yunnan, China. Rammed-earth and stone houses with grey clay tile roofs, old wooden plank doors, strings of dried corn under the eaves, steep earthen terraced potato fields, jagged limestone karst peaks, low clouds clinging to the ridges. Overcast natural light, documentary realism, no people.

**REF-A-VILLAGE**
Establishing reference photo: a small Quechua farming hamlet in the Andean highlands near Cusco, Peru. Adobe and fieldstone houses with clay tile roofs, old wooden doors, ancient dry-stone Inca terraces planted with potatoes, high grassland, snow-capped peaks partly hidden in cloud, a few llamas grazing. Overcast natural light, documentary realism, no people.

---

## PART 1｜序 + 第一幕（19 张）

Rule for PART 1: every A image before S12A must hide anything that reveals the Andes. No snow peaks, no llamas, no felt hats, no colorful potatoes, no visible faces.

**S02W** `[DAWN]`
Extreme wide shot: a jagged limestone mountain ridge in the Wumeng Mountains of northeastern Yunnan slowly emerging from a sea of clouds, layered ridges fading into the fog behind it, faint terraced fields on the lower slopes.

**S03A** `MIRROR OF S02W`
Change only: replace the limestone ridge with a rugged Andean mountain ridge near Cusco, Peru, with grassy slopes and faint ancient stone terraces. Any snow peaks stay completely hidden in the fog.

**S04W** `[DAWN]`
High-angle wide shot of curved earthen terraced fields on a steep mountainside in northeastern Yunnan, rows of potato plants, a river of fog flowing slowly down over the terrace edges.

**S04A** `MIRROR OF S04W`
Change only: replace the earthen terraces with ancient Inca dry-stone terraces (andenes) on a steep Andean slope with rows of potato plants.

**S05W** `[DAWN]`
Interior of a dark rammed-earth farmhouse, camera low on the earthen floor, looking toward an old wooden plank door being pushed open from inside. Cold blue dawn light and fog spill into the dark room. Only the silhouette of one weathered hand on the door edge is visible.

**S05A** `MIRROR OF S05W`
Change only: replace the rammed-earth walls with rough adobe brick walls of an Andean farmhouse; the door is old weathered wood with a simple wooden latch; the hand belongs to A-ELDER.

**S06W** `[DAWN]`
Wide shot from behind: W-ELDER carrying a cone-shaped bamboo back-basket walks up a narrow dirt path into dense fog. She is a soft dark silhouette; the path rises to the center of frame between dark potato fields.

**S06A** `MIRROR OF S06W`
Change only: the woman is A-ELDER carrying a large bundle wrapped in a dark woven shawl (lliclla) tied across her shoulders, her head covered with a dark shawl against the cold so no hat is visible. Her silhouette outline must match S06W as closely as possible.

**S07W** `[DAWN]`
Low-angle close-up against a foggy grey sky: two weathered hands (W-ELDER) gripping a long wooden hoe handle raised high overhead, the iron blade at the top of its swing, about to come down.

**S07A** `[DAWN]` (not a mirror, generate directly)
Ground-level extreme close-up in an Andean potato field: an iron hoe blade slamming into dark wet soil, clods of earth bursting toward the camera, the wooden handle and A-ELDER's hands entering from the top of frame.

**S08W** `[DAWN]`
Extreme close-up: two weathered, soil-stained hands (W-ELDER) pulling a cluster of brown-skinned potatoes out of dark moist soil, fine roots and crumbs of earth falling away.

**S08A** `MIRROR OF S08W`
Change only: the hands belong to A-ELDER. The potatoes stay plain brown-skinned.

**S09W** `[DAWN]`
Wide shot: the grey clay-tile roof of a mountain farmhouse half hidden in fog, a thin column of wood smoke rising straight up from the roof, a dark ridgeline behind.

**S09A** `MIRROR OF S09W`
Change only: replace the house with an Andean adobe farmhouse with a clay-tile roof, keeping the same roofline shape and the same smoke position.

**S10W** `[DAWN]`
Overhead shot: hundreds of dried red chilies spread out to dry on a large woven bamboo mat in a farmhouse courtyard, thin morning fog, the edges of the mat and grey flagstones visible. The chili red is the only vivid color in the frame.

**S10A** `MIRROR OF S10W`
Change only: replace the bamboo mat with a large woven reed mat on packed earth in an Andean courtyard; the chilies are dried red ají panca peppers, longer, deep red and wrinkled.

**S11W** `[DAWN]`
Wide shot from behind: W-ELDER stands at the edge of a terrace, straightening her back and looking out over a valley filled with fog, her bamboo back-basket on the ground beside her, layered dark ridges beyond. She stands in the exact center of frame.

**S11A** `MIRROR OF S11W`
Change only: the woman is A-ELDER with her shawl-wrapped bundle on the ground beside her and her head covered with a dark shawl. The distant mountains stay completely hidden in fog.

**S12A** `EDIT OF S11A`
Change only: the fog has begun to clear, revealing massive snow-capped Andean peaks in the far distance, and a brown-and-white llama stands a few meters to the right of the woman, side-on to the camera. Keep the woman exactly as she is.

---

## PART 2｜第二幕（15 张）

S14 and S19 will be shown in split screen: keep the subject in the center of frame.

**S14W** `[DAY]`
Close-up, subject centered: two weathered hands (W-ELDER) cupping a pile of freshly dug yellow-skinned potatoes, soil on the fingers, dark earth background.

**S14A** `MIRROR OF S14W`
Change only: the hands belong to A-ELDER, cupping native Andean potatoes of many colors and shapes: deep purple, black, yellow, speckled, knobby and twisted. No red-skinned potatoes.

**S15W** `[FIRE]`
Close-up inside a dim farmhouse: weathered hands (W-ELDER) burying potatoes into glowing embers and grey ash in a sunken indoor fire pit, wisps of smoke, firelight on the fingers, background dark and out of focus.

**S15A** `MIRROR OF S15W`
Change only: replace the indoor fire pit with an outdoor Andean earth oven (huatia), a small dome of stacked dirt clods glowing orange-hot inside; the hands are A-ELDER's. Keep the same tight framing so the background stays dark and out of focus.

**S16W** `[DAY]`
Close-up: dried red chilies being stirred with a wooden spatula in a wide black iron wok over a wood fire, thin smoke rising, the chilies beginning to darken.

**S16A** `MIRROR OF S16W`
Change only: replace the iron wok with a shallow unglazed clay pan (callana) over a small open fire; the chilies are dried red ají peppers stirred with a short wooden stick.

**S17a** `[DAY]`
Extreme close-up: a heavy wooden pestle striking down into toasted dried red chilies in a thick stone mortar, red flakes jumping on impact, dark background, hard side light from the left.

**S17b** `[DAY]` (generate directly, same scale and light as S17a)
Extreme close-up: weathered hands (A-ELDER) rocking a heavy curved stone back and forth on a flat grinding stone (batán), crushing red ají peppers into a coarse paste, dark background, hard side light from the left.

**S17c** `[DAY]`
Macro shot: coarse chili flakes and seeds inside a stone mortar, every granule visible, a cloud of fine red dust hanging in a beam of side light.

**S17d** `[DAY]`
Macro shot: bright red chili paste being pressed under a grinding stone, seeds and fibers visible, glistening texture, hard side light from the left.

**S17e**
Macro shot: fine red chili dust particles floating in a single shaft of light in a completely dark room, black background.

**S18W** `[DAY]`
Extreme close-up of the eyes of W-ELDER: deep wrinkles, squinting through drifting wood smoke, warm side light from the left, dark background.

**S18A** `MIRROR OF S18W`
Change only: the eyes are A-ELDER's, with the same framing, the same squint and the same light.

**S19W** `[DAY]`
Close-up, subject centered: weathered hands (W-ELDER) breaking open a charred roasted potato, fluffy white interior, ash on the skin, dark background.

**S19A** `MIRROR OF S19W`
Change only: the hands are A-ELDER's; the potato is a purple-skinned native potato roasted in an earth oven, with pale yellow flesh.

---

## PART 3｜四百年前（5 张）

**S21** `[NIGHT]`
Extreme wide shot at night: a 16th-century Spanish galleon with torn sails pitching in a violent storm on the open Pacific Ocean, enormous black waves, a lightning bolt illuminating the whole sea and the ship's silhouette, sheets of rain. Epic scale.

**S22** `[NIGHT]`
Inside the dark hold of a wooden galleon at night, camera at floor level: a swinging oil lantern, wet wooden planks, a burlap sack split open with brown potatoes spilling across the planks, and a single dried red chili pod lying among them. Warm lantern light against cold darkness.

**S23** (still image only, no people)
An antique hand-drawn parchment map of the Pacific Ocean in a Pacific-centered projection, East Asia on the left edge and South America on the right edge, sepia ink coastlines, a faded compass rose, aged paper with stains and creases, flat top-down view, even soft light. Absolutely no text, labels or lettering of any kind.

**S24a** `[NIGHT]`
Close-up: a blinding white lightning bolt striking down through black storm clouds.

**S24b** `[FIRE]`
Close-up at table height: flames bursting to life in a charcoal brazier beneath a shallow round cast-iron griddle (laoguo), fire flaring up around its dark rim, dark farmhouse interior.

---

## PART 4｜第三幕（10 张）

**S25W** `[FIRE]`
Overhead shot: a round shallow cast-iron griddle (laoguo) glistening with hot oil on a charcoal brazier in the middle of a dark wooden table, slices of potato being laid onto it with chopsticks, oil sizzling and steaming.

**S25A** `MIRROR OF S25W`
Change only: replace the cast-iron griddle with a round shallow unglazed clay pan (callana) on a small clay stove; chunks of purple and yellow native potato are turned by A-ELDER's fingers instead of chopsticks.

**S26W** `[FIRE]`
Close-up: a small white ceramic dish filled with coarse dark-red chili powder on a dark wooden table, flakes, seeds and granules clearly visible, side-lit by firelight, the glowing griddle softly out of focus behind.

**S26A** `MIRROR OF S26W`
Change only: replace the ceramic dish with a small hand-carved stone bowl filled with coarse red chili sauce (uchucuta); the clay pan is softly out of focus behind.

**S27W** `[FIRE]`
Close-up: chopsticks pressing a golden griddled potato slice into a small dish of coarse red chili powder, the granules clinging to the potato.

**S27A** `[FIRE]` (not a mirror, generate directly)
Close-up: weathered fingers (A-ELDER) lifting a roasted potato piece out of a stone bowl of red chili sauce, a drop of sauce falling.

**S28W** `[FIRE]`
Medium shot at seated eye level in a firelit farmhouse: W-ELDER sits at the left end of a long dark wooden table, her body angled toward the right side of the frame, an iron griddle glowing in front of her. She slides a small dish of chili powder toward the right. The table edge runs horizontally across the lower third and continues off the right edge of frame. A small window behind her shows misty limestone peaks at dusk. Keep her in the left-center part of the frame.

**S28A** `MIRROR OF S28W`, flipped horizontally
Recreate S28W as a horizontal mirror image: A-ELDER sits at the RIGHT end of the table, angled toward the left. Replace the iron griddle with a clay pan, and the dish with a small stone bowl of chili sauce that she slides toward the left. Replace the walls with adobe; the window behind her shows snow-capped Andean peaks at dusk. The table edge must stay at exactly the same height as in S28W.

**S29** `[FIRE]` (use S28W and S28A as references)
One continuous wide image at seated eye level: a single long wooden table runs across the whole frame. The left half of the room is the Yunnan farmhouse from S28W (rammed-earth wall, small window showing misty limestone peaks); the right half is the Andean adobe interior from S28A (adobe wall, small window showing snow-capped peaks). The two halves blend seamlessly at the center with no visible line. W-ELDER sits at the left end and A-ELDER at the right end, facing each other along the table; an iron griddle on the left and a clay pan on the right, both steaming.

**S30**
Aerial view at dusk: one continuous mountain ridge runs across the frame. The left half is green karst mountains of northeastern Yunnan with terraced fields and small grey-roofed villages with rising smoke; it blends seamlessly into the right half, the high Andes with stone terraces, small adobe villages and snow peaks. One unbroken ridgeline, warm golden sky, mist in the valleys.
