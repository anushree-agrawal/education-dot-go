from send import send_sms
# TODO: query the status of this phone number

users = {
    '+14088288498': ['Vibhav', '1.1', False],
    '+15133311772': ['Rajat', '1.1', False],
    '+16177101266': ['Parker', '1.1', False],
    '+18324836840': ['Anushree', '1.1', False],
    '+14054036409': ['Joseph', '1.1', False]
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

def get_user_info(phone_num):
    global users
    val = users[phone_num]
    name = val[0]; status = val[1]; taking_quiz = val[2]
    course_num = int(status[0])
    class_num = int(status[2])
    global

# status = '1.2'
# taking_quiz = False


def transition(phone_num, body):
    if taking_quiz:
        ans_verify(phone_num, body)
    else:
        body_split = body.lower().split()
        message = body_split[0]
        if message == 'help':
            help(phone_num)
        elif message == 'progress':
            progress(phone_num)
        elif message == 'resume':
            resume(phone_num)
        elif message == 'test' or message == 'exam' or message == 'quiz':
            quiz(phone_num)


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
    send_sms(phone_num,
             'Please contact this number for furthuer assistance: %s' % assist)


def resume(phone_num):
    to_send = query_class_content(course_num + 1, class_num + 1) # TODO: query the class information
    send_sms(phone_num, to_send)


def quiz(phone_num):
    to_send = query_quiz_content(course_num + 1, class_num + 1) #
    send_sms(phone_num, to_send)


def ans_verify(phone_num, message):
    # TODO: set taking_quiz = False
    # TODO: query the answers
    if ans.lower() != message.lower():
        send_sms(phone_num, 'Sorry the answer was incorrect')
    else:
        send_sms(phone_num, 'Congratulations! You have entered the correct answer :)')
        # TODO: update the status of the phone number in db







