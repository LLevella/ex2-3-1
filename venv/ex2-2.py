import myfunclib



def main():
    str_file_begin_name = ["newsafr", "newscy", "newsfr", "newsit"]
    str_file_end_name = ["txt", "json", "xml"]
    for s_end in str_file_end_name:
        for s_beg in str_file_begin_name:
            print(s_beg, s_end, myfunclib.file_analys(s_beg, s_end))

main()