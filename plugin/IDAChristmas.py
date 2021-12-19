import idc
import idaapi
import idautils

GREEN = 0x247E32
DEEPGREEN = 0x15331B
RAINBOW = [0xFF0000, 0xFF8000, 0xFFFF00, 0xFFFF00, 0x00FF00]
BROWN = 0x5E3A12
SNOWRED = 0xffe0e0
SNOWGREEN = 0xe0ffe0

GRAD_GREEN = 0x1f001f
GRAD_RED = 0x000f0f

def get_bb_id(graph, ea):
    for block in graph:
        if block.startEA <= ea and block.endEA > ea:
            return block.id

def rgb2bgr(value): # to satisfy ida's color format    
    a = (value << 8 * 2) & 0xff0000
    b = (value) & 0xff00
    c = (value >> 8 * 2)
    return a|b|c

def colorize(bb, mode):
    i = 0
    if mode == 'star': 
        COLOR = SNOWRED
        for addr in Heads(bb.start_ea, bb.end_ea):
            set_color(addr, CIC_ITEM, rgb2bgr(COLOR))
            if (COLOR - GRAD_RED) & 0xff0000 != 0xff0000: # saturated red color
                continue
            # gradually brighten top to bottom    
            COLOR -= GRAD_RED
        
        
    elif mode == 'leaf': 
        COLOR = SNOWGREEN
        for addr in Heads(bb.start_ea, bb.end_ea):
            set_color(addr, CIC_ITEM, rgb2bgr(COLOR))
            if (COLOR - GRAD_GREEN) & 0xff00 != 0xff00: # saturated green color
                continue 
            # gradually brighten top to bottom    
            COLOR -= GRAD_GREEN
        
        
    elif mode == 'pole':
        for addr in Heads(bb.start_ea, bb.end_ea):
            # gradually brighten top to bottom
            set_color(addr, CIC_ITEM, rgb2bgr(BROWN))
    
# register keyboard shortcut Ctrl+t to colorize current function tree.
def hoykeyfunc():
    # get ea from mouse pointer 
    addr = idc.get_screen_ea()
    
    # get all basic block information from function
    function = idaapi.get_func(addr)
    flowchart = idaapi.FlowChart(function)
    basicblocks = []
    n_basicblocks = flowchart.size
    
    for i, bb in enumerate(flowchart):
        basicblocks.append(bb)

    # sort basicblocks by the starting address. 
    basicblocks.sort(key = lambda bb:bb.start_ea) # bb.start_ea / bb.end_ea
    
    # tree is consist of 1) uppermost star, 2) snowcapped leaves, 3) bottom pole 
    colorize(basicblocks[0], 'star') # star
    for i in range(1, n_basicblocks-1): colorize(basicblocks[i], 'leaf') # leaves
    colorize(basicblocks[n_basicblocks-1], 'pole') # pole
    
if __name__=='__main__':
    ida_expr.compile_idc_text('static py_hoykeyfunc() { RunPythonStatement("hoykeyfunc()"); }')
    # ida_kernwin.add_idc_hotkey("Ctrl+H", 'py_hoykeyfunc')
    ida_kernwin.add_idc_hotkey("`", 'py_hoykeyfunc')
    print ("done!")