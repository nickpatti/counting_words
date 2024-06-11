from main import process_chunk, count_words, format_word_counts


def test_process_chunks_small_file():
    short_string = "Hello, this will test a variety of aspects in a single string: punctuation!!!; CaSing, and frequency of words. This is a test"
    result = process_chunk(chunk=short_string, word_counts={})
    assert result == {'hello': 1, 'this': 2, 'will': 1, 'test': 2, 'a': 3, 'variety': 1, 'of': 2, 'aspects': 1, 'in': 1, 'single': 1, 'string': 1, 'punctuation': 1, 'casing': 1, 'and': 1, 'frequency': 1, 'words': 1, 'is': 1}


def test_count_words_large_file():
    result = count_words("/Users/nickpatti/Documents/projects/globalsign_test/large_test_file.txt", 5)
    expected_output = [('sed', 61848), ('in', 54908), ('ut', 54292), ('et', 50476), ('sit', 47580)]
    assert result == expected_output


def test_count_words_moby_dick():
    result = count_words("/Users/nickpatti/Documents/projects/globalsign_test/moby_dick.txt", 20)
    expected_output = [('the', 4284), ('and', 2192), ('of', 2185), ('a', 1861), ('to', 1685), ('in', 1366), ('i', 1056), ('that', 1024), ('his', 889), ('it', 821), ('he', 783), ('but', 616), ('was', 603), ('with', 595), ('s', 577), ('is', 564), ('for', 551), ('all', 542), ('as', 541), ('at', 458)]
    assert result == expected_output


def test_output_format():
    result = format_word_counts("/Users/nickpatti/Documents/projects/globalsign_test/moby_dick.txt", 20)
    expected_output = ("4284 the\n2192 and\n2185 of\n1861 a\n1685 to\n1366 in\n1056 i\n"
                       "1024 that\n889 his\n821 it\n783 he\n616 but\n603 was\n595 with\n"
                       "577 s\n564 is\n551 for\n542 all\n541 as\n458 at")
    assert result == expected_output












