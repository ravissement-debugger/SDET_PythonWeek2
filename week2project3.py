try:

    def generate_test_report(test_cases):

        a = open('test_results.txt', 'w')

        failed = 0

        for test_case , result in test_cases.items():
            a.write(f"{test_case} :\n")
            if result['Status'].upper() == 'FAIL':
                failed += 1
                for test , endresult in result.items():
                    a.write(f"{test}\t{endresult}\n")
            else:
                for test , endresult in result.items():
                    a.write(f"{test}\t{endresult}\n")

        if failed != 0:
            a.write("BUILD REJECTED")
        else:
            a.write("BUILD SUCCESSFUL")


        a.close()





    test_cases = {

        "Login": {"Status" : "Pass", "Time" : 2 },
        "Signup": {"Status": "Pass", "Time" : 1.1 },
        "Logout": {"Status": "Fail", "Time": 1.3},
        "Api": {"Status": "Pass", "Time": 9},
        "Delete Account": {"Status": "Fail", "Time": 3}

    }


    def print_test_report():
        a = open('test_results.txt', 'r')

        for line in a.readlines():
            print(line)

        a.close()


    generate_test_report(test_cases)
    print_test_report()

except Exception as e:
    print(e)