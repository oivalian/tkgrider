
class Pack:
    y = 0
    x = 0
    iy = 0
    ix = 0
    s = 0


    @classmethod
    def packcol(cls, widget_list, max_col, y=None, x=None, iy=None, ix=None, s=""):
        row_pos = 0
        col_pos = 0
        for widget in widget_list:
            widget.grid(row=row_pos, column=col_pos, pady=y, padx=x, ipady=iy, ipadx=ix, sticky=s)
            col_pos += 1
            if col_pos == max_col:
                row_pos += 1
                col_pos = 0

    @classmethod
    def packrow(cls, widget_list, max_row, pady, padx, ipady, ipadx, sticky):
        row_pos = 0
        col_pos = 0
        for widget in widget_list:
            widget.grid(row=row_pos, column=col_pos, pady=pady, padyx=padx, ipady=ipady, ipadx=ipadx, sticky=sticky)
            row_pos += 1
            if row_pos == max_row:
                col_pos += 1
                row_pos = 0

