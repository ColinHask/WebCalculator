import re
from playwright.sync_api import Page, expect

# MethodName_StateUnderTest_ExpectedBehavior

# preq-E2E-TEST-5	Verify the page title is "Calculator".
def test_CalculatorWebUi_PageTitle_IsCalculator(page: Page):
    #arrange
    expected_value = "Calculator"

    #act
    page.goto("http://127.0.0.1:5000")

    #assert
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile(expected_value))

# preq-E2E-TEST-6	From the application's default state, compute the sample standard deviation for 9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4. Verify that the result is 3.060787652326.
def test_StDevUi_NumberInput_CorrectResult(page: Page):
    #arrange
    expected_value = "3.060787652326"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("9\n2\n5\n4\n12\n7\n8\n11\n9\n3\n7\n4\n12\n5\n4\n10\n9\n6\n9\n4")
    page.get_by_role("button", name="Compute Sample Standard Deviation | one value per line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))

# preq-E2E-TEST-7	From the application's default state, attempt to compute the population standard deviation with an empty list. Verify the error message is shown.
def test_StDevUi_EmptyInput_ErrorMessage(page: Page):
    #arrange
    expected_value = "Invalid input"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("")
    page.get_by_role("button", name="Compute Population Standard Deviation | one value per line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))

# preq-E2E-TEST-8	From the application's default state, attempt to compute the sample standard deviation with a single value. Verify the error message is shown.
def test_StDevUi_SingleInput_ErrorMessage(page: Page):
    #arrange
    expected_value = "Invalid entry, At least two data points are needed for sample standard deviation."

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("5")
    page.get_by_role("button", name="Compute Sample Standard Deviation | one value per line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))

# preq-E2E-TEST-9	From the application's default state, compute the mean for 9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4. Verify that the result is 7.
def test_MeanUi_NumberInput_CorrectResult(page: Page):
    #arrange
    expected_value = "7"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("9\n2\n5\n4\n12\n7\n8\n11\n9\n3\n7\n4\n12\n5\n4\n10\n9\n6\n9\n4")
    page.get_by_role("button", name="Compute Mean | one value per line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))

# preq-E2E-TEST-10	From the application's default state, compute the z-score for 5.5 with a mean of 7 and a standard deviation of 3.060787652326. Verify that the result is -0.49007.

def test_ZScoreUi_NumberInput_CorrectResult(page: Page):
    #arrange
    expected_value = "-0.490069"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("5.5, 7, 3.060787652326")
    page.get_by_role("button", name="Compute Z Score | value, mean, stdDev on one line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))

# preq-E2E-TEST-11	From the application's default state, compute the single linear regression formula for the following 12 X,Y pairs. Verify the result is y = -0.04596X + 6.9336.
# 5,3
# 3,2
# 2,15
# 1,12.3
# 7.5,-3
# 4,5
# 3,17
# 4,3
# 6.42,4
# 34,5
# 12,17
# 3,-1

def test_LinearRegressionUi_XYInput_CorrectResult(page: Page):
    #arrange
    expected_value = "y = -0.0459615329x + 6.9335877814"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("""5,3
3,2
2,15
1,12.3
7.5,-3
4,5
3,17
4,3
6.42,4
34,5
12,17
3,-1""")

    page.get_by_role("button", name="Compute Single Linear Regression Formula | one x,y pair per line").click()
    msgboard = page.locator("#MsgBoard")


    #assert
    expect(msgboard).to_contain_text(expected_value)

# preq-E2E-TEST-12	From the application's default state, predict the Y value for the regression values X=6, M=-0.04596, B=6.9336. Verify the result is 6.65784.

def test_PredictYUi_NumberInput_CorrectResult(page: Page):
    #arrange
    expected_value = "6.65784"

    #act
    #fill textbox, click button, then find output box (msgBoard)
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox").fill("6, -0.04596, 6.9336")
    page.get_by_role("button", name="Predict Y From Linear Regression Formula | x, m, b on one line").click()
    msgboard = page.locator("#MsgBoard")

    #assert
    expect(msgboard).to_have_text(re.compile(expected_value))