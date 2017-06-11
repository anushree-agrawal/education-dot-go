from send import send_sms

# TODO: query the status of this phone number

users = {
    '+14088288498': ['Vibhav', 1, 0, False],
    '+15133311772': ['Rajat', 1, 0, False],
    '+16177101266': ['Parker', 1, 0, False],
    '+18324836840': ['Anushree', 1, 0, False],
    '+14054036409': ['Joseph', 2, 0, False]
}

courses = {
    0: 'new user',
    1: 'Sex Education All Ages',
    2: 'Introduction to Math Age 11-13',
    3: 'Intermediate Math Age 13-15',
    4: 'Advanced Math Age 15-17',
    5: 'Introduction to Biology Age 11-13',
    6: 'Advanced Biology Age 13-15',
    7: 'Introduction to Chemistry Age 11-13'
}

lessons = {
    1: {
        1: ("Lesson 1: Welcome to Sexual Education 101! We're very excited to have you and to help you understand your body and empower you to make safe, healthy sexual decisions. For our first course we'll be talking about the parts of the female reproductive system. The female reproductive system is comprised of three major parts: the vagina, the cervix, and the uterus. The vagina is a hollow tube that extends from the external opening to the cervix (the vulva is the very outside portion); the vulva contains the clitoris, and the urethera where urine is passed. The uterine lining is an inner part of the body that is shed during your menstrual cycle - we'll discuss this in lesson 5! The uterus is where the baby develops after intercourse (discussed in lesson 4). The ovaries connect the uterus to the fallopian tubes and this is where the female reproductive hormones--namely estrogen--are released during puberty.", None),
        2: ("Lesson 2: Welcome back to Sexual Education 101! Today we'll be talking about the male reproductive system. The male reproductive system includes the scrotum, testes, spermatic ducts, sex glands, and penis. These organs work together to produce sperm, the male gamete, and the other components of semen. These organs also work together to deliver semen out of the body and into the vagina where it can fertilize egg cells to produce offspring", None),
        3: ("Lesson 3: Welcome back to Sexual Education 101! Today's lesson is about sexual reproduction and intercourse. All offspring have genetic material from the mom and the dad. When a male and a female have sexual intercourse with each other, they share genetic information that is used to create offspring. Sexual intercourse, or copulation, is principally the insertion and thrusting of the penis, usually when erect, into the vagina for sexual pleasure, reproduction, or both. ", None),
        4: ("Lesson 4: Welcome back to Sexual Education 101! Today's education is about safe sex. Safe sex is incredibly important to make sure that you stay safe. One of the best tools to do this is to use a condom, a sheath-shaped barrier device used during sexual intercourse to reduce the probability of pregnancy or a sexually transmitted infection (STIs).", None)
    },
    2: {
        1: ("Welcome to Lesson 1: Introduction to Financial Mathematics. Math is a language that can be applied to a variety of different applications. It is a very powerful tool that can help you manage your money! Managing money in order to be able to buy and do the things you want is a skill that can be developed. If you are able to save money on a daily/weekly/monthly basis, it will help you have enough capital for large purchases such as a car or a phone. Math is important to budgeting and saving money because it helps give you an understanding of how much you need to save in order to buy the things you want." , None),
        2: ("Welcome to Lesson 2: Budgeting. The first step to saving money is to figure out how much you spend. The most important thing while budgeting is keeping track of all your expenses. Keep track of all your expenses that means every coffee, newspaper and snack you buy. Ideally, you can account for every penny. Once you have your data, organize the numbers by categories, such as gas, groceries and mortgage, and total each amount. Consider using your credit card or bank statements to help you with this. If you bank online, you may be able to filter your statements to easily break down your spending. Once you have an idea of what you spend in a month, you can begin to organize your recorded expenses into a workable budget. Your budget should outline how your expenses measure up to your income so you can plan your spending and limit overspending. In addition to your monthly expenses, be sure to factor in expenses that occur regularly but not every month.", None)
    }
}

quiz_content = {
    1: {
        1: "What is the external part of the female reproductive system? \nA. uterus \nB. vulva \nC. clitoris \nD. ovaries \nWhat part of the body is shed during your menstrual cycle? \nA. vagina \nB. uterine lining \nC. uterus \nD. estrogen",
        2: "Which organ is not part of the male reproductive system? \nA. testes \nB. scrotum \nC. vulva \nD. penis"
    }
}

ans = {
    1: {
        1: ['B', 'B'],
        2: ['C']
    }    
}


def get_user_info(phone_num):
    val = users[phone_num]
    name = val[0]; course_num = val[1];  class_num = val[2]; taking_quiz = val[3]
    global name; global class_num; global course_num; global taking_quiz

# status = '1.2'
# taking_quiz = False

def transition(phone_num, body):
    get_user_info(phone_num)
    if taking_quiz:
        ans_verify(phone_num, body)
    else:
        body = '/' + body
        body_split = body.lower().split()
        message = body_split[0]
        if message == '/help':
            help(phone_num)
        elif message == '/progress':
            progress(phone_num)
        elif message == '/resume':
            resume(phone_num)
        elif message == '/test' or message == '/exam' or message == '/quiz':
            quiz(phone_num)
            users[phone_num][3] = True

def not_in_db(phone_num):
    send_sms(phone_num,
             'Sorry this phone number is currently not registered in our database. Please contact a local refugee camp manager to sign up :)')

def in_db(phone_num):
    send_sms(phone_num,
             'Hi! Welcome to Education.Go, an on-the-go education system. To see all the courses that are available, type "C". If you need help, type "HELP". To return to the home text, type HOME.')

def progress(phone_num):
    send_sms(phone_num,
             'Current progress is at %s class number %s' % (courses[course_num], class_num))

def help(phone_num):
    assist = '+16177101267'
    send_sms(phone_num, 'Please contact this number for furthuer assistance: %s' % assist)

def resume(phone_num):
    to_send = lessons[course_num][class_num+1] # TODO: query the class information
    send_sms(phone_num, to_send)

def quiz(phone_num):
    to_send = quiz_content[course_num][class_num+1]
    send_sms(phone_num, to_send)

def ans_verify(phone_num, message):
    # set taking_quiz = False
    users[phone_num][3] = False
    # query the answers
    if ans[course_num][class_num+1] != [x.upper() for x in message.split(",")]:
        send_sms(phone_num, 'Sorry the answer was incorrect')
    else:
        send_sms(phone_num, 'Congratulations! You have entered the correct answer :)')
        # update the status of the phone number in db
        users[phone_num][2] += 1
        print(users[phone_num][2])
        to_send = lessons[users[phone_num][1]][users[phone_num][2]+1] # TODO: query the class information
        send_sms(phone_num, to_send)







