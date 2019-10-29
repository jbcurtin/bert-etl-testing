import typing

from bert import binding, utils, constants

@binding.follow('noop')
def test_cf_disable():
    import boto3
    work_queue, done_queue, ologger = utils.comm_binders(test_cf_disable)

    cf_client = boto3.client('cloudfront')
    def _load_distro(domain_name: str) -> typing.Dict[str, typing.Any]:
        for page in cf_client.get_paginator('list_distributions').paginate():
            for distro in page['DistributionList']['Items']:
                if distro['DomainName'] == domain_name:
                    return distro

        return None

    distro = _load_distro('d3jrr736oclhqi.cloudfront.net')
    response = cf_client.get_distribution(Id=distro['Id'])
    config = response['Distribution']['DistributionConfig']
    if distro['Status'] == 'Deployed' and config['Enabled'] is True:
        config['Enabled'] = False
        ologger.info(f'Shutting down distro[{distro["Id"]}]')
        cf_client.update_distribution(
            Id=distro['Id'],
            IfMatch=response['ETag'],
            DistributionConfig=config)

    elif distro['Status'] == 'Deployed':
        ologger.info(f'Distro[{distro["Id"]}] is Disabled')

    elif distro['Status'] == 'InProgress':
        ologger.info(f'Distro[{distro["Id"]}] update in progress. Aborting Update')

    else:
        raise NotImplementedError

