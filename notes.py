# data structure of each stage list: [stage title, [section0_title, [section0_bullet0, section0_bullet1, ...]], [section1], ...]

stage0 = ['Stage 0: Basics of Web and HTML',
    [['WWW (World Wide Web)', ['Collection of mainly HTML docs.']],
    ['HTML Components', ['Text content is what you see.',
                         'Markup determines appearance.']
    ],
    ['Tags', ['Elements are everything inside tag, including tag.',
              "Void tags have no content, don't require closing brackets.",
              "Block vs inline: block create invisible box; inline does not.",
              "Attributes are inside tag, have value, eg. href, source."]
    ],
    ["HTML Document Structure", ["doctype: html, tells browser it is an html doc.",
                                  "head: head, contains metadata like css, js.",
                                  "body: body, main part that is displayed."]
    ]]

]

stage1= ["Stage 1: HTML, CSS (very boring)",

[['What is a Website?', ['HTML - structure.',
                        'CSS - style.',
                        'Javascript - interaction.']

],
['More HTML Structure', ['DOM (Document Object Model) - tree structure.',
                         'Page is composed of rectangles: margin, border, padding, content.']
],
['CSS (Cascading Style Sheets)', ['CSS helps us avoid repetition. Repetition leads to mistakes and carpal.',
                                  'Most specific rule governs.',
                                  'Components: selector, property, value.',
                                  '3 ways to add CSS: 1) add element in head, 2) link css file in head 3)inline(sucks).',
                                  'Size boxes with px or % for margin, border, etc.',
                                  'box-sizing to set size for all components of box.',
                                  'flex positions box.']
],
['Code, Test, Refine', ['Find Boxes.',
                        'Find style and semantic patterns.',
                        'Write HTML.',
                        'Write styles: big to small.']
]]
]

stage2 = ["Stage 2: Intro to Programming",
          [["Basics", ["A computer is a universal machine.",
                      "A program is a sequence of steps that tells a computer how to get something done.",
                      "Programing languages are how we instruct computers.",
                      "Code is interpreted or compiled so that the computer can read it.",
                      "Languages: unambiguous (unlike garbage human langs), grammar.",
                      "An 'expression' in python is a legal statement."]
          ],
          ["Variables", ["A variable is a name that can be assigned different values.",
                         "An '=' sign in python means variable is assigned to that value; not equal to that value."]
          ],
          ["Functions", ["Functions take input, do something with it, and return output.",
                         "Parameters can be passed to functions."]
          ],
          ["Conditionals", ["if statements",
                            "while loops",
                            "Conditional statements are more fun."]
          ],
          ["Lists", ["Lists help you structure data.",
                     "Lists are mutable (strings are a mess).",
                     "You can have nested lists until they drive you insane (like now).",
                     "Looping through lists is fun and relaxing."]
          ]]
]

stage3 = ["Stage 3: Object Oriented Programming (OOP)",
          [["What is OOP?", ["A class is a blueprint. It describes how to build something: 1)data 2)functions.",
                             "An object is an instance of a class; it's built according to the class blueprint. Seems simple so why act like it's a big deal?",
                             "Classes and objects (OOP) help us avoid repetition by allowing reuse of code.",
                             "We create an object of a class, and know that it has all the data and can perform all the procedures defined in the class."
                             ]

           ],

           ["Classes", [ "Implement your class in one module and implement use of it (create objects, etc.) in a different module.",
                         "Weird function,__init__,(from initialize) is a special function reserved in python to create new instances of classes.",
                         "Each class must have an init function.",
                         "init intializes a space in memory to store the new object.",
                         "init is called the 'constructor' function.",
                         "init always takes the parameter 'self' which is the object being created.",
                         "init can also take other parameters which is the data that can vary between objects of the same class.",
                         "Assign these arguments to variables with 'self' in front. Those variables become 'instance variables' rather than 'local variables.'",
                         "Other functions defined inside of class, are called 'instance functions.'",
                         "Class Variables are defined at the class level, i.e. not inside of the instance functions or _init__ function. Their names should be uppercase.",
                         "Python has default class variables such as __doc__, __bases__."
                         ]
            ],


           ["Objects", ["Import the class module.",
                        "Assign a variable to 'filename.Classname'(note: Class names are capitalized; functions are not).",
                        "Pass the arguments required (self is not required).",
                        "Python will call the class/init function to create the object and assign it to your variable.",
                        "Call data or function of the object with objectname.data/function, e.g. bestmovie.title, bestmovie.show_trailer()."
                        ]
            ],

            ["Inheritance", ["A child class can inherit from the parent class. That means it has all the attributes (data, function) of the parent class.",
                            "Pass parent, like you would a parameter, to tell Python that child class inherits from parent. Example: def Sapien(Homo):",
                            "Inside the child constructor, call the parent constructor.",
                            "The child constructor must take all the arguments which the parent constructor takes.",
                            "The child constructor can also take additional arguments which the parent does not. These parameters must be defined in the child init.",
                            "The child class can also have its own functions.",
                            "Method overriding: If a child function bears the same name of a parent function, the child function overrides."
                            ]
            ],

           ["Libraries", ["A Module is a .py file containing python code.",
                         "A Package is a folder that contains modules that together solve some problem. A package might also contain sub-folders (sub-packages?).",
                         "Python Standard Library (PSL) are the packages included when you download python.",
                         "Third party packages can be created by any bozo; they must be downloaded separately.",
                         "Built-in functions are the most common procedures in PSL; they've been set to always be available, e.g. open()",
                         "To use non-built-in functions, we must 'import' its module.",
                         "Avoid typing the name of the module every time by using 'from' to import specific folders, attributes (variables, procedures, classes). Example: 1) import module; x = module.foo() 2): from module import foo; x = foo().",
                         "Seems you can't tell from the syntax what you are importing (package, module, variable, or function) except for a class cause it's capitalized, e.g. 'from twilio.rest import TwilioRestClient'."
                         ]
            ]
           ]

]

stage4 = ["Stage 4: Full Stack",
          [["Networks", ["Network: communication between all nodes is possible even though nodes are not all connected.",
                         "Elements: encoding, routing, priority.",
                         "Measuring network speed: 1) Latency - time needed for bit to reach destination, 2) Bandwidth - number of bits that can be sent at a time, e.g. Mbps.",
                         "Base unit for encoding is the 'bit' which is one yes/no question.",
                         "Encoding data is most efficient when chance of yes or no is equal. Adding 1 more bit doubles the amount of information that can be encoded.",
                         "Routing is done by routers. They figure out best path ... somehow.",
                         "No general rule on internet for priority ...good luck!"
                         ]
          ],
           ["URL Anatomy", ["Uniform Resource Locator (URL) components: 1)protocol 2)host 3)path 4)port 5)query 6)fragment.",
                             "Protocol: The procedure that will guide the communication. Examples: http, ftp.",
                             "Host: IP address or domain name",
                             "Path: Everything after .com, .net, etc.",
                             "Port: Default is 80, otherwise specify.",
                             "Query (GET) Parameters: When you request a path from a server, the query parameter adds extra information. Query parameters have values. First QP is separated by '?', rest by '&'",
                             "Fragment: shows only a part of the object; doesn't get sent to the sever, only in the browser; comes after '#'"
                            ]

           ],

           ["HTTP", ["HTTP Request Components: 1) Request line 2) Headers. Example: GET/foo HTTP1.1",
                    "Request Line Components: 1)Method 2)Path 3)Version",
                    "Method: e.g. GET, POST.",
                    "Path: The document we are requesting from the server. Includes query parameters but not fragment",
                    "Version: e.g. HTTP/1.1",
                    "Request Headers: Format is 'name:value'",
                    "Header Types: 1) Host 2) User-Agent",
                    "Host: Why do we need this when we are already connected to host? Cause web servers may have multiple names.",
                    "User-Agent: Tells who is making request, e.g. firefox, googlebot; a host can block bad user-agents.",
                    "HTTP Response Components: 1) Status Line 2)Status Code 3) Reason phrase. Example: HTTP1.1/200 OK",
                    "Status Line Components: 1)version 2) status code 3) reason phrase",
                    "Common Status Codes: 200 = ok; 302 = found (do something different to get doc?); 404 = not found (browser side error); 500 = server error (server side error).",
                    "Response Headers: 1) Date 2) Server (don't include for security) 3) Content type (eg text/html, img/gif) 4) Content length.",
                    "Servers: 2 types of Responses: 1) Static - pre-written content 2) Dynamic - content generated on the fly by web app.",
                    "GET (default method): parameters in URL so bounded by max URL length; for fetching data so good to cache.",
                    "POST: parameters in request body (after req headers) so NOT bounded by max URL length; for updating data so DO NOT cache."
                    ]
            ],

           ["HTML Forms", ["Useful Elements: form, input, label, option, select",
                          "Useful parameters for input element: type ('submit', 'password', 'checkboxes', 'radio'); value; name: sets name of parameter",
                          "Never going to remember all these elements/parameters/values."
                          ]
            ],

           ["webapp2 Framework", ["Has 2 parts: 1) contains the code needed to handle http requests and builds responses. 2)Has a 'WSGIApplication instance' that sends requests to handles based on the URL(wth?).",
                                 "A main py file is required. It imports webapp2. Although webapp2 'module not found' when I run the .py file, somehow it works.",
                                 "yaml file also required. It contains application ID which is globally unique for each project.",
                                 "DOB Example: 1) user sends GET(form) 2) server returns form data 3)user sends POST(data) 4)server validates 5) updates server or resends form data along with error."
                                 ]
            ],

           ["Validation", ["When allowing POSTs, user may enter blank fields or incorrect data (eg March 41).",
                           "Anticipate user errors by checking for things like blanks, out of range data, spelling mistakes. Either correct them or send  error messages to improve user experience.",
                           "Worse, user can send HTML code to manipulate your website; even when using HTML elements with built-in limitations(eg checkboxes) user can still send junk.",
                           "Server must escape 4 dangerous symbols to maintain site security: 1) quote 2) amper 3) less than 4) greater than.",
                           "Better to use built in escape functions (eg templates or cgi module) than to create your own.,"
                           ]
            ],

           ["Jinja Template", ["Templates are libraries for creating complex strings (usually HTML) which are hard to do with Python.",
                               "Templates also help you avoid repetition by facilitating string substitution.",
                               "Jinja2 is a template that is built into google app engine",
                               "Add library to yaml and import python module (if something is wrong with python, page will not load; check errors in log console.",
                               "Jinja2 allows you to insert python snippets into regular html.",
                               "The python code in jinja2 is a bit different from regular python code, eg curly braces, 'endif'; basically a new language.",
                               "Rules of thumb when using templates: 1) use builtin safety features (eg autoescape) 2) minimize python in template 3) minimize html in main code.",
                               "You can have one template html file inherit from another with 'extends'."
                              ]
            ],

            ["Misc Python from Steve", ["Creating dictionaries from list: mydict = dict((e, e) for e in mylist)",
                                        "String substitution with value from dictionary keyword: 'Capital of %(country)s'; country is key in a dictionary, eg 'spain'",
                                        "Unexplained: *args, **params. Something to do with passing arguments to function when you aren't sure how many there will be.",
                                        "Steve doesn't have his functions explicitly 'return None'",
                                        "n = n and int(n): means if n (has a value, i.e. not None), then get int(n).",
                                        "Call 'get' on python dicts so that if the kw is not in dict, it will return none."
                                        ]
            ],

           ["Databases", ["A database stores and retrieves data",
                          "Databases are organized into tables which are composed of columns and rows.",
                          "Relational (SQL language) dbs examples: PostgreSQL, MySQL, SQLite, Oracle.",
                          "Non-relational dbs examples: Google App Engine, Amazon Dynamo, NoSql(eg mongo)."
                          ]
            ],

           ["SQL(Structured Query Language)", ["SQL is a language for retrieving data from db",
                                               "SQL query: SELECT/column/FROM/table/WHERE/constraint.",
                                               "Use boolean to add more constraints.",
                                               "ORDER clause sorts our rows by something.",
                                               "JOINS are used to get data based on constraints from multiple tables. Rarely used.",
                                               "Use indices to make queries faster: Hashtables fast but not sorted; Trees slower but sorted",
                                               "ACID: Atomicity, Consistency, Isolation, Durability"
                                               ]
           ]


        ]
]

all_stages = [stage0, stage1, stage2, stage3, stage4]
