# 🎥 CINEMATIC SHORTS & ANIMATED MOVIE CLIPS TECH STACK
**Credit 2 Money Solutions** | Video Production Playbook  
*The exact generative AI software stack Rick Jefferson uses for cinematic animated characters and movie clips.*

---

## 1. Overview of the Stack
Rick Jefferson produces high-engagement animated movie clips and stylized characters using a multi-model generative AI pipeline:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                     RICK JEFFERSON CINEMATIC PRODUCTION PIPELINE                │
├─────────────────────┬─────────────────────┬───────────────────┬──────────────────┤
│   1. CHARACTER ART  │ 2. VIDEO GENERATION │  3. LIP-SYNC/FACE │ 4. POST & CAPTION│
│  Midjourney v6.1 /  │  Kling AI v1.5/v2 / │   LivePortrait /  │   CapCut Pro /   │
│   FLUX.1 [dev]      │   Runway Gen-3/4    │    Hedra Studio   │   DaVinci Resolve│
└─────────────────────┴─────────────────────┴───────────────────┴──────────────────┘
```

---

## 2. The 4 Pipeline Stages

### Stage 1: Character Genesis (Image Generation)
- **Tools**: **Midjourney v6.1** or **FLUX.1 [dev]** via Venice AI / Replicate.
- **Formula for Antoine's Stylized Character**:
  ```text
  /imagine prompt: A high-end 3D animated executive character representing Antoine Solomon, African American male with sharp groomed beard, sharp focus, wearing an emerald green and black tailored velvet blazer, modern luxury penthouse background overlooking city skyline, cinematic dramatic studio lighting, 8k octane render, stylized Pixar meets comic book graphic novel aesthetic, vibrant money green and deep slate palette --ar 9:16 --v 6.1 --stylize 250
  ```

### Stage 2: Motion & Camera Directing (Video AI)
- **Tools**: **Kling AI (v1.5 / v2)** or **Runway Gen-3 Alpha / Gen-4**.
- **Technique**: Upload the still image from Stage 1 into Kling Image-to-Video.
- **Motion Prompt**:
  ```text
  Slow cinematic push-in on character, character confidently looks directly into camera lens, subtle confident smirk, cinematic golden hour lighting, slight head movement, 4k ultra realistic, high frame rate, zero distortion.
  ```

### Stage 3: Audio & Voice Re-Enactment (Lip-Sync)
- **Tools**: **LivePortrait** (open source) or **Hedra Studio** (`hedra.com`).
- **Workflow**:
  - Generate vocal audio using Antoine's voice clone on ElevenLabs (or recorded voice note).
  - Feed the animated video clip and audio file into Hedra or LivePortrait.
  - The AI aligns phonemes to mouth movements with emotional micro-expressions.

### Stage 4: Editing & B-Roll Assembly
- **Tool**: **CapCut Pro** (Desktop / Mobile).
- **Features to Enable**:
  - Auto-Captions with **Bold Green / Yellow Kinetic Styling** (Hormozi / Rick Jefferson style).
  - Cash register / "cha-ching" sound effects at key money terms.
  - Whoosh transitions between hook, body, and CTA.
  - Overlay screenshot proof (Chase Ink approvals, dispute deletion letters).
