from manim import *
from manim_slides import Slide



Text.set_default(font="Ubuntu")
config.background_color = "#121212"      # Deep charcoal (not quite black)
Text.set_default(color="#e0e0e0")        # Soft grey-white
MathTex.set_default(color="#e0e0e0")
Axes.set_default(axis_config={"color": "#404040"})
Line.set_default(color="#60a5fa")        # Soft blue
ParametricFunction.set_default(color="#c084fc")  # Lavender


class MyPresentation(Slide):
    def construct(self):
        
        rect=Rectangle()
        text3 = Text("Conception")
        self.play(Write(text3))
        self.play(ShowPassingFlash(rect,run_time=2,time_width=0.5))

from manim import *
from manim_slides import Slide

# Custom styling functions
def style_rectangle(rect, fill_color, stroke_color=WHITE, fill_opacity=0.3, stroke_width=3):
    """Apply consistent styling to rectangles"""
    rect.set_style(
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
        stroke_opacity=0.9,
        sheen_factor=-0.3,
        sheen_direction=UR
    )
    return rect

def style_text(text, color=WHITE):
    """Apply styling to text"""
    text.set_style(
        fill_color=color,
        fill_opacity=1,
        stroke_color=BLACK,
        stroke_width=0.5,
        stroke_opacity=0.5
    )
    return text

class DataPipelineSlideShow(Slide, MovingCameraScene):
    def construct(self):
        # ============================================
        # TITLE SLIDE
        # ============================================
        title = Text("Conception", font_size=72, weight="BOLD")
        title.set_style(fill_color=WHITE, stroke_width=0)
        self.play(Write(title))
        self.wait(0.5)
        self.next_slide()  # Wait for user input
        
        # Fade out title
        self.play(FadeOut(title, shift=UP))
        self.wait(0.3)
        
        # ============================================
        # TOPICS FOR SLIDES
        # ============================================
        topics = [
            ("Dataset Exploration", "#FF6B6B"),
            ("Dataset Distillation", "#4ECDC4"),
            ("Creation & Calculation", "#45B7D1"),
            ("Retrieval Metrics", "#96CEB4"),
            ("Generation Metrics", "#FFEAA7"),
            ("Conclusion", "#DDA0DD")
        ]
        
        slide_width = 8
        slide_height = 3
        slides = []
        arrows = VGroup()
        
        # Save initial camera state (zoomed out view)
        self.camera.frame.save_state()
        
        # ============================================
        # CREATE EACH SLIDE WITH CAMERA MOVEMENT
        # ============================================
        
        for i, (topic, color) in enumerate(topics):
            # Determine position for this slide
            if i == 0:
                # First slide at center
                slide_pos = ORIGIN
            else:
                # Subsequent slides - 5 units down from previous
                slide_pos = slides[i-1].get_center() + DOWN * 5
            
            # Create the rectangle (no corner_radius)
            rect = Rectangle(width=slide_width, height=slide_height)
            rect.move_to(slide_pos)
            rect = style_rectangle(rect, fill_color=color, stroke_color=WHITE)
            
            # Create the text
            text = Text(topic, font_size=40, weight="BOLD")
            text = style_text(text, color=WHITE)
            text.move_to(rect.get_center())
            
            # Group as slide
            slide = VGroup(rect, text)
            slides.append(slide)
            
            # Animate slide creation with camera
            if i == 0:
                # First slide: create in place
                self.play(FadeIn(slide, scale=0.8), run_time=0.6)
                self.wait(0.3)
            else:
                # Move camera to new slide position first
                self.play(
                    self.camera.frame.animate.move_to(slide_pos),
                    run_time=0.8
                )
                # Then create the new slide
                self.play(FadeIn(slide, scale=0.8), run_time=0.5)
                self.wait(0.2)
                
                # Add arrow from previous slide to current
                arrow = Arrow(
                    slides[i-1].get_bottom(),
                    slide.get_top(),
                    color=WHITE,
                    stroke_width=4,
                    buff=0.2,
                    tip_length=0.2
                )
                arrow.set_style(stroke_color=WHITE, stroke_width=3)
                arrows.add(arrow)
                self.play(Create(arrow), run_time=0.3)
            
            # Highlight and wait on each slide
            self.play(
                rect.animate.set_stroke(width=6, color=YELLOW),
                run_time=0.2
            )
            self.wait(1)
            self.play(
                rect.animate.set_stroke(width=3, color=WHITE),
                run_time=0.2
            )
            
            # Add slide pause for manual advancement
            self.next_slide()
        
        # ============================================
        # ZOOM OUT TO SEE ALL SLIDES
        # ============================================
        
        # Calculate the full bounding box of all slides and arrows
        all_elements = VGroup(*slides, arrows)
        bounding_center = all_elements.get_center()
        

        self.play(
            AnimationGroup(
                self.camera.frame.animate.scale(4).move_to([0,-13,0]),
                run_time=1.2,
                lag_ratio=0.1
            )
        )




        # Wait to show full pipeline
        self.wait(0.5)
        
        # Add a subtle pulse to all slides
        self.play(
            *[slide.animate.scale(1.02) for slide in slides],
            run_time=0.3
        )
        self.play(
            *[slide.animate.scale(0.9804) for slide in slides],
            run_time=0.3
        )
        
        self.next_slide()
        
        
        
        self.next_slide()
        self.play(*[FadeOut(obj, shift=DOWN, scale=0.9) for obj in self.mobjects])
        
        # Fade out everything
        
        self.wait(0.5)


from manim import *
from manim_slides import Slide


def style_rectangle(rect, fill_color, stroke_color=WHITE, fill_opacity=0.3, stroke_width=3):
    rect.set_style(
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
        stroke_opacity=0.9,
        sheen_factor=-0.3,
        sheen_direction=UR
    )
    return rect


def style_text(text, color=WHITE):
    text.set_style(
        fill_color=color,
        fill_opacity=1,
        stroke_color=BLACK,
        stroke_width=0.5,
        stroke_opacity=0.5
    )
    return text


class DataPipelineSlideShow(Slide, MovingCameraScene):
    def construct(self):

        # ── TITLE ──────────────────────────────────────────────
        title = Text("Conception", font_size=72, weight="BOLD")
        title.set_style(fill_color=WHITE, stroke_width=0)
        self.play(Write(title))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(title, shift=UP))
        self.wait(0.3)

        # ── PIPELINE STAGES ────────────────────────────────────
        # Each entry: (label, subtitle, hex color)
        # Colors mirror the SVG diagram:
        #   teal   → data bookends
        #   gray   → fixed components
        #   purple → reranker (variable)
        #   amber  → distillation side-branch
        #   coral  → evaluation
        stages = [
            ("BioASQ 13b  –  Task B",    "5 389 train · 340 test queries",           "#1D9E75"),  # teal
            ("Preprocessing",             "BEIR format · 200 k PubMed expansion",     "#1D9E75"),  # teal
            ("BM25 Retrieval",            "Top-50 candidate passages  (fixed)",        "#888780"),  # gray
            ("Distillation pipeline",     "DeepSeek V3.2  →  LiT5 fine-tune",           "#BA7517"),  # amber
            ("Reranker",                  "LiT5 · LiT5 fine-tuned · Qwen3-4B · Hybrid Approach ",        "#7F77DD"),  # purple
            ("Llama-3.1-8B-Instruct",    "Fixed generator  –  local",                 "#888780"),  # gray
            ("Evaluation",               "Retrieval (MAP·MRR·NDCG)  +  Generation",   "#D85A30"),  # coral
            ("Statistical Test",  "Paired signed-rank test",                   "#1D9E75"),  # teal
        ]

        slide_width  = 9
        slide_height = 2.6
        gap          = 4.2          # vertical distance between slide centres
        slides       = []
        arrows       = VGroup()

        self.camera.frame.save_state()

        # ── BUILD EACH SLIDE WITH CAMERA PAN ──────────────────
        for i, (label, subtitle, color) in enumerate(stages):

            slide_pos = ORIGIN if i == 0 else slides[i - 1].get_center() + DOWN * gap

            # Rectangle
            rect = Rectangle(width=slide_width, height=slide_height)
            rect.move_to(slide_pos)
            rect = style_rectangle(rect, fill_color=color, stroke_color=WHITE, fill_opacity=0.25)

            # Main label
            main_text = Text(label, font_size=52, weight="BOLD")
            main_text = style_text(main_text, color=WHITE)
            main_text.move_to(slide_pos)

            # Subtitle
            # sub_text = Text(subtitle, font_size=22)
            # sub_text = style_text(sub_text, color=LIGHT_GRAY)
            # sub_text.move_to(slide_pos + DOWN * 0.38)

            slide = VGroup(rect, main_text )
            slides.append(slide)

            # ── animate ──
            if i == 0:
                self.play(FadeIn(slide, scale=0.85), run_time=0.6)
                self.wait(0.3)
            else:
                self.play(
                    self.camera.frame.animate.move_to(slide_pos),
                    run_time=0.75
                )
                self.play(FadeIn(slide, scale=0.85), run_time=0.5)
                self.wait(0.2)

                # Special dashed arrow for the distillation branch (index 3)
                arrow = Arrow(
                        slides[i - 1].get_bottom(),
                        slide.get_top(),
                        color=WHITE,
                        stroke_width=3,
                        buff=0.18,
                        tip_length=0.2
                    )
                arrow.set_style(stroke_color=WHITE, stroke_width=3)

                arrows.add(arrow)
                self.play(Create(arrow), run_time=0.35)

            # Highlight pulse
            self.play(rect.animate.set_stroke(width=6, color=YELLOW), run_time=0.2)
            self.wait(0.8)
            self.play(rect.animate.set_stroke(width=3, color=WHITE),  run_time=0.2)

            self.next_slide()

        # ── ZOOM OUT TO SEE THE FULL PIPELINE ─────────────────
        total_height = len(stages) * gap

        self.play(
            self.camera.frame.animate
                .scale(len(stages) * 0.52)
                .move_to([0, -14.7 , 0]),
            run_time=1.4
        )
        self.wait(0.5)

        # Subtle pulse on all slides
        self.play(*[s.animate.scale(1.02) for s in slides], run_time=0.3)
        self.play(*[s.animate.scale(1 / 1.02) for s in slides], run_time=0.3)

        self.next_slide()
        return

        # ── FADE OUT ──────────────────────────────────────────
        self.play(
        LaggedStart(
        *[FadeOut(obj, shift=DOWN, scale=0.9) for obj in self.mobjects],
        lag_ratio=0.1
    )
)
        self.wait(0.5)
