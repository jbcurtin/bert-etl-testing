from bert import constants, utils, binding, aws as bert_aws

@binding.follow('noop')
def test_kms():
    import os
    work_queue, done_queue, ologger = utils.comm_binders(test_kms)
    ologger.info('Key Master test')

    with bert_aws.kms(os.environ['KMS_KEY_ALIAS']) as keymaster:
        github_token: str = keymaster.decrypt(os.environ['GITHUB_TOKEN'])
        github_username: str = keymaster.decrypt(os.environ['GITHUB_USERNAME'])
        ologger.info(f'Github Token[{github_token}]')
        ologger.info(f'Github Username[{github_username}]')
