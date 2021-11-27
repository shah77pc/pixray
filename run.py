import sys
sys.path.append("pixray")
# Simple setup
import pixray

prompts = "big white"
drawer = "pixel"

# these are good settings for pixeldraw
pixray.reset_settings()
pixray.add_settings(prompts=prompts)
pixray.add_settings(quality="better")
pixray.add_settings(drawer=drawer)
pixray.add_settings(display_clear=True)
settings = pixray.apply_settings()
pixray.do_init(settings)
pixray.do_run(settings)
