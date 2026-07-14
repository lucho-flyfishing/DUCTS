from tkinter import Frame, Canvas, Scrollbar

def make_scrollable(parent, bg='gray5'):
    """Return (container, inner). Pack `container` where the scrollable area
    goes; build your content inside `inner`. Content scrolls vertically when
    it's taller than the viewport, and fills the viewport when it's shorter."""
    container = Frame(parent, bg=bg)

    canvas = Canvas(container, bg=bg, highlightthickness=0)
    vscroll = Scrollbar(container, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=vscroll.set)

    vscroll.pack(side='right', fill='y')
    canvas.pack(side='left', expand=True, fill='both')

    inner = Frame(canvas, bg=bg)
    window_id = canvas.create_window((0, 0), window=inner, anchor='nw')

    _busy = {'on': False}   # re-entrancy guard so the two <Configure>s don't loop

    def _refresh(_=None):
        if _busy['on']:
            return
        _busy['on'] = True
        try:
            needed = inner.winfo_reqheight()
            available = canvas.winfo_height()
            # match width to canvas; stretch height to fill when content is short
            canvas.itemconfigure(window_id,
                                 width=canvas.winfo_width(),
                                 height=max(needed, available))
            canvas.configure(scrollregion=canvas.bbox('all'))
        finally:
            _busy['on'] = False

    canvas.bind('<Configure>', _refresh)
    inner.bind('<Configure>', _refresh)

    def _on_wheel(event):
        if not canvas.winfo_exists():      # screen may have been rebuilt
            return
        if event.num == 4:                 # Linux scroll up
            canvas.yview_scroll(-1, 'units')
        elif event.num == 5:               # Linux scroll down
            canvas.yview_scroll(1, 'units')
        elif event.delta:                  # Windows / macOS
            canvas.yview_scroll(-1 if event.delta > 0 else 1, 'units')

    # Global binding so the wheel works over the images too, not just blank areas.
    # Only one of these menus is on screen at a time, so re-binding on each build
    # just points the wheel at the current live canvas.
    canvas.bind_all('<MouseWheel>', _on_wheel)   # Windows / macOS
    canvas.bind_all('<Button-4>', _on_wheel)     # Linux
    canvas.bind_all('<Button-5>', _on_wheel)

    return container, inner