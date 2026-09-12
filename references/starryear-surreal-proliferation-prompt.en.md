# Starryear Surreal Proliferation | Endless-Cloning Prompt Standard

## Core proposition

Transform one source photograph into a vertical top–middle–bottom artwork whose primary subject is **the absurdity of endless cloning**. The middle is an ungenerated, unretouched crop of the source. Above and below it, boldly reconstruct subject and scene into two different surreal clone-worlds. The source supplies subject identity, color, material, and atmosphere, but it is not a composition template. Both generated panels must deliberately break the source's object coordinates, count, orientation, scale hierarchy, depth order, camera arrangement, and negative-space map. They must share one palette and rendering language while feeling invented rather than like embellished copies of the middle.

## Fixed architecture

Never generate the finished triptych in one image-model call. Generate the upper and lower panels separately. Keep the middle entirely outside the image model, then insert authentic source pixels with `scripts/compose_triptych.py`.

The middle may only be cropped, proportionally resized, and positioned. No generation, redraw, outpainting, retouching, grading, filtering, sharpening, added grain, masking, typography, overlays, or change in subject count.

## Silent pre-generation analysis

Do not output this analysis:

1. Identify the subject's irreplaceable identity cues: silhouette, construction, pose, color, material, expression, and signature details.
2. Separate **identity evidence** from **layout evidence**. Preserve the former and actively discard the latter. Do not inherit original coordinates, subject count, left/right or top/bottom relationships, facing direction, scale hierarchy, occlusion order, horizon placement, or negative-space silhouette.
3. Extract 3–5 dominant colors and define one shared color temperature, value structure, light/weather logic, surface treatment, edge behavior, grain, and sharpness.
4. Find one amplifiable contradiction, such as “many yet lonely,” “identical things manufacturing each other,” “heavy yet airborne,” “tiny things becoming architecture,” or “the subject cloning until it erases its original setting.”
5. Write a new and different spatial proposition for each generated panel. Neither sentence may merely describe the source. If they are interchangeable or still map onto the source layout, redesign them.
6. Choose a new camera, spatial skeleton, primary anchor, and directional flow before cloning begins. Never copy the source composition first and then fill its gaps with clones.

## Shared art direction

- Both generated panels must visibly clone the source subject, its parts, or both. Repetition is the protagonist, not decorative pattern.
- Bold reconstruction of the setting is allowed: stretch, fold, invert, hollow, compress, theatricalize, architecturally rebuild, or construct the scene from clones themselves.
- Preserve subject identity. Exaggerate number, scale, space, and causality without casually turning the subject into an unrelated object.
- Recognizability protects identity, not composition. Do not recreate the source's main subject regions, relational layout, orientation cluster, depth order, horizon, or negative-space map.
- The largest or clearest anchor in each generated panel should normally move to a different frame third from the source anchor. When literal relocation is unsuitable, create equivalent compositional separation through viewpoint, direction, scale, or spatial structure.
- Use one source-derived core palette across both panels. Saturation and value range may be expanded, but do not create two unrelated color scripts.
- Use one rendering language and finish across both panels: the same family of light, material response, texture/mark, edge hardness, grain, contrast, and atmosphere. Choose one primary language—photographic realism, dry painting, screen print, paper collage, sculptural stage, or another coherent system—and apply it consistently to both.
- The panels need not depict the same location or camera setup. They must feel native to the same aesthetic world.

## Upper panel | Quantity out of control

Using the source photograph as the sole subject reference, generate one full-width frame for the upper panel. The first glance should say “there are impossibly many.” Emphasize runaway quantity, density, and scale.

Choose the logic that best suits the source:

- One subject splits into dozens or hundreds of clones receding toward a horizon, sky, or architectural depth;
- A scale cascade runs from enormous to microscopic until clones become terrain, clouds, walls, or skyline;
- Subjects contain further subjects in recursive nesting, while each level remains source-recognizable;
- Clones consume the setting like a tide, migration, procession, swarm, or runaway production line;
- A signature body part proliferates massively while a few complete subjects act as witnesses and anchors.

Use density gradients, occlusion, scale shifts, and a clear visual current. Choose a viewpoint and primary flow absent from the source, and move the largest anchor away from its corresponding source location. Extreme density is welcome, but preserve a newly shaped area of negative space that lets the absurd relationship read. Avoid neat matrices, wallpaper tiling, identical stamp poses, literal copy-paste, or preserving the source composition while merely increasing quantity. Do not make causal loops, functional inversion, carrying hierarchies, or reversed gravity the upper panel's main mechanism.

## Lower panel | Rules out of order

Using the same source photograph as the sole subject reference, generate another full-width frame for the lower panel. Repetition remains abundant, but absurdity now comes primarily from broken space, function, causality, gravity, or hierarchy—not quantity alone.

Choose one logic clearly different from the upper panel:

- Clones carry, wear, support, or worship one another in an impossible hierarchy;
- One clone manufactures another, which manufactures a smaller one, forming a causal loop;
- Clones become stairs, bridges, rooms, mountains, streets, or containers, so the subject is also the setting;
- Gravity splits, with clones standing on walls, ceilings, or folded planes;
- Recursive rooms, looping roads, or mirrored spaces trap the clones without becoming a simple reflection effect;
- One giant clone and many tiny clones perform a clear but unexplained impossible task.

Create one dominant event, retain at least one near-source-scale identity anchor, and make repetition unfold through space or causality. Theatrical staging and radical scale failure are welcome; unsupported floating, contactless piles, and illegible clutter are not.

That identity anchor must not return to the corresponding position of the primary source subject or reproduce its neighboring relationships. The lower panel should feel like another set of physical laws inside the same visual world, not a natural extension downward from the middle.

## Composition-independence gate

After generating each panel, compare it with the middle crop. Reject and regenerate the panel if any condition is true:

- The largest or clearest subject occupies the same frame third as the middle's primary anchor;
- Two or more subjects repeat a recognizable left/right, top/bottom, or front/back relationship from the middle;
- The main silhouette, horizon, density distribution, or negative-space shape still resembles the source;
- “The source composition with more copies” remains an accurate summary;
- Style, quantity, or local scale changed, but camera, spatial skeleton, direction, and primary event did not.

Do not fix a failure with minor nudging. Select a new viewpoint, anchor region, directional flow, and spatial mechanism so the change is structural.

## Unity and difference check

- **Difference:** upper = quantity/scale/density out of control; lower = space/function/causality/gravity out of order.
- **Unity:** shared core palette, color temperature, lighting character, material, texture/mark, edge behavior, grain, and finish.
- **Source:** the identity and visual DNA of every major clone is traceable to the photograph, but its compositional coordinates and staging are not. Do not add attention-stealing species, symbols, galaxies, neon, magic glow, or generic dream decoration.
- **Absurdity:** each panel proposes an impossible but immediately legible rule. If it only says “more of the same thing,” reconstruct the space or causality further.

## Explicit exclusions

Exclude ordinary copy-paste, source-position tracing, same-place hero subjects, the original composition with added quantity, regular grids, wallpaper patterns, kaleidoscopes, simple mirroring, identical poses and scales everywhere, cutout halos, floating stickers, bad intersections, fused clones, malformed anatomy/construction, lost subject identity, unrelated objects, different rendering styles between panels, separate color scripts, generic fog, halos, stars, neon, text, borders, dividers, title, logo, signature, and watermark.

## Deterministic assembly

After approving both generated panels, run:

```bash
python scripts/compose_triptych.py --top TOP.png --source ORIGINAL.jpg --bottom BOTTOM.png --output FINAL.png
```

The default canvas is 1536×2304 with 34/24/42 panel ratios. This makes the middle a calm strip of real-world evidence and gives the lower reconstruction more room. Adjust with `--ratios` when needed; use `--crop x,y,w,h` for the source crop. Never apply a whole-image effect after assembly if it would alter the middle pixels.

## Acceptance and output

1. The middle is made from authentic source pixels with crop and proportional resize only.
2. “Absurd endless cloning” reads at first glance.
3. The upper and lower can be summarized by two genuinely different sentences; neither is a rearranged version of the other.
4. Neither generated panel repeats the middle's anchor position, relational layout, depth order, directional flow, or negative-space map; neither can be summarized as “the source composition with more copies.”
5. Both generated panels share one palette and rendering language despite radical scene reconstruction.
6. Clone identity, density rhythm, occlusion, scale, spatial contact, and negative space remain readable.
7. Return exactly one borderless vertical artwork without text or watermark unless the user requests separate panels.
