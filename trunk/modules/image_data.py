#### Movable Python
#### image_data.py

# Homepage : http://www.voidspace.org.uk/python/movpy/
# Download from : http://voidspace.tradebit.com

# Copyright Michael Foord, 2004-2006.
# Commercial software.

# For information about bugfixes, updates and support, 
# or for bug reports and feature requests - join the movpy mailing list.
# http://groups.google.com/group/movpy/
# Scripts maintained at http://www.voidspace.org.uk/python/index.shtml
# E-mail fuzzyman@voidspace.org.uk

movpyLogo = (
    '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\n')

arrow_right = (
            'R0lGODdhEAAQAPenAP8A/063MjmuJUKjJMXord7yzNHtusLnprPikZLUZFex'
            'L5/YhOr328bor5PUa4HMUnjJRHvKSXjLSGrLOUm2IR98D4zSceH00qPagG3E'
            'Nm/FOc7svMLmq2PCLVa+JE28I0bBHzSuFheFCtLtvKTbgmPAKGfCL4LNU/n9'
            '9////7LinEu8IkG6HTa3GDDAFB2RD4PMZ7rlm3DGOGnDMG/FOJfWcO746LHi'
            'n0i9ID65Gim6EBejCAphBZPSb43TX5XUbZnWcpjWcYzSZKjfkvv++7jlrEy/'
            'Liu4ERmxCCONE4PMWHfJQv3+/cHqvBq0ChmzCQ1tBhyCD2zCN2zHM9rxzdPv'
            'ydDux9LvyNDuxc/ux/n9+PP78nnSbxm0CAtlBRByCFu2KmXFLE29IiK0Dxqy'
            'ChyzDBmyCpXbjff89mPLWBmyCRq1CRerCAldBDqaG1vGKkW7HSW0DhuzCyG0'
            'EaDfmvj992XLWhq4CROUCBVqC0m+IEC9GzC3FB+yCja8KOH13+/67m3OYxq6'
            'CQxnBiKFDzS9Fie3ERyyCxaxBxexCBm0CRCEBxVqChV/Chy2Cxq5CRi0CBay'
            'BxCDBwZNBAlgBRORCBiwCRqzCRmxCRSWBwxoBQZJBAlbBQxsBgpeBQZMBAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAAGgAP8COQAA/zkBoAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLh//QAAAAAA'
            'AAACAMAAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj2AAEIFBhAgEEB'
            'AwYqBGCQQAEDBxAkUKBgoYAFDBo4eAAhgoQJFCoMFGDhAoYMGjZw6ODhA4gQ'
            'IgQKGEGihIkTKFKoWMGihYuYL2DEkDGDBo0aNlLcwJFDxw4eL3r4+AEkCBAh'
            'Q4ikKGLkCBIeSZQsSUG2LBOyTZw8gRJFyhQqVaxcwZJFS4otXLo88fIFTBgx'
            'Y8iUMXOGCZo0atawafPFzRs4ceTMoZOijh01au7gaQMgj549fPr4+QMoEOYn'
            'ggYJzEOokKFDiBJhVqNI0CLVAhk1cvQIUqQniu48kjRpISVKlSxdeoIpkyZN'
            'Cwdu4tSpk6dPCwMCACH+ADs=')

arrow_right_h = (
            'R0lGODdhEAAQAPf/AP8A/zWkHSOZEyqME7XhmNTuvcTnp7HgkJ/ZeHnHST2d'
            'G4jMauP00LbhmnrHUGe9OF26LGC7MF28L0+8IzCjEQ9iBnPFVtjwxYzPZlK0'
            'IFS1I8DmqrHelkixGTysEzSqEi2wDx+ZCgprA8Xnqo7QaEivFkyxG2i/Off8'
            '9P///57ZhDKqESmnDiCkCxyvCQ54Bmm9TKfdg1W2Ik6yHFS1In/KVen24Z3Z'
            'iC+rECemDBanBgqMAwNGAXrFVHTGRH3HUoHKV4DKVnPFSZLVefr++qXdlzOt'
            'GhilBwydAxJ0CGm9Ply6Kvz+/LDjqgygAwyfAwVSAg1oBlGxIVG3Hs/tv8bq'
            'usLpt8XquMLptcHpt/f89u/67l7FVARKAQZXA0GjF0q1GDSrERGgBgyeAw2f'
            'BH3QdPT780i8PgyhAwqWAwNCASOCDUG2Fy2pDhOgBRGgB4nVgvb89Eq8QAyl'
            'Awh7AwlPBDCsECirDRykCQ+eAyCqFtjy1er46VLASAynAwRMAhFrBh+rChWk'
            'Bw2eBAqdAgqdAwZqAglPAwllAw2jBAymAwugAwqeAgZpAgI0AQNFAQh4Awuc'
            'Awl+AgRNAQIwAQNBAQRRAgNDAQIzAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAADd8AP8CMgAA/zI3fAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLx//QAAAAAA'
            'AAACAMQAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAj1AAEIFBhAgEEB'
            'AwYqBGCQQAEDBxAkUKBgoYAFDBo4eAAhgoQJFCoMFGDhAoYMGjZw6ODhA4gQ'
            'IgQKGEGihIkTKFKoWMGihYuYL2DEkDGDBo0aNlLcwJFDxw4eL3r4+AEkCBAh'
            'Q4ikKGLkCBIeSZQsSUG2LBOyTZw8gRJFyhQqVaxcwZJFS4otXNR28fIFTBgx'
            'Y8iMKcPEzJkxaNKo8bKGTRs3ZN7ASRFHzpgxc+ioAVDHzh08efTs4dPn8hM/'
            'fwTWARRI0CBChS6PceLHUGqBhxAlUrSI0RMncxQ1crTw0SNIkZ48QSJp0qSF'
            'AylVsmTpEqaFAQEAIf4AOw==')

open_document = (
             'R0lGODdhEAAQAPf/AP8A/xiFDDi1IUO3Kkm6Lb6NB2XQQP7+/v/+pbaMB9y3'
            'Q3ndTlS6Nv/7oP77oP76of77oYThVm7NR/71m/72mv31m/72m2zORojkWYjh'
            'WJTrYWXBQP7wk/3wk8WXFn/ZUpftYmXEQfzqivPcd8acIv///f73yP73yV28'
            'PPv53vn21vzjguDDZf3wrPzrjf3rjdq7TPn3tuDKbfvdeceZGPPfmvvnkvvk'
            'hPzkg/zkhPvkg/zlhNq5SPn0s/rWcvzqrvvcefvcevrcedm1RPnxrue8TNGo'
            'OfvioPrUb/nUb/rUbvnUbtmxPuvXhNGhJefHcvrXhfnNZvnNZfjNZfnOZtit'
            'OQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAI4gAP8COwAA/zuOIAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLJ//QAAAAAA'
            'AAACALoAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAi8AAEIFBigYICB'
            'CBMSNKiwIYAAAg46RBhgAAGJAwtoLEDRAEYABQ4gGJlAgckACxhIDNnAgYMH'
            'EAwGiCDBYIEJFChUsEBhQoALGDJo2HCwAIcOHjZqDPABRIgAG0WMIFHCxImr'
            'JgKgCJBChcYVCli0cOHixYuyAWDEkKFxBo0aNm7gwJEDh44dPHpwLOCjwA8g'
            'gAEHESJkCJG9RYwcQZJESRIkkJcwabLXyRMoUaRoniJlCpUqHAUqHa1UYEAA'
            'If4AOw==')

open_document_h = (
            'R0lGODdhEAAQAPf/AP8A/wtrBCKhESukFzCnGax0AkrCKP7+/v/+j6NzAtGk'
            'K17TNTqnIP/6if76if74iv76imrYPFO/Lv7yg/7zgvzyg/7zg1HALW7cP27Y'
            'PnvlRkqwKP7revzrerV/CmXOOH/nR0q0KfvjcO/RXLaEEf///P70uP70ukKq'
            'Jfr31PfzyvvaaNeySvzrl/vldPzldM+pM/f0o9e7UvrTXreBC+/Vgvrgefrc'
            'avvcafvcavrcafvdas+mL/fwn/jKV/vjmfrRXvrRX/jRXs6hLPftmeCqM8SS'
            'I/rZifjHVPfHVPjHU/fHU86dJ+XLasSKE+C3V/jLa/e/S/e/Sva/SvfAS8yY'
            'IwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAO+kAP8COwAA/zvvpAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLZ//QAAAAAA'
            'AAACAL4AAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAi8AAEIFBigYICB'
            'CBMSNKiwIYAAAg46RBhgAAGJAwtoLEDRAEYABQ4gGJlAgckACxhIDNnAgYMH'
            'EAwGiCDBYIEJFChUsEBhQoALGDJo2HCwAIcOHjZqDPABRIgAG0WMIFHCxImr'
            'JgKgCJBChcYVCli0cOHixYuyAWDEkKFxBo0aNm7gwJEDh44dPHpwLOCjwA8g'
            'gAEHESJkCJG9RYwcQZJESRIkkJcwabLXyRMoUaRoniJlCpUqHAUqHa1UYEAA'
            'If4AOw==')

properties = (
            'R0lGODdhEAAQAPeTAP8A/6SmwtDm/6y5ycfO39Po//T4+9fq/9na5trs/5ai'
            'sPs1A97u/6m1xai0w6ezwuLw/wAzmREzj8g1IuXx//7+/vx3Vunz/v7q5P7g'
            '2f2smFk0ZOz1/vx0UvtCFP3JvP7y7/tHGvxyTwQzl/D3/v7e1vxoQ/xmQPs2'
            'BPT5/v77+vyYfvx6Wff7/v2kjv3GuPv8/mwAYQBcAGkAZwBmADEAXAA2AHAA'
            'XAByAHAAbwBlAHQAcgBpAHMAZQBfAG8AZABjADEAXwA2AGcALgBpAAAAZgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAANJ4AP8COwAA/zvSeAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLR//QAAAAAA'
            'AAACALwAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAifAAEACECwIEGB'
            'CBEGEMCQ4QACARIqLECR4gADECUOPMCR40UDCCImDJCgpEkFKBUEWKCQgcuX'
            'DRw8WEBTIYQIOHNKmLBApMAAFCJUGDrUwgIKPgdeiIAhw1ANCzZcSBqAQ4QO'
            'Hj6ACCFiBAeqJCKUMLHgBIoMEUhQTSFUxYoFLCpESEG1hdChLl7IbUEVRs6/'
            'EWD0hUG4cGGqBhMfBBAQACH+ADs=')

properties_h = (
            'R0lGODdhEAAQAPf/AP8A/46QscLe/5emurfA1cbh//D2+svj/87P3s/m/36L'
            'nPofAdTp/5OhtZKgspGfsdnr/wAegQcedrgfEd3t//7+/vtcPOLv/v7j3P7X'
            'zvyXgD8fSeby/vtZOPoqCfy6qv7u6vouDPtXNQEef+v0/v7UyvtNK/tLKPog'
            'AfD3/v76+PuAZPtfP/T6/vyOdfy2pfr7/mwAYQBcAGkAZwBmADEAXAA2AHAA'
            'XAByAHAAbwBlAHQAcgBpAHMAZQBfAG8AZABjADEAXwA2AGgAXwAuAGkAZwBm'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAH54AP8CPAAA/zx+eAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLh//QAAAAAA'
            'AAACAMAAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgACFNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAifAAEACECwIEGB'
            'CBEGEMCQ4QACARIqLECR4gADECUOPMCR40UDCCImDJCgpEkFKBUEWKCQgcuX'
            'DRw8WEBTIYQIOHNKmLBApMAAFCJUGDrUwgIKPgdeiIAhw1ANCzZcSBqAQ4QO'
            'Hj6ACCFiBAeqJCKUMLHgBIoMEUhQTSFUxYoFLCpESEG1hdChLl7IbUEVRs6/'
            'EWD0hUG4cGGqBhMfBBAQACH+ADs=')

folder = (
             'R0lGODdhEAAQAPdjAP8A/76NB/7+/v/+pf/7oP77oP76of77of76oP/7obqJ'
            'Cf71m/72mv31m/72m/32mv7wk/3wk8WXFvzqivPcd8ecIf///v33yP33yf73'
            'yf73yObVm/7+6vjz0vzjgty3Q+DCZfzwq/zrjf3rjdq7TPPwyfvdeceZGPPf'
            'mvznkvvkhPzkg/zkhPvkg/zlhNq5SMSWFPrWcvzprvvcefvcevrcedm1ROe8'
            'TNGoOfvioPrUb/nUb/rUbvnUbtmxPtGhJejGcfrXhPnNZvnNZfjNZfnOZtit'
            'OsmZGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAABEAAP8CNwAA/zcRAAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfK5//QAAAAAA'
            'AAACALYAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAihAAEIHEiwoMGD'
            'CBMqXBigYQCGAgZIdOiQYAABBAoUMHAAwYEEBBIoGBhgAQMGDRwwWPDAJIOR'
            'AgNAiCCBok2KEyhUsHABA4YMGjBo2MChQ0MPH0CEECFixIimIkiUKNHQxAkU'
            'KVSsWMFiRQsXL0rAABAgRgAZM9KmpVGjhg2qZG/gyKFjB48dOvL28AE3wA8g'
            'QYQMGUxkCJEiRo6QvGlzYEAAIf4AOw=='
)

folder_h = (
             'R0lGODdhEAAQAPdIAP8A/6x0Av7+/v/+j//6if76if74iv76iv74if/6iqdv'
            'A/7yg/7zgvzyg/7zg/zzgv7revzrerV/CvvjcO/RXLeEEf///vz0uPz0uv70'
            'uv70uN7Jg/7+4/bvxfvaaNGkK9exSvvrlvvldPzldM+pM+/ruvrTXreBC+/V'
            'gvvgefrcavvcafvcavrcafvdas+mL7R+CfjKV/vimfrRXvrRX/jRXs6hLOCq'
            'M8SSI/rZifjHVPfHVPjHU/fHU86dJ8SKE+G2VvjLave/S/e/Sva/SvfAS8yY'
            'I7qBDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAANn8AAAAEgAAAJEFyCCYfMgAFQAS2pEFURN4fG0AFXyRBQAAAAQ9AAB8'
            'kQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAgAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAANSHNNtZdxgAAAAS2BUAANuQABgAEnyQ'
            '7pFAwP//fLv//3yRQAHWjgBFAAwAAAAS2hAAgNuQwBgAEnyQ7pEFcP//fAD/'
            '/wAAAJEEPdtAfHUAEnyBCwAAAAAIAP8CMgAA/zIACAAYAgAAAAAAABLbKABA'
            'AAAAAAAAABLbDAAAAAAAAAAAAAAAAAAMAAIAAAAAAJABAfwAfLJ//QAAAAAA'
            'AAACALoAAAIaABUgoAAAAKAAAAAVIAAABeLfAGR8gAAS24AaT+XlfEh8kHyB'
            'DgABqNuIAJAAEgAS2wAACCH5BAkAAAAALAAAAAAQABAAAAihAAEIHEiwoMGD'
            'CBMqXBigYQCGAgZIdOiQYAABBAoUMHAAwYEEBBIoGBhgAQMGDRwwWPDAJIOR'
            'AgNAiCCBok2KEyhUsHABA4YMGjBo2MChQ0MPH0CEECFixIimIkiUKNHQxAkU'
            'KVSsWMFiRQsXL0rAABAgRgAZM9KmpVGjhg2qZG/gyKFjB48dOvL28AE3wA8g'
            'QYQMGUxkCJEiRo6QvGlzYEAAIf4AOw=='
)

rocket = (
            'R0lGODlhFAAUAPeWAP7+/vz8/MYAAKurq+np6aioqPDw8Pv6+v/+/vHZ2vLv'
            '770AAL0DA7VtbdPPzfj4+MC+vsC8vPHv7+vV1eDExLgAAMc4ONq0tEVCQqkB'
            'AX19fdzFxdm3tv38/OS2tpeksero5/v4+J88PV5nZ8Z0dEGHvX5JSqKiosx6'
            'ej92mDdviv7//wWAxdPS0t7Z1pYAAObS0XoAAGgWFuPj4+jV1QCD09vCwtnc'
            '3KuqqlFQUJWZmZWVlcBiYuCsrCkzMjQRENnZ2RkjInolJs0AAN28u/X19c3L'
            'yZxgYOHDw3tDQs2Ehb1WV81XV1wYGJkAAIVERM0LC8kMDFoUFIhTU/n5+fLy'
            '8sU8PP39/aMKC9PT06AdHagVFbVBQWwAAHpBQHFvbnx/gjlGTswSEri4u5We'
            'qbirqytPX+nk5ZycnfPz8/3//21qZx0REkx2lt3V1UkJCMjIyNfX1/37+5GL'
            'iX9bXL8AAE5GQcvIxtDQ0L5ERffk5U1daPDp6rnCw/Pp6c9pbDyDt7IfIOPE'
            'xUgICP78/NTU03l5eYAKC5GMi8EAAN3d3YiJiu7Fxfz7+9Wxsdzb2/z5+b2O'
            'jc7OzvHj5M/Pz////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAACH5BAEAAJYALAAAAAAUABQAAAjsAC0JHEiwYIAq'
            'WSgVXEjwwQw8BQYwXAjAgCQgcXbAmUjwiiIjIAgM0FCEo0AAj8Z8IHPCUIFK'
            'JisRcNCmBKA9a9JMlFOpkoRCLlLUYBHmDkyCCPwIUkIiUoQbEMCoMIMIQMED'
            'PSxAGbJARJ8yi77YmUOl4CQmAgTUSbRFR4MnI3LgCFCQBhcrf/JgcULniAwf'
            'GFocJXhhAiRLIZCYSNIkyA8pZ0wKDDDlDZtBXQ65kVyJiBc0QmK80KLAJAAb'
            'jgxY8pChAo8VJg9sICRQjxgGMDgjGJggyhI1kgsyCsQnOMFKKCgMNt6BQyOT'
            'AQEAOw=='
)