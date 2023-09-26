import click
import boto3

# Initialize the AWS S3 and ECS clients
s3 = boto3.resource('s3')

@click.command()
@click.argument('bucket_name', required=False)
def main(bucket_name):
    """
    AWS CLI Tool
    """
    if bucket_name:
        list_s3_files(bucket_name)
    else:
        click.echo("You must provide a bucket name.")

def list_s3_files(bucket_name):
    """
    List files in an S3 bucket
    """
    try:
        bucket = s3.Bucket(bucket_name)
        for obj in bucket.objects.all():
            click.echo(obj.key)
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    main()
