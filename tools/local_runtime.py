"""Portable local dependencies for optional rendering helpers."""
import os
import shutil


def executable(name, environment_variable):
    """Resolve an explicit override or a command on PATH without recording it."""
    requested = os.environ.get(environment_variable) or name
    resolved = shutil.which(requested)
    if not resolved:
        raise FileNotFoundError(
            f"Install {name} on PATH or set {environment_variable} to its executable."
        )
    return resolved


def load_font(size):
    """Use an explicit font, an installed common font, or Pillow's fallback."""
    from PIL import ImageFont
    override = os.environ.get('ISO20022_FONT')
    if override:
        return ImageFont.truetype(override, size)
    for name in ('arial.ttf', 'DejaVuSans.ttf'):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()
