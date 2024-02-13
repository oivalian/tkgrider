
class Pack:

    @classmethod
    def packcol(cls, widget_list, max_col, y=None, x=None, iy=None, ix=None, stick=None, reverse=False):
        row_pos = 0
        col_pos = max_col if reverse else 0
        for widget in widget_list:
            widget.grid(row=row_pos, column=col_pos, pady=y, padx=x, ipady=iy, ipadx=ix, sticky=stick)
            if not reverse:
                col_pos += 1
                if col_pos == max_col:
                    row_pos += 1
                    col_pos = 0
            elif reverse:
                col_pos -= 1
                if col_pos == 0:
                    row_pos += 1
                    col_pos = max_col

    @classmethod
    def packrow(cls, widget_list, max_row, y=None, x=None, iy=None, ix=None, s=None, reverse=False):
        col_pos = 0
        row_pos = max_row if reverse else 0
        for widget in widget_list:
            widget.grid(row=row_pos, column=col_pos, pady=y, padx=x, ipady=iy, ipadx=ix, sticky=s)
            if not reverse:
                row_pos += 1
                if row_pos == max_row:
                    col_pos += 1
                    row_pos = 0
            elif reverse:
                row_pos -= 1
                if row_pos == 0:
                    col_pos += 1
                    row_pos = max_row

    @classmethod
    def pack(cls, widget_list, max_row, max_col, y=None, x=None, iy=None, ix=None, s=None):
        row_pos = 0
        col_pos = 0
        for widget in widget_list:
            widget.grid(row=row_pos, column=col_pos, pady=y, padx=x, ipady=iy, ipadx=ix, sticky=s)
            col_pos += 1
            if col_pos == max_col:
                col_pos = 0
                row_pos += 1
                if row_pos == max_row:
                    break
