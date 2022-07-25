PipelineECS(appName: 'hello-world',
        ecrRepository: 'hello-world',
        ecrRegistry: '169889227629.dkr.ecr.us-west-2.amazonaws.com',
        functionalTestCommand: 'sleep 300 && export ALB_DNS_NAME=`terraform output -json alb_dns_name` && pip install -r features/requirements.txt && behave -f html -o test-reports/index.html',
        thisWillDestroyEverything: 'false'
)
