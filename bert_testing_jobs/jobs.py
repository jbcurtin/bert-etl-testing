from bert import binding, constants, utils, shortcuts

@binding.follow('noop')
def init_job_queue() -> None:
    work_queue, done_queue, ologger = utils.comm_binders(init_job_queue)
    # for idx in range(0, 500):
    for idx in range(0, 10):
        done_queue.put({'idx': idx})

@binding.follow(init_job_queue, pipeline_type=constants.PipelineType.CONCURRENT)
def handle_job_queue() -> None:
    work_queue, done_queue, ologger = utils.comm_binders(handle_job_queue)
    for details in work_queue:
        done_queue.put(details)

@binding.follow(handle_job_queue)
def conclude_job_queue() -> None:
    work_queue, done_queue, ologger = utils.comm_binders(conclude_job_queue)
    data_points = []
    for details in work_queue:
        data_points.append(details['idx'])

    ologger.info(f'Data Point Length: {len(data_points)}')

