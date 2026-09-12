---
name: starryear-surreal-proliferation
description: "Transform one photograph into a vertical three-part artwork about absurd, seemingly endless cloning: two compositionally independent surreal clone-worlds around an untouched source crop, unified by one palette and rendering language without imitating the source layout. Use for 超现实复制、无尽克隆、荒诞增殖、原图居中三联画, or Starryear Surreal Proliferation. Do not use for ordinary copy-paste effects, generic photo filters, source-layout imitation, or full-image style transfer."
---

# Starryear Surreal Proliferation

Create one borderless vertical triptych whose central idea is **absurd, endless cloning**. The middle is an untouched crop from the actual source file. Above and below, boldly reconstruct the subject and scene into two different impossible worlds. Preserve identity, palette, material, and atmosphere from the source, but deliberately break its object coordinates, count, orientation, scale hierarchy, camera arrangement, and negative-space map. The generated panels must feel invented rather than like embellished copies of the middle.

## Non-negotiable architecture

Never ask an image model to render the finished triptych in one pass. Use three assets:

1. Generate the upper clone-world from the source photograph.
2. Generate the lower clone-world from the source photograph in a separate call.
3. Run `scripts/compose_triptych.py` to crop the original file itself and assemble upper + source crop + lower.

The middle panel must contain actual source pixels. It may be cropped, proportionally resized, and positioned only.

## Workflow

1. Inspect the source at full resolution. Identify the subject's unmistakable identity, repeatable form/gesture, native palette, light, texture, spatial skeleton, and one contradiction that can drive absurdity.
2. Separate **identity evidence** from **layout evidence**. Preserve only the minimum visual DNA needed to recognize the source subject; treat its original object positions, count, facing direction, scale relationships, depth order, camera framing, and empty-space pattern as forbidden templates for the generated panels.
3. Choose two different cloning logics from the full prompt. Write one sentence for each panel that describes a new spatial premise. Neither sentence may describe the source scene, and the two sentences must not be interchangeable.
4. Establish one shared art direction before generation: 3–5 dominant source-derived colors, one light/weather logic, one surface family, one edge/mark language, and one contrast/grain level. Apply this same visual grammar to both generated panels without borrowing the source composition.
5. Read the appropriate full prompt:
   - Chinese: [references/starryear-surreal-proliferation-prompt.zh-CN.md](references/starryear-surreal-proliferation-prompt.zh-CN.md)
   - English: [references/starryear-surreal-proliferation-prompt.en.md](references/starryear-surreal-proliferation-prompt.en.md)
6. Generate the upper panel as an overwhelming multiplication event: the viewer should immediately feel “there are impossibly many.” Favor escalating quantity, scale cascades, swarms, nesting, extrusion, or horizon-filling processions, using a camera position and directional flow absent from the source.
7. Generate the lower panel as a different kind of absurdity: cloned subjects alter space, architecture, function, causality, gravity, or hierarchy. Favor loops, recursive rooms, impossible carrying, subject-built landscapes, inverted gravity, or one clone producing another.
8. Run a **composition-independence gate** on each generated panel. Compare it with the middle crop and reject it if the main anchor occupies a similar normalized location, if multiple subjects repeat the same left/right/top/bottom relationships, or if the silhouette and negative-space map still read like the original photograph. Regenerate with a new camera, new anchor placement, new direction, and stronger spatial transformation rather than making a minor variation.
9. Reject either panel if it reads as ordinary duplication, a neat pattern, unrelated fantasy decoration, the same idea twice, or a stylized imitation of the middle. Rebuild rather than merely add more copies.
10. Assemble deterministically:

   ```bash
   python scripts/compose_triptych.py \
     --top <upper-panel> \
     --source <original-photo> \
     --bottom <lower-panel> \
     --output <finished.png>
   ```

   Default canvas: 1536×2304 with 34/24/42 panel ratios. Use `--crop x,y,w,h` only to choose the best evidence crop; coordinates are source pixels.
11. Inspect the finished artwork. Confirm that the middle is untouched source evidence; neither generated panel mirrors its placement or staging; the cloning feels excessive and absurd; top and bottom are genuinely different; and both belong to the same chromatic and material world.
12. Return exactly one finished image unless the user asks for separate panels.

## Visual guardrails

- **Cloning is the subject, not decoration.** Quantity must affect meaning, space, or causality.
- **Bold reconstruction is allowed above and below.** The original location may stretch, fold, invert, empty out, become architectural, or be rebuilt around the clones.
- **Source identity remains legible.** Preserve enough silhouette, anatomy, object construction, gesture, or signature detail that every clone is traceable to the photograph.
- **Source composition is not protected.** Do not preserve the source subject's coordinates, count, facing direction, scale hierarchy, depth order, focal arrangement, horizon placement, or negative-space silhouette. Source fidelity applies to identity and visual DNA, not staging.
- **No positional echo.** The largest or clearest clone in either generated panel should normally move to a different third of the frame from the source anchor; avoid recreating a recognizable constellation of source objects even when individual objects are accurate.
- **Invent before multiplying.** Each generated panel must first establish a new camera, spatial skeleton, and impossible rule; only then populate it with clones. More copies alone do not count as transformation.
- **Difference across generated panels.** Do not reuse the same arrangement, camera setup, scale structure, or surreal trick above and below.
- **Unity across generated panels.** Match palette, color temperature, light direction or atmospheric logic, texture family, grain, material response, edge handling, and overall finish. “Different scene” must not become “different franchise.”
- **Middle evidence is inviolable.** No generation, retouching, recoloring, relighting, filtering, masking, overlays, text, seams, or object edits.
- Avoid wallpaper grids, stamp-like clones, source-layout tracing, same-place hero subjects, identical pose and scale everywhere, empty floating cutouts, collage halos, malformed bodies/objects, illegible clutter, generic fog/glow, galaxies, neon effects, and unrelated symbols.
- One borderless vertical image; no title, caption, logo, signature, date, frame, gutter, or watermark.

## Final QA

- Compare the middle panel with the corresponding crop from the source; any unexplained pixel change fails.
- At first glance, the work must communicate an absurd surplus of the source subject.
- Upper and lower must be describable with two different one-sentence premises.
- Neither generated panel may be describable as “the source composition with more copies”; compare anchor position, relational layout, depth order, directional flow, and negative-space map against the middle crop.
- Both generated panels must share the same palette and rendering language despite different spatial constructions.
- Check clone integrity, perspective, contacts, occlusion, density rhythm, readable negative space, and clean joins.

Keep `assets/examples` empty during drafting and testing. Add only final user-approved examples; never reuse their subject matter or composition for another source.
