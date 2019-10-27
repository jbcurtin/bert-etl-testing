from bert import binding, constants, utils, shortcuts

@binding.follow('noop')
def test_sns_subscription() -> None:
    work_queue, done_queue, ologger = utils.comm_binders(test_sns_subscription)
    for details in work_queue:
        ologger.info(f'SNS Topic[{details}]')

