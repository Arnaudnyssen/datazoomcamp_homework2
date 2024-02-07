if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    #filter with passenger count > and trip distance > 0
    df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    #create a new column lpep_pickup_date as a date

    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    dico_rename={'VendorID':'vendor_id','RatecodeID':'ratecode_id','PULocationID':'pulocation_id','DOLocationID':'dolocation_id'}
    df = df.rename(columns=dico_rename)
    # Assertion 1: vendor_id is one of the existing values in the column
    assert df['vendor_id'].notnull().all(), "Assertion Error: vendor_id contains NaN values"

    # Assertion 2: passenger_count is greater than 0
    assert (df['passenger_count'] > 0).all(),"Assertion Error: passenger_count is not greater than 0"

    # Assertion 3: trip_distance is greater than 0
    assert (df['trip_distance'] > 0).all(),"Assertion Error: trip_distance is not greater than 0"

    return df
    



@test
def test_output(output, *args) -> None:
    
    assert output is not None, 'The output is undefined'
