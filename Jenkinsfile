PipelineECS(appName: 'hello-world',
        ecrRepository: 'hello-world',
        ecrRegistry: '169889227629.dkr.ecr.us-west-2.amazonaws.com',
        unitTestCommand: 'pip install -r test/requirements.txt && export WHO="Brian Carpio" && export WHAT="Is DevOps" && python3 -m pytest --junitxml=test-reports/unit-test.xml && pylint --output-format text --output pylint-report.text hello_world',
        snycTargetFile: 'hello_world/requirements.txt',
        snykAdditionalArguments: '--command=python3',
        functionalTestCommand: 'sleep 300 && pip install -r test/requirements.txt && behave --no-capture --no-capture-stderr -f html -o test-reports/index.html test/features/',
        thisWillDestroyEverything: 'false'
)
