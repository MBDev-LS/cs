
def getLongestListLength(lists: list) -> int:
	return max([len(lst for lst in lists)])


def getLongestItemStrInList(lst: list):
	return max([len(str(item)) for item in lst])


def lists_to_table(lists: list, headings: list):
	outputString = ''


