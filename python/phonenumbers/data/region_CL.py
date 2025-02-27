"""Auto-generated file, do not edit by hand. CL metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CL = PhoneMetadata(id='CL', country_code=56, international_prefix='(?:0|1(?:1[0-69]|2[0-57]|5[13-58]|69|7[0167]|8[018]))0',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[2-9]|600|123)\\d{7,8}', possible_number_pattern='\\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:2\\d{7}|1962\\d{4})|(?:3[2-5]|[47][1-35]|5[1-3578]|6[13-57])\\d{7}', possible_number_pattern='\\d{7,9}', example_number='221234567'),
    mobile=PhoneNumberDesc(national_number_pattern='9[5-9]\\d{7}', possible_number_pattern='\\d{8,9}', example_number='961234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}|1230\\d{7}', possible_number_pattern='\\d{9,11}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='600\\d{7,8}', possible_number_pattern='\\d{10,11}', example_number='6001234567'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='44\\d{7}', possible_number_pattern='\\d{9}', example_number='441234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='600\\d{7,8}', possible_number_pattern='\\d{10,11}', example_number='6001234567'),
    national_prefix='0',
    national_prefix_for_parsing='0|(1(?:1[0-69]|2[0-57]|5[13-58]|69|7[0167]|8[018]))',
    number_format=[NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['22'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='$CC (\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[357]|4[1-35]|6[13-57]'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='$CC (\\1)'),
        NumberFormat(pattern='(9)([5-9]\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(44)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['44'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([68]00)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['60|8'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(600)(\\d{3})(\\d{2})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['60'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(1230)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['219'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='$CC (\\1)'),
        NumberFormat(pattern='(\\d{4,5})', format='\\1', leading_digits_pattern=['[1-9]'], national_prefix_formatting_rule='\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['22']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[357]|4[1-35]|6[13-57]']),
        NumberFormat(pattern='(9)([5-9]\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['9']),
        NumberFormat(pattern='(44)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['44']),
        NumberFormat(pattern='([68]00)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['60|8']),
        NumberFormat(pattern='(600)(\\d{3})(\\d{2})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['60']),
        NumberFormat(pattern='(1230)(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\\d{5})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['219'])],
    mobile_number_portable_region=True)
