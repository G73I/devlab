import click
import boto3

# Initialize the AWS S3 and ECS clients
ecs = boto3.client('ecs')

@click.command()
@click.argument('service_name', required=False)
def main(service_name):
    """
    AWS CLI Tool
    """
    if service_name:
        list_ecs_task_versions(service_name)
    else:
        click.echo("You must provide either a bucket name or a service name.")

def list_ecs_task_versions(service_name):
    """
    List versions of an ECS task definition for a service
    """
    try:
        response = ecs.list_task_definitions(familyPrefix=service_name, status='ACTIVE')
        task_versions = response['taskDefinitionArns']
        if task_versions:
            for version in task_versions:
                click.echo(version)
        else:
            click.echo(f"No task definitions found for service: {service_name}")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    main()

