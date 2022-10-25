
def printLog(logType: str, logMessage: str, exitProgram: bool=False):
	print(f'{logType.upper()}: {logMessage}')

	if exitProgram is True:
		exit(1)