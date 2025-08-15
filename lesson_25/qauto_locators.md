# Локатори для сайту qauto2.forstudy.space

## XPath локатори (25 шт.)

1. //button[text()='Sign In']
2. //button[@type='submit']
3. //input[@name='email']
4. //input[@placeholder='Password']
5. //a[@href='/panel']
6. //h1[text()='Welcome to QAuto']
7. //div[@class='header']/*[@class='logo']
8. //ul[@class='nav']/li/a[text()='Home']
9. //ul[@class='nav']/li/a[contains(text(),'Garage')]
10. //div[@id='userMenu']//button[@class='btn']
11. //form[@id='loginForm']//input[@type='email']
12. //form[@id='loginForm']//input[@type='password']
13. //form[@id='loginForm']//button[text()='Login']
14. //div[contains(@class,'alert') and contains(text(),'Invalid')]
15. //footer//a[text()='Privacy Policy']
16. //header//nav//a[text()='About']
17. //div[@class='car-card'][1]//h2
18. //div[@class='car-card'][last()]//button[text()='Details']
19. //table[@id='carsList']//tr[1]//td[2]
20. //table[@id='carsList']//tr[2]//td[3]
21. //div[@class='modal']//h4[text()='Add new car']
22. //div[@class='modal']//button[text()='Close']
23. //section[@id='features']//h3[contains(text(),'Speed')]
24. //main//p[contains(text(),'automation')]
25. //span[@class='user-name']

## CSS локатори (25 шт.)

1. button:contains('Sign In')
2. button[type='submit']
3. input[name='email']
4. input[placeholder='Password']
5. a[href='/panel']
6. h1:contains('Welcome to QAuto')
7. .header .logo
8. ul.nav > li > a:contains('Home')
9. ul.nav > li > a:contains('Garage')
10. #userMenu button.btn
11. form#loginForm input[type='email']
12. form#loginForm input[type='password']
13. form#loginForm button:contains('Login')
14. div.alert:contains('Invalid')
15. footer a:contains('Privacy Policy')
16. header nav a:contains('About')
17. .car-card:nth-of-type(1) h2
18. .car-card:last-of-type button:contains('Details')
19. table#carsList tr:nth-of-type(1) td:nth-of-type(2)
20. table#carsList tr:nth-of-type(2) td:nth-of-type(3)
21. .modal h4:contains('Add new car')
22. .modal button:contains('Close')
23. section#features h3:contains('Speed')
24. main p:contains('automation')
25. span.user-name
