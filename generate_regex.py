class regex_generate:
  def convert_string_number_reg(self, value: str) -> str:
        """
        Returns a Regular Expression that matches this exact number or lower
        :param value: String Value of the Number in question
        :return: RegEx String
        """

        if value.__len__() == 0:
            #Guard Statement
            return None
        if value.__len__() == 1:
            if value == "0":
                return None
            elif value == "1":
                return "0"
            else:
                return f"[0-{value}]"

        #
        regex_statements = []
        octet = 0
        char_array = list(value)
        while octet < char_array.__len__():
            spot = 0
            s = ""
            for slice in char_array:
                if spot == octet:
                    if int(slice) == 0:
                        #print(f"error will robinson {slice}")
                        #s = s + "[0]"
                        pass
                    else:
                        s = s+f"{self.convert_string_number_reg(str(int(slice)-1))}"
                    pass
                if spot < octet:
                    s = s + f"[{slice}]"
                if spot > octet:
                    s = s + '\\d'
                    pass
                spot = spot + 1
            regex_statements.append(s)
            octet = octet + 1
        final_s = None
        for reg in regex_statements:
            if not final_s:
                final_s = f"({reg})"
            else:
                final_s = final_s + f"|({reg})"
        print(final_s)
        return final_s

    def convert_full_string(self, value: str) -> str:
        """
        This function converts a String representation of a software version into a Regular Expression

        :param value: The String value of the software version, delimited by "."
        :return: String Regular Expression
        """
        regex_statement = []
        version_split = value.split(".")

        octet = 0
        while octet < version_split.__len__():
            #print(f"process octet {octet} of {version_split.__len__()}")
            #print(version_split[octet])
            spot = 0
            new_slice = []
            for slice in version_split:
                if spot == octet:
                    new_slice.append(self.convert_string_number_reg(slice))
                if spot < octet:
                    new_slice.append(slice)
                if spot > octet:
                    new_slice.append("\\d*")
                spot = spot + 1

            s = None
            for i in new_slice:
                if s == None:
                    s = i
                else:
                    s = s + "\." + i
            #print(f"final s = {s}")
            regex_statement.append(s)
            octet = octet + 1
        final_regex = None
        for regex in regex_statement:
            if not final_regex:
                final_regex = f"(^{regex})"
            else:
                final_regex = final_regex + f"|(^{regex})"
            #print(regex)
        return final_regex
