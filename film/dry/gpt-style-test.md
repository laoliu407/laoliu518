# 《干》ChatGPT 风格测试（7 张图）

## 给你看的用法

这 7 张图先验证一件事：**画面能不能做到真实纪录片的质感**。它们覆盖了全片的几种主要场景：阳台、县城、乡下、天气、夜里的室内、烙烤锅、高潮的柜台。测试通过的图会直接用进正片，所以请认真挑。

1. 开一个新的 ChatGPT 对话，上传本文件，发送：`按文件执行`。
2. ChatGPT 每次出一张图，开头标着图片编号。满意就回复 `下一个`；不满意就回复 `重做`，并说明哪里不对（第 5 节有现成的说法）。
3. 每张图按编号保存，比如 `BALCONY-MASTER.png`、`S05.png`。同一张多出几版，就加后缀：`S05-2.png`、`S05-3.png`。
4. 做完后把图发给我：直接发到我们这个对话里，或者传到 GitHub 仓库的 `film/dry/incoming/` 文件夹。我逐张检查，通过了再出完整任务单的其余部分。

**最重要的两张：**
- `BALCONY-MASTER.png` 是阳台母版。全片 7 个阳台镜头都从它改出来，构图一旦定下就不再变。
- `S21.png` 是烙烤锅"拱背背"，后面瓦檐流水的镜头要照着它的角度来做。

**怎么判断合不合格：** 问自己，这像不像纪录片里随手截下来的一帧？如果它像电影剧照、广告、短剧或者摆拍的风景照，就重做。

---

## INSTRUCTIONS FOR CHATGPT

You are generating still frames for a short **observational documentary** about a rainy mountain county town in northeast Yunnan, China. Every image must look like a frame grab from real documentary footage shot on location. If an image looks like a movie still, a TV drama, an advertisement, a painting or AI art, it has failed.

1. When the user says `按文件执行` or `下一个`, generate the next item in section 4, in order. Generate exactly ONE image per reply.
2. Build each prompt like this: the STYLE block, then the REGION block, then the item's prompt, then the PEOPLE block if people appear, then the PALETTE & AVOID block. Pass the text to the image tool as it is. Do not add words about mood, beauty, drama, atmosphere, "cinematic" or "epic" quality.
3. Landscape 3:2 (1536×1024), filled edge to edge. Never add borders, captions, titles, watermarks, logos or any readable text.
4. Start every reply with the item ID in bold (for example **S05**) and end it with one line: the file name to save it as.
5. When in doubt, make the image plainer, flatter and more ordinary. Never beautify.
6. If the user says `重做` or reports a problem, regenerate the same item and apply the matching fix from section 5.

---

## 1. STYLE（每条开头）

```
Observational documentary still, a frame grab from a digital cinema camera shot on location. Only the light that is really there: overcast diffuse daylight, fog, a window, a bare bulb or a stove flame. No added lighting. Deep focus: everything sharp from foreground to background. Eye-level tripod unless stated otherwise. Natural, slightly muted colors straight from the camera, neutral white balance, slightly underexposed, humid air.
```

## 2. REGION（每条第二段）

```
Northeast Yunnan mountain county, about 1,200 m altitude: a small basin town ringed by steep green slopes with patchy dry-land fields of corn, potato and chili, some under plastic mulch film; bamboo groves; low clouds clinging to the ridges. The town is 4–6 storey self-built concrete houses, some tiled white or beige, many bare concrete; blue or white corrugated metal rain awnings; stainless steel window grilles; air-conditioner units; tangled power lines; small shops with roll-up shutters; wet asphalt; e-bikes and motorcycles with full rain capes. Rural houses mix old timber-frame houses with grey clay tile roofs and newer 2–3 storey flat-roofed concrete houses, with concrete courtyards, firewood stacks and woven plastic sacks.
```

## 3. PEOPLE（画面里有人时加上）

```
Ordinary local residents in worn, faded, mismatched everyday clothes, going about their business, not looking at the camera, not posing, small in the frame or turned away. Real, uneven skin; no makeup; no ethnic costume.
```

## PALETTE & AVOID（每条结尾）

```
Palette: grey-green mountains, wet cement grey, old white tiles, brownish brick, dull chili red only where the prompt asks for it, coal-flame blue. Avoid: cinematic lighting, rim light, light rays, shallow depth of field, bokeh, golden hour glow, lens flare, teal-and-orange grade, HDR, glossy or retouched skin, costumes or ethnic dress, tourist-town or old-town architecture, rice-paddy terraces, staged symmetry, readable text or logos. Keep the top and bottom 8% of the frame free of important detail.
```

---

## 4. 七张图

### BALCONY-MASTER（阳台母版，也是 S04 的首帧）

```
A second-floor balcony of a three-storey self-built concrete house in a small mountain county town, about 8:30 am in January, flat grey morning light, light drizzle, fog. Camera at the inner end of the balcony, eye level, tripod, 28mm lens, looking diagonally along the balcony toward the street. Right edge of frame: an open aluminium balcony door into a dim living room; just inside, a wooden cabinet with an old radio on it. Under a blue corrugated metal rain awning, a stainless steel drying rail runs the length of the balcony. Nearest to the camera, left of centre, hangs a single pale blue cotton long-sleeve shirt on a white plastic hanger, wet and heavy, one drop of water at its hem; further along the rail hang two dark towels. Directly below the shirt, on the beige tiled floor: a red plastic basin with a little water in it. Along the left: a waist-high railing wall with a flat concrete ledge on top and a stainless steel grille. Clutter: a mop leaning on the wall, a dead potted plant, a stack of woven plastic sacks, a twin-tub washing machine under a faded cover near the door. Beyond the railing: a narrow street, and across it a row of 4–5 storey concrete houses, some tiled white, with balconies, awnings, window grilles, rooftop water tanks and solar water heaters, their flat roofs visible, fading into fog. No people.
```

### S05（一月早晨的县城）

```
Wide shot from a rooftop across the street, tripod, 35mm lens, about 8:30 am on a January morning, fog and light drizzle. Foreground: under the edge of a rooftop eave, a neat stack of coal honeycomb briquettes, wet and dripping. Middle ground: the street below, with steam rising from a breakfast stall's bamboo steamers, a few motorcycles and e-bikes passing with full rain capes covering rider and handlebars, people with umbrellas, wet asphalt reflecting grey sky. Background: rows of 4–6 storey self-built houses with awnings and grilles, each row fainter as it disappears into the fog. People are small in the frame.
```

### S10（七月底的辣椒坡地）

```
Very wide shot from an opposite hillside, tripod, late July, a bright day with big cumulus clouds and their shadows lying on the slopes. A steep dry-land hillside of chili fields (not terraced rice paddies), row after row of chili plants heavy with ripe red chilies, some rows under old plastic mulch film. Foreground: a few chili plants full of red pods and a cone-shaped bamboo back-basket on the ground. Middle ground: a handful of pickers in straw hats and old shirts scattered across the field, very small. Background: a few farmhouses with flat concrete roofs and grey tile roofs, then the next ridge with cumulus clouds above it.
```

### S12（雨墙推过坝子）

```
Very wide shot from a hilltop looking down into a mountain basin, tripod, a hot August afternoon. The county town lies small in the sunlit basin, a patchwork of grey and white concrete roofs, many spread with quilts and drying trays. Above the far ridge a huge dark grey storm cloud is pressing in, and beneath it a solid grey curtain of rain hangs like a wall, already crossing the far edge of the basin. The near half of the basin is still in sunshine; the far half is in the storm's shadow. No lightning. No people visible.
```

### S18（冬夜的灶房）

```
Medium shot, camera slightly above the stove at about 15 degrees, tripod, a winter night, lit only by the stove flame, one bare bulb and a little light from the next room. A large square cast-iron coal stove top with a round fire hole showing a ring of blue coal flame; a dented aluminium kettle steaming on top; two charred, split roasted potatoes on the stove edge; a bowl of noodles topped with red chili; a small white dish of coarse red chili flakes. Above the stove, hanging from a bamboo pole, a one-metre string of dark red, wrinkled, matte dried chilies. Behind, a tiled wall with a thermos flask and a plastic stool, and a window misted with condensation, night outside. No people.
```

### S21（烙烤锅"拱背背"）

```
Side view, camera about 15 degrees above the table surface, tripod, at night in a small local grill restaurant. A round iron ring set into a wooden table holds an upside-down cast-iron wok; its back forms a low black dome that fills the right two-thirds of the frame, with an oil gutter about 2 cm wide running around its rim. Five potato slices are browning on the dome; thin streams of rapeseed oil run down the dome's curve into the gutter; a little smoke drifts across the top of the dome like a cloud over a hill. Light: a warm bare tungsten bulb from the upper left, cool fluorescent fill from the room. Deep focus. No hands, no people.
```

### S23（高潮：干燥的柜台）

```
Medium-wide side view of the front counter of a small local grill restaurant at night, tripod. A worn wooden counter under one bare tungsten bulb; a row of eight small white porcelain dishes; a stainless steel basin of coarse red chili flakes; the owner, seen from the side and slightly behind, wearing fabric over-sleeves, spooning flakes into one dish. The spoon and the flakes are small in the frame. Dry, warm light. No steam, no smoke, no wet surfaces, no window or door in the frame. Deep focus.
```

---

## 5. 常见问题与重做说法

| 问题 | 回复 ChatGPT 的说法 |
|---|---|
| 像电影、短剧或广告 | Make it look like an ordinary unedited frame from a documentary: flat, plain light, neutral colors, nothing dramatic, nothing beautified. |
| 背景虚化、有光斑 | Deep focus: make the background as sharp as the foreground. No bokeh. |
| 偏黄、偏橙、像夕阳 | Neutral white balance. Remove the warm tint. |
| 太干净、太整齐 | Add real everyday clutter and wear: dust, stains, worn surfaces. Make the framing slightly imperfect. |
| 人物像演员、在看镜头 | Make the people ordinary local residents, small in the frame or turned away, busy with their work, not looking at the camera. |
| 建筑像古镇或景区 | Replace it with plain self-built 4–6 storey concrete houses of a small Chinese county town, some bare concrete, some white tiles. |
| 出现文字或乱码 | Remove all text, letters, signs and logos. |
| 阳台母版：衬衫不在左中最近的位置 | The pale blue shirt must be the closest object to the camera, left of centre, with the red basin directly below it. |
| S12 有闪电 | Remove the lightning. Only the dark cloud and the grey wall of rain. |
| S23 有水汽或湿反光 | Remove all steam, smoke and wet reflections. Everything is dry. |
