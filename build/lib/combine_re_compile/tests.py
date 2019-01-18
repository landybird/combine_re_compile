import re

#
# DIGIT_PATTERN = re.compile(r"""
#     (?P<my_digit_pattern>        # start named group
#       \d+                        # 1 or more integers
#     )                            # close named group
#     """, re.VERBOSE)
#
#
#
# CHAR_PATTERN = re.compile(r"""
#     (?P<my_char_pattern>         # start named group
#       [a-z]                      # a character
#     )                            # close named group
#     """, re.VERBOSE)
#
#
# CHARS_PATTERN = re.compile(r"""
#     (?P<my_char_pattern>         # start named group
#       [a-z]+                     # a character
#     )                            # close named group
#     """, re.VERBOSE)

#
# r = CombinationPattern(DIGIT_PATTERN, CHAR_PATTERN, new_pattren_name="my_new_pattern").get_new_pattern
#
# s = "213213as2312"
# print(r.search(s).group('my_new_pattern'))


class CombinationPattern(object):

    def __init__(self, *args, **options):
        self.re_pattern = self.handle_re_expression_list(args)
        self.flags = self.handle_flags(args)
        self.pattern_name = self.handle_new_expression_name(options)




    @staticmethod
    def _move_annotation(s):
        """
        move annotation
        """
        move_annotation_re = re.compile(r"#.*")
        moved_result = move_annotation_re.sub("", s)
        return moved_result

    def handle_re_expression_list(self, args):
        """
        handle combine re expression
        """
        re_expression_list = list(map(self._move_annotation, [item.pattern for item in args]))

        new_re_expression_list = []
        for expression in re_expression_list:
            re_str_result = re.search(">(.*?)\)", expression, re.S)
            re_str = re_str_result.group(1)
            r = re_str.strip()
            new_re_expression_list.append(r)
        return "".join(new_re_expression_list)



    def handle_new_expression_name(self, options):
        return options["new_pattren_name"]


    def handle_flags(self, args):
        """
        keep one flag
        """
        flags_set = set([ item.flags for item in args])
        if len(flags_set) > 1:
            raise Exception("only support one flag")
        return flags_set.pop()


    @property
    def get_new_pattern(self):
        re_str = r"""
                 (?P<{0}>        
                    {1}                   
                 )         
                  """.format(self.pattern_name, self.re_pattern)

        return re.compile(re_str, self.flags)










