import re

def is_copyright_statement(s):
    rx = r'''(?xi)
    (?:©                                        # Start of a group: © symbol
    (?:\s*                                      #  Start of optional group: 0+ whitespaces
      (?:\d{4}                                  #   Start of optional group: 4 digits
        (?:\s*[-—–]\s*\d{4})?                   #     0+ spaces, dashes, spaces, 4 digits
      )?                                        #   End of group
      \s*Copyright                              #  Spaces and Copyright
    )?                                          #  End of group 
    |                                           #  OR 
    Copyright                                   
     (?:\s*                                     #  Start of optional group: 0+ whitespaces
       (?:\d{4}                                 #   Start of optional group: 4 digits
         (?:\s*[-—–]\s*\d{4})?                  #     0+ spaces, dashes, spaces, 4 digits
       )?\s*©                                   #   End of group, 0+ spaces, ©
     )?                                         #  End of group
    )                                           # End of group
    (?:\s*\d{4}(?:\s*[-—–]\s*\d{4})?)?          # Optional group, 9999 optionally followed with dash enclosed with whitespaces and then 9999
    \s*                                         # 0+ whitespaces
    (                                           # Start of a capturing group:
       .*?                                      # any 0+ chars other than linebreak chars, as few as possible, up to...
        (?=\s*[.|]|                             # 0+ spaces and then | or ., or
            \W*All\s+rights\s+reserved)         # All rights reserved with any 0+ non-word chars before it
      |                                         # or
       .*\b                                     # any 0+ chars other than linebreak chars, as many as possible
    )'''
    return bool(re.match(rx, s))

# Example usage:
print(is_copyright_statement("2007 Marvel"))  # Example of a copyright statement
print(is_copyright_statement("Some random text"))  # Example of non-copyright statement
