PipelineECS(appName: 'hello-world',
        ecrRepository: 'hello-world',
        ecrRegistry: '169889227629.dkr.ecr.us-west-2.amazonaws.com',
        unitTestCommand: 'pip install tox && tox',
        snycTargetFile: 'hello_world/requirements.txt',
        snykAdditionalArguments: '--command=python3',
        functionalTestCommand: 'sleep 300 && tox -e behave',
        thisWillDestroyEverything: 'false'
)
