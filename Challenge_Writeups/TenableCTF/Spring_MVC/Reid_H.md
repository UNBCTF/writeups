## Spring MVC 1 ##

    Attached is a zip archive containing the source code of a Spring MVC Java web application. Download and extract the archive.

    The goal is for you to analyze the code and construct HTTP requests to either (There are multiple sites due to high traffic volume):

        http://challenges.ctfd.io:30542/
        http://challenges.ctfd.io:30541/
        http://challenges.ctfd.io:30543/

    This could be accomplished using a web proxy tool such as OWASP ZAP or Burp Suite or your favorite scripting language. It's up to you how you retrieve the flags. Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

    If you would like to run the application locally, inside you'll find a README which instructs you on how to run the application. A pre-built WAR has been provided. The app was created and tested in the following environment:

    Ubuntu 20.04 LTS Release: 20.04 openjdk 14.0.2 2020-07-14 OpenJDK Runtime Environment (build 14.0.2+12-Ubuntu-120.04) OpenJDK 64-Bit Server VM (build 14.0.2+12-Ubuntu-120.04, mixed mode, sharing)

    When in doubt, read the Spring framework docs!

    Note: The flags in the provided source code have been changed in the live app.

## Solution ##

Let's jump in by downloading the source code and taking a look.

We can find the 'MainController.java' file in the 'src/main/java/com/tenable/ctf/mvc/' directory. Here is the contents:

```
  1   package com.tenable.ctf.mvc;
  1 
  2 import org.springframework.stereotype.Controller;
  3 import org.springframework.ui.Model;
  4 import org.springframework.web.servlet.ModelAndView;
  5 import org.springframework.web.bind.annotation.GetMapping;
  6 import org.springframework.web.bind.annotation.PostMapping;
  7 import org.springframework.web.bind.annotation.RequestMapping;
  8 import org.springframework.web.bind.annotation.RequestParam;
  9 import org.springframework.web.bind.annotation.RequestMethod;
 10 import org.springframework.web.bind.annotation.RequestHeader;
 11 import com.tenable.ctf.mvc.FlagService;
 12 import javax.servlet.http.HttpSession;
 13 
 14 @Controller
 15 public class MainController {
 16     private FlagService flags;
 17     public MainController() {
 18         this.flags = new FlagService();
 19     }
 20 
 21     @GetMapping("/")
 22     public String index(HttpSession session, Model model, @RequestParam(name="name", required=false, defaultValue="user") String name) {
 23         model.addAttribute("name", name);
 24         session.setAttribute("sessionFlag", flags.getFlag("session_flag"));
 25         return ".hello";
 26     }
 27 
 28     @GetMapping("/main")
 29         public ModelAndView getMain() {
 30         ModelAndView modelAndView = new ModelAndView("flag");
 31                 modelAndView.addObject("flag", flags.getFlag("spring_mvc_1"));  // get main
 32                 return modelAndView;
 33         }
 34 
 35     @PostMapping("/main")
 36         public String postMain(@RequestParam(name="magicWord", required=false, defaultValue="") String magicWord, Model model) {
 37         if (magicWord.equals("please"))
 38             model.addAttribute("flag", flags.getFlag("spring_mvc_3"));  // post main param 
 39         else
 40                     model.addAttribute("flag", flags.getFlag("spring_mvc_2"));  // post main
 41                 return "flag";
 42         }
 43 
 44     @PostMapping(path = "/main", consumes = "application/json")
 45     public String postMainJson(Model model) {
 46                 model.addAttribute("flag", flags.getFlag("spring_mvc_4"));  // post main flag json
 47                 return "flag";
 48         }
 49 
 50     @RequestMapping(path = "/main", method = RequestMethod.OPTIONS)
 51         public String optionsMain(Model model) {
 52                 model.addAttribute("flag", flags.getFlag("spring_mvc_5"));  // options main
 53                 return "flag";
 54         } 
 
 55     @RequestMapping(path = "/main", method = RequestMethod.GET, headers = "Magic-Word=please")
 56         public String headersMain(Model model) {
 57                 model.addAttribute("flag", flags.getFlag("spring_mvc_6"));  // headers main
 58                 return "flag";
 59         }
 60  }
```

Great, now we can see each method that has to be called in order to give us each flag for Spring MVC 1-6. After some research into the Spring framework, I know that `@GetMapping("/main")` means the following function is to be called in response to a HTTP GET request to the '/main' directory of the webpage. When we route to http://challenges.ctfd.io:30542/main, we're greeted with the following: flag{flag1_517d74}

## Spring MVC 2 ##

    See Spring MVC 1 for instructions.

    Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

## Solution ##

From the code shown in Spring MVC 1, we can see that an HTTP POST request is required to trigger the function to give us flags for Spring MVC 2 and 3. It seems as though Spring MVC 3 reqires a header of 'magicWord' equal to 'please' in order to recieve the flag; and, if this parameter is something else or not given, we receive flag 2.

Let's use cURL to create a HTTP POST request with `curl -X POST http://challenges.ctfd.io:30542/main`. It returns with the following:

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Tenable CTF: Spring MVC</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
        <p >flag{flag2_de3981}</p>
</body>
</html>
```

There's flag 2!

## Spring MVC 3 ##

    See Spring MVC 1 for directions.

    Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

## Solution ##

In Spring MVC 2, I mentioned that a HTTP POST request with a 'magicWord' parameter of 'please' was required to obtain flag 3. When I do this by running `curl -X POST -F 'magicWord=please' http://challenges.ctfd.io:30542/main`, I recieve:

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Tenable CTF: Spring MVC</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
        <p >flag{flag3_0d431e}</p>
</body>
</html>
```

Got it!

## Spring MVC 4 ##

    See Spring MVC 1 for directions.

    Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

## Solution ##

From the explanation given in Spring MVC 1, we can see that an HTTP POST request to '/main' is required. What's new is the 'consumes = "application/json"' parameter. After reading [this](https://stackoverflow.com/questions/7172784/how-do-i-post-json-data-with-curl) Stack Overflow post, I know that we must include a header in our request stating that we are passing JSON data (even though we're not actually transmitting any data). Let's do this with `curl -X POST -H 'Content-Type: application/json' http://challenges.ctfd.io:30542/main`. We recieve:

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Tenable CTF: Spring MVC</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
        <p >flag{flag4_695954}</p>
</body>
</html>
```

There it is!

## Spring MVC 5 ##

    See Spring MVC 1 for directions.

    Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

## Solution ##

It looks like we need to send an HTTP OPTIONS request to the website for flag 5. Let's try `curl -X OPTIONS http://challenges.ctfd.io:30542/main`. We get:

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Tenable CTF: Spring MVC</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
        <p >flag{flag5_70102b}</p>
</body>
</html>
```

Short and sweet.

## Spring MVC 6 ##    

    See Spring MVC 1 for directions.

    Please, no automated scanners or denial of service. Be nice to the application! This is an exercise in precision.

## Solution ##

Looks like this one is similar to Spring MVC 4 with the fact we need to use a header, though this one requires a HTTP GET request. When we run `curl -H 'Magic-Word: please' http://challenges.ctfd.io:30542/main`, we get:

```
<!DOCTYPE HTML>
<html>
<head>
    <title>Tenable CTF: Spring MVC</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
        <p >flag{flag5_70102b}</p>
</body>
</html>
```

All done!
