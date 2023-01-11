PipelineECS(appName: 'hello-world',
        ecrRepository: 'hello-world',
        ecrRegistry: '169889227629.dkr.ecr.us-west-2.amazonaws.com',
        unitTestCommand: 'pip install -r hello_world/requirements.txt && tox',
        snycTargetFile: 'hello_world/requirements.txt',
        snykAdditionalArguments: '--command=python3',
        functionalTestCommand: 'sleep 300 && tox -e behave',
        fortifyAppId: '149890',        
        fortifyReleaseName: 'Dev',
        pollFortifyResult: false,
        manifestLocation: 'hello_world/requirements.txt',
        thisWillDestroyEverything: 'false'
)
